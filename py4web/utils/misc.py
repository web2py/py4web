#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name,redefined-builtin

"""
| This file is part of the web2py Web Framework
| Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
| License: LGPLv3 (http://www.gnu.org/licenses/lgpl.html)

This file specifically includes utilities for security.
--------------------------------------------------------
"""

import base64
import hashlib
import hmac
import json
import logging
import os
import random
import re
import socket
import struct
import sys
import threading
import time
import uuid
import zlib

from Crypto.Cipher import AES

_struct_2_long_long = struct.Struct("=QQ")

HAVE_COMPARE_DIGEST = False
if hasattr(hmac, "compare_digest"):
    HAVE_COMPARE_DIGEST = True


def AES_new(key, IV=None):
    """Return an AES cipher object and random IV if None specified."""
    if IV is None:
        IV = fast_urandom16()
    return AES.new(key, AES.MODE_CBC, IV), IV


def compare(a, b):
    """Compares two strings and not vulnerable to timing attacks"""
    if HAVE_COMPARE_DIGEST:
        return hmac.compare_digest(a, b)
    result = len(a) ^ len(b)
    for i in range(len(b)):
        result |= ord(a[i % len(a)]) ^ ord(b[i])
    return result == 0


def pad(s, n=32):
    """does padding according to PKCS7v1.5 https://www.ietf.org/rfc/rfc2315.txt"""
    padlen = n - len(s) % n
    return s + bytes(bytearray(padlen * [padlen]))


def unpad(s, n=32):
    """removed padding"""
    padlen = s[-1]
    if isinstance(padlen, str):
        padlen = ord(padlen)  # python2
    if (padlen < 1) | (padlen > n):  # avoid short-circuit
        # return garbage to minimize side channels
        return bytes(bytearray(len(s) * [0]))
    return s[:-padlen]


def secure_dumps(data, encryption_key, hash_key=None, compression_level=None):
    """dumps data, followed by a signature"""
    dump = json.dumps(data).encode()
    if compression_level:
        dump = zlib.compress(dump, compression_level)
    if not hash_key:
        hash_key = hashlib.sha256(encryption_key).digest()
    cipher, IV = AES_new(pad(encryption_key)[:32])
    encrypted_data = base64.urlsafe_b64encode(IV + cipher.encrypt(pad(dump)))
    signature = hmac.new(hash_key, encrypted_data, hashlib.sha256).hexdigest()
    return f"v1-hmac256:{signature}:{encrypted_data.decode()}"


def secure_loads(data, encryption_key, hash_key=None, compression_level=None):
    """loads a signed data dump"""
    version, signature, encrypted_data = data.split(":", 2)
    assert version == "v1-hmac256"
    if not hash_key:
        hash_key = hashlib.sha256(encryption_key).digest()
    encrypted_data = encrypted_data.encode()
    actual_signature = hmac.new(hash_key, encrypted_data, hashlib.sha256).hexdigest()
    assert compare(signature, actual_signature)
    encrypted_data = base64.urlsafe_b64decode(encrypted_data)
    IV, encrypted_data = encrypted_data[:16], encrypted_data[16:]
    cipher, _ = AES_new(pad(encryption_key)[:32], IV=IV)
    data = unpad(cipher.decrypt(encrypted_data))
    if compression_level:
        data = zlib.decompress(data)
    return json.loads(data.decode())


def initialize_urandom():
    """
    This function and the web2py_uuid follow from the following discussion:
    `http://groups.google.com/group/web2py-developers/browse_thread/thread/7fd5789a7da3f09`

    At startup web2py compute a unique ID that identifies the machine by adding
    uuid.getnode() + int(time.time() * 1e3)

    This is a 48-bit number. It converts the number into 16 8-bit tokens.
    It uses this value to initialize the entropy source ('/dev/urandom') and to seed random.

    If os.random() is not supported, it falls back to using random and issues a warning.
    """
    node_id = uuid.getnode()
    microseconds = int(time.time() * 1e6)
    ctokens = [((node_id + microseconds) >> ((i % 6) * 8)) % 256 for i in range(16)]
    random.seed(node_id + microseconds)
    try:
        os.urandom(1)
        have_urandom = True
        if sys.platform != "win32":
            try:
                # try to add process-specific entropy
                frandom = open("/dev/urandom", "wb")
                try:
                    frandom.write(bytes([]).join(bytes([t]) for t in ctokens))
                finally:
                    frandom.close()
            except IOError:
                # works anyway
                pass
    except NotImplementedError:
        have_urandom = False
        logging.warning(
            """Cryptographically secure session management is not possible on your system because
your system does not provide a cryptographically secure entropy source.
This is not specific to web2py; consider deploying on a different operating system."""
        )
    packed = bytes([]).join(bytes([x]) for x in ctokens)
    unpacked_ctokens = _struct_2_long_long.unpack(packed)
    return unpacked_ctokens, have_urandom


UNPACKED_CTOKENS, HAVE_URANDOM = initialize_urandom()


def fast_urandom16(urandom=[], locker=threading.RLock()):
    """
    This is 4x faster than calling os.urandom(16) and prevents
    the "too many files open" issue with concurrent access to os.urandom()
    """
    try:
        return urandom.pop()
    except IndexError:
        try:
            locker.acquire()
            ur = os.urandom(16 * 1024)
            urandom += [ur[i : i + 16] for i in range(16, 1024 * 16, 16)]
            return ur[0:16]
        finally:
            locker.release()


REGEX_IPv4 = re.compile(r"(\d+)\.(\d+)\.(\d+)\.(\d+)")


def is_valid_ip_address(address):
    """
    Examples:
        Better than a thousand words::

            >>> is_valid_ip_address('127.0')
            False
            >>> is_valid_ip_address('127.0.0.1')
            True
            >>> is_valid_ip_address('2001:660::1')
            True
    """
    # deal with special cases
    if address.lower() in ("127.0.0.1", "localhost", "::1", "::ffff:127.0.0.1"):
        return True
    elif address.lower() in ("unknown", ""):
        return False
    elif address.count(".") == 3:  # assume IPv4
        if address.startswith("::ffff:"):
            address = address[7:]
        if hasattr(socket, "inet_aton"):  # try validate using the OS
            try:
                socket.inet_aton(address)
                return True
            except socket.error:  # invalid address
                return False
        else:  # try validate using Regex
            match = REGEX_IPv4.match(address)
            if match and all(0 <= int(match.group(i)) < 256 for i in (1, 2, 3, 4)):
                return True
            return False
    elif hasattr(socket, "inet_pton"):  # assume IPv6, try using the OS
        try:
            socket.inet_pton(socket.AF_INET6, address)
            return True
        except socket.error:  # invalid address
            return False
    else:  # do not know what to do? assume it is a valid address
        return True


def is_loopback_ip_address(ip=None, addrinfo=None):
    """
    Determines whether the address appears to be a loopback address.
    This assumes that the IP is valid.
    """
    if addrinfo:  # see socket.getaddrinfo() for layout of addrinfo tuple
        if addrinfo[0] == socket.AF_INET or addrinfo[0] == socket.AF_INET6:
            ip = addrinfo[4]
    if not isinstance(ip, (str, bytes)):
        return False
    # IPv4 or IPv6-embedded IPv4 or IPv4-compatible IPv6
    if ip.count(".") == 3:
        return ip.lower().startswith(
            ("127", "::127", "0:0:0:0:0:0:127", "::ffff:127", "0:0:0:0:0:ffff:127")
        )
    return ip == "::1" or ip == "0:0:0:0:0:0:0:1"  # IPv6 loopback


def getipaddrinfo(host):
    """
    Filter out non-IP and bad IP addresses from getaddrinfo
    """
    try:
        return [
            addrinfo
            for addrinfo in socket.getaddrinfo(host, None)
            if (addrinfo[0] == socket.AF_INET or addrinfo[0] == socket.AF_INET6)
            and isinstance(addrinfo[4][0], (str, bytes))
        ]
    except socket.error:
        return []


def unlocalised_http_header_date(data):
    """
    Converts input datetime to format defined by RFC 7231, section 7.1.1.1

    Previously, %a and %b formats were used for weekday and month names, but
    those are not locale-safe. uWSGI requires latin1-encodable headers and
    for example in cs_CS locale, fourth day in week is not encodable in latin1,
    as it's "Čt".

    Example output: Sun, 06 Nov 1994 08:49:37 GMT
    """

    short_weekday = {
        "0": "Sun",
        "1": "Mon",
        "2": "Tue",
        "3": "Wed",
        "4": "Thu",
        "5": "Fri",
        "6": "Sat",
    }.get(time.strftime("%w", data))

    day_of_month = time.strftime("%d", data)

    short_month = {
        "01": "Jan",
        "02": "Feb",
        "03": "Mar",
        "04": "Apr",
        "05": "May",
        "06": "Jun",
        "07": "Jul",
        "08": "Aug",
        "09": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec",
    }.get(time.strftime("%m", data))

    year_and_time = time.strftime("%Y %H:%M:%S GMT", data)

    return "{}, {} {} {}".format(
        short_weekday, day_of_month, short_month, year_and_time
    )
