#!/bin/python
# -*- coding: utf-8 -*-

"""
| This file is part of the py4web Web Framework
| Copyrighted by Massimo Di Pierro <mdipierro@cs.depaul.edu>
| License: "BSDv3" (https://opensource.org/licenses/BSD-3-Clause)
"""

from __future__ import print_function
import email.utils
from email import message_from_string
import json
import logging
import mimetypes
import os
import smtplib

from pydal._compat import *

try:
    from google.appengine.api import mail as google_mail

    GAE = True
except ImportError:
    GAE = False

try:
    import M2Crypto
except ImportError:
    M2Crypto = None

try:
    from pyme import core, errors
    from pyme.constants.sig import mode as pyme_mode
except ImportError:
    pyme = None


class Settings(object):
    pass


class Mailer(object):
    """
    Class for configuring and sending emails with alternative text / html
    body, multiple attachments and encryption support

    Works with SMTP and Google App Engine.

    Args:
        server: SMTP server address in address:port notation
        sender: sender email address
        login: sender login name and password in login:password notation
            or None if no authentication is required
        tls: enables/disables encryption (True by default)

    In Google App Engine use ::

        server='gae'

    For sake of backward compatibility all fields are optional and default
    to None, however, to be able to send emails at least server and sender
    must be specified. They are available under following fields::

        mail.settings.server
        mail.settings.sender
        mail.settings.login
        mail.settings.timeout = 60 # seconds (default)

    When server is 'logging', email is logged but not sent (debug mode)

    Optionally you can use PGP encryption or X509::

        mail.settings.cipher_type = None
        mail.settings.gpg_home = None
        mail.settings.sign = True
        mail.settings.sign_passphrase = None
        mail.settings.encrypt = True
        mail.settings.x509_sign_keyfile = None
        mail.settings.x509_sign_certfile = None
        mail.settings.x509_sign_chainfile = None
        mail.settings.x509_nocerts = False
        mail.settings.x509_crypt_certfiles = None

        cipher_type       : None
                            gpg - need a python-pyme package and gpgme lib
                            x509 - smime
        gpg_home          : you can set a GNUPGHOME environment variable
                            to specify home of gnupg
        sign              : sign the message (True or False)
        sign_passphrase   : passphrase for key signing
        encrypt           : encrypt the message (True or False). It defaults
                            to True
                         ... x509 only ...
        x509_sign_keyfile : the signers private key filename or
                            string containing the key. (PEM format)
        x509_sign_certfile: the signers certificate filename or
                            string containing the cert. (PEM format)
        x509_sign_chainfile: sets the optional all-in-one file where you
                             can assemble the certificates of Certification
                             Authorities (CA) which form the certificate
                             chain of email certificate. It can be a
                             string containing the certs to. (PEM format)
        x509_nocerts      : if True then no attached certificate in mail
        x509_crypt_certfiles: the certificates file or strings to encrypt
                              the messages with can be a file name /
                              string or a list of file names /
                              strings (PEM format)

    Examples:
        Create Mailer object with authentication data for remote server::

            mail = Mailer('example.com:25', 'me@example.com', 'me:password')

    Notice for GAE users:
        Attachments have an automatic content_id='attachment-i' where i is progressive number
        in this way the can be referenced from the HTML as <img src="cid:attachment-0" /> etc.
    """

    class Attachment(MIMEBase):
        """
        Email attachment

        Args:
            payload: path to file or file-like object with read() method
            filename: name of the attachment stored in message; if set to
                None, it will be fetched from payload path; file-like
                object payload must have explicit filename specified
            content_id: id of the attachment; automatically contained within
                `<` and `>`
            content_type: content type of the attachment; if set to None,
                it will be fetched from filename using gluon.contenttype
                module
            encoding: encoding of all strings passed to this function (except
                attachment body)

        Content ID is used to identify attachments within the html body;
        in example, attached image with content ID 'photo' may be used in
        html message as a source of img tag `<img src="cid:photo" />`.

        Example::
            Create attachment from text file::

                attachment = Mailer.Attachment('/path/to/file.txt')

                Content-Type: text/plain
                MIME-Version: 1.0
                Content-Disposition: attachment; filename="file.txt"
                Content-Transfer-Encoding: base64

                SOMEBASE64CONTENT=

            Create attachment from image file with custom filename and cid::

                attachment = Mailer.Attachment('/path/to/file.png',
                                                 filename='photo.png',
                                                 content_id='photo')

                Content-Type: image/png
                MIME-Version: 1.0
                Content-Disposition: attachment; filename="photo.png"
                Content-Id: <photo>
                Content-Transfer-Encoding: base64

                SOMEOTHERBASE64CONTENT=
        """

        def __init__(
            self,
            payload,
            filename=None,
            content_id=None,
            content_type=None,
            encoding="utf-8",
        ):
            if isinstance(payload, str):
                if filename is None:
                    filename = os.path.basename(payload)
                with open(payload, "rb") as fp:
                    payload = fp.read()
            else:
                if filename is None:
                    raise Exception("Missing attachment name")
                payload = payload.read()
            # FIXME PY3 can be used to_native?
            filename = filename.encode(encoding)
            if content_type is None:
                content_type = mimetypes.guess_type(filename)
            self.my_filename = filename
            self.my_payload = payload
            MIMEBase.__init__(self, *content_type.split("/", 1))
            self.set_payload(payload)
            self["Content-Disposition"] = 'attachment; filename="%s"' % to_native(
                filename, encoding
            )
            if content_id is not None:
                self["Content-Id"] = "<%s>" % to_native(content_id, encoding)
            Encoders.encode_base64(self)

    def __init__(self, server=None, sender=None, login=None, tls=True, ssl=False):

        settings = self.settings = Settings()
        settings.logger = logging
        settings.server = server
        settings.sender = sender
        settings.login = login
        settings.tls = tls
        settings.timeout = 5  # seconds
        settings.hostname = None
        settings.ssl = ssl
        settings.cipher_type = None
        settings.gpg_home = None
        settings.sign = True
        settings.sign_passphrase = None
        settings.encrypt = True
        settings.x509_sign_keyfile = None
        settings.x509_sign_certfile = None
        settings.x509_sign_chainfile = None
        settings.x509_nocerts = False
        settings.x509_crypt_certfiles = None
        settings.debug = False
        self.result = {}

    def send(
        self,
        to,
        subject="[no subject]",
        body="[no body]",
        sender=None,
        attachments=None,
        cc=None,
        bcc=None,
        reply_to=None,
        encoding="utf-8",
        raw=False,
        headers={},
        from_address=None,
        cipher_type=None,
        sign=None,
        sign_passphrase=None,
        encrypt=None,
        x509_sign_keyfile=None,
        x509_sign_chainfile=None,
        x509_sign_certfile=None,
        x509_crypt_certfiles=None,
        x509_nocerts=None,
    ):
        """
        Sends an email using data specified in constructor

        Args:
            to: list or tuple of receiver addresses; will also accept single
                object
            subject: subject of the email
            body: email body text; depends on type of passed object:

                - if 2-list or 2-tuple is passed: first element will be
                  source of plain text while second of html text;
                - otherwise: object will be the only source of plain text
                  and html source will be set to None

                If text or html source is:

                - None: content part will be ignored,
                - string: content part will be set to it,
                - file-like object: content part will be fetched from it using
                  it's read() method
            attachments: list or tuple of Mailer.Attachment objects; will also
                accept single object
            cc: list or tuple of carbon copy receiver addresses; will also
                accept single object
            bcc: list or tuple of blind carbon copy receiver addresses; will
                also accept single object
            reply_to: address to which reply should be composed
            encoding: encoding of all strings passed to this method (including
                message bodies)
            headers: dictionary of headers to refine the headers just before
                sending mail, e.g. `{'X-Mailer' : 'web2py mailer'}`
            from_address: address to appear in the 'From:' header, this is not
                the envelope sender. If not specified the sender will be used

            cipher_type :
                gpg - need a python-pyme package and gpgme lib
                x509 - smime
            gpg_home : you can set a GNUPGHOME environment variable
                to specify home of gnupg
            sign : sign the message (True or False)
            sign_passphrase  : passphrase for key signing
            encrypt : encrypt the message (True or False). It defaults to True.
                         ... x509 only ...
            x509_sign_keyfile : the signers private key filename or
                string containing the key. (PEM format)
            x509_sign_certfile: the signers certificate filename or
                string containing the cert. (PEM format)
            x509_sign_chainfile: sets the optional all-in-one file where you
                can assemble the certificates of Certification
                Authorities (CA) which form the certificate
                chain of email certificate. It can be a
                string containing the certs to. (PEM format)
            x509_nocerts : if True then no attached certificate in mail
            x509_crypt_certfiles: the certificates file or strings to encrypt
                the messages with can be a file name / string or
                a list of file names / strings (PEM format)
        Examples:
            Send plain text message to single address::

                mail.send('you@example.com',
                          'Message subject',
                          'Plain text body of the message')

            Send html message to single address::

                mail.send('you@example.com',
                          'Message subject',
                          '<html>Plain text body of the message</html>')

            Send text and html message to three addresses (two in cc)::

                mail.send('you@example.com',
                          'Message subject',
                          ('Plain text body', '<html>html body</html>'),
                          cc=['other1@example.com', 'other2@example.com'])

            Send html only message with image attachment available from the
            message by 'photo' content id::

                mail.send('you@example.com',
                          'Message subject',
                          (None, '<html><img src="cid:photo" /></html>'),
                          Mailer.Attachment('/path/to/photo.jpg'
                                          content_id='photo'))

            Send email with two attachments and no body text::

                mail.send('you@example.com,
                          'Message subject',
                          None,
                          [Mailer.Attachment('/path/to/fist.file'),
                           Mailer.Attachment('/path/to/second.file')])

        Returns:
            True on success, False on failure.

        Before return, method updates two object's fields:

            - self.result: return value of smtplib.SMTP.sendmail() or GAE's
              mail.send_mail() method
        """

        # We don't want to use base64 encoding for unicode mail
        add_charset("utf-8", charset_QP, charset_QP, "utf-8")

        def encode_header(key):
            if [c for c in key if 32 > ord(c) or ord(c) > 127]:
                return Header(key.encode("utf-8"), "utf-8")
            else:
                return key

        # Encoded or raw text
        def encoded_or_raw(text):
            if raw:
                text = encode_header(text)
            return text

        sender = sender or self.settings.sender

        if not isinstance(self.settings.server, str):
            raise Exception("Server address not specified")
        if not isinstance(sender, str):
            raise Exception("Sender address not specified")

        if not raw and attachments:
            # Use multipart/mixed if there is attachments
            payload_in = MIMEMultipart("mixed")
        elif raw:
            # No encoding configuration for raw messages
            if not isinstance(body, basestring):
                body = body.read()
            if isinstance(body, unicodeT):
                text = body.encode("utf-8")
            elif not encoding == "utf-8":
                text = body.decode(encoding).encode("utf-8")
            else:
                text = body
            # No charset passed to avoid transport encoding
            # NOTE: some unicode encoded strings will produce
            # unreadable mail contents.
            payload_in = MIMEText(text)
        if to:
            if not isinstance(to, (list, tuple)):
                to = [to]
        else:
            raise Exception("Target receiver address not specified")
        if cc:
            if not isinstance(cc, (list, tuple)):
                cc = [cc]
        if bcc:
            if not isinstance(bcc, (list, tuple)):
                bcc = [bcc]
        if body is None:
            text = html = None
        elif isinstance(body, (list, tuple)):
            text, html = body
        elif body.strip().startswith("<html") and body.strip().endswith("</html>"):
            text = self.settings.server == "gae" and body or None
            html = body
        else:
            text = body
            html = None

        if (text is not None or html is not None) and (not raw):

            if text is not None:
                if not isinstance(text, basestring):
                    text = text.read()
                if isinstance(text, unicodeT):
                    text = text.encode("utf-8")
                elif not encoding == "utf-8":
                    text = text.decode(encoding).encode("utf-8")
            if html is not None:
                if not isinstance(html, basestring):
                    html = html.read()
                if isinstance(html, unicodeT):
                    html = html.encode("utf-8")
                elif not encoding == "utf-8":
                    html = html.decode(encoding).encode("utf-8")

            # Construct mime part only if needed
            if text is not None and html:
                # We have text and html we need multipart/alternative
                attachment = MIMEMultipart("alternative")
                attachment.attach(MIMEText(text, _charset="utf-8"))
                attachment.attach(MIMEText(html, "html", _charset="utf-8"))
            elif text is not None:
                attachment = MIMEText(text, _charset="utf-8")
            elif html:
                attachment = MIMEText(html, "html", _charset="utf-8")

            if attachments:
                # If there are attachments put text and html into
                # multipart/mixed
                payload_in.attach(attachment)
            else:
                # No attachments no multipart/mixed
                payload_in = attachment

        if (attachments is None) or raw:
            pass
        elif isinstance(attachments, (list, tuple)):
            for attachment in attachments:
                payload_in.attach(attachment)
        else:
            payload_in.attach(attachments)
            attachments = [attachments]

        #######################################################
        #                      CIPHER                         #
        #######################################################
        cipher_type = cipher_type or self.settings.cipher_type
        sign = sign if sign is not None else self.settings.sign
        sign_passphrase = sign_passphrase or self.settings.sign_passphrase
        encrypt = encrypt if encrypt is not None else self.settings.encrypt
        #######################################################
        #                       GPGME                         #
        #######################################################
        if cipher_type == "gpg":
            if self.settings.gpg_home:
                # Set GNUPGHOME environment variable to set home of gnupg
                import os

                os.environ["GNUPGHOME"] = self.settings.gpg_home
            if not sign and not encrypt:
                raise RuntimeError(
                    "No sign and no encrypt is set but cipher type to gpg"
                )
            if not pyme:
                raise RuntimeError("pyme not installed")
            ############################################
            #                   sign                   #
            ############################################
            if sign:
                import string

                core.check_version(None)
                pin = payload_in.as_string().replace("\n", "\r\n")
                plain = core.Data(pin)
                sig = core.Data()
                c = core.Context()
                c.set_armor(1)
                c.signers_clear()
                # Search for signing key for From:
                for sigkey in c.op_keylist_all(sender, 1):
                    if sigkey.can_sign:
                        c.signers_add(sigkey)
                if not c.signers_enum(0):
                    raise RuntimeError("No key for signing [%s]" % sender)
                c.set_passphrase_cb(lambda x, y, z: sign_passphrase)
                try:
                    # Make a signature
                    c.op_sign(plain, sig, pyme_mode.DETACH)
                    sig.seek(0, 0)
                    # Make it part of the email
                    payload = MIMEMultipart(
                        "signed",
                        boundary=None,
                        _subparts=None,
                        **dict(micalg="pgp-sha1", protocol="application/pgp-signature")
                    )
                    # Insert the origin payload
                    payload.attach(payload_in)
                    # Insert the detached signature
                    p = MIMEBase("application", "pgp-signature")
                    p.set_payload(sig.read())
                    payload.attach(p)
                    # It's just a trick to handle the no encryption case
                    payload_in = payload
                except errors.GPGMEError as ex:
                    raise RuntimeError("GPG error: %s" % ex.getstring())

            ############################################
            #                  encrypt                 #
            ############################################
            if encrypt:
                core.check_version(None)
                plain = core.Data(payload_in.as_string())
                cipher = core.Data()
                c = core.Context()
                c.set_armor(1)
                # Collect the public keys for encryption
                recipients = []
                rec = to[:]
                if cc:
                    rec.extend(cc)
                if bcc:
                    rec.extend(bcc)
                for addr in rec:
                    c.op_keylist_start(addr, 0)
                    r = c.op_keylist_next()
                    if r is None:
                        raise RuntimeError("No key for [%s]" % addr)
                    recipients.append(r)
                try:
                    # Make the encryption
                    c.op_encrypt(recipients, 1, plain, cipher)
                    cipher.seek(0, 0)
                    # Make it a part of the email
                    payload = MIMEMultipart(
                        "encrypted",
                        boundary=None,
                        _subparts=None,
                        **dict(protocol="application/pgp-encrypted")
                    )
                    p = MIMEBase("application", "pgp-encrypted")
                    p.set_payload("Version: 1\r\n")
                    payload.attach(p)
                    p = MIMEBase("application", "octet-stream")
                    p.set_payload(cipher.read())
                    payload.attach(p)
                except errors.GPGMEError as ex:
                    raise RuntimeError("GPG error: %s" % ex.getstring())

        #######################################################
        #                       X.509                         #
        #######################################################
        elif cipher_type == "x509":
            if not sign and not encrypt:
                raise RuntimeError(
                    "No sign and no encrypt have been set but cipher type set to x509"
                )

            import os

            x509_sign_keyfile = x509_sign_keyfile or self.settings.x509_sign_keyfile

            x509_sign_chainfile = (
                x509_sign_chainfile or self.settings.x509_sign_chainfile
            )

            x509_sign_certfile = (
                x509_sign_certfile
                or self.settings.x509_sign_certfile
                or x509_sign_keyfile
                or self.settings.x509_sign_certfile
            )

            # crypt certfiles could be a string or a list
            x509_crypt_certfiles = (
                x509_crypt_certfiles or self.settings.x509_crypt_certfiles
            )

            x509_nocerts = x509_nocerts or self.settings.x509_nocerts

            # Missing needed m2crypto
            if not M2Crypto:
                raise RuntimeError("Can't load M2Crypto module")
            BIO, SMIME, X509 = M2Crypto.BIO, M2Crypto.SMIME, M2Crypto.X509

            msg_bio = BIO.MemoryBuffer(payload_in.as_string())
            s = SMIME.SMIME()

            # SIGN
            if sign:
                # Key for signing
                try:
                    keyfile_bio = (
                        BIO.openfile(x509_sign_keyfile)
                        if os.path.isfile(x509_sign_keyfile)
                        else BIO.MemoryBuffer(x509_sign_keyfile)
                    )
                    sign_certfile_bio = (
                        BIO.openfile(x509_sign_certfile)
                        if os.path.isfile(x509_sign_certfile)
                        else BIO.MemoryBuffer(x509_sign_certfile)
                    )
                    s.load_key_bio(
                        keyfile_bio,
                        sign_certfile_bio,
                        callback=lambda x: sign_passphrase,
                    )
                    if x509_sign_chainfile:
                        sk = X509.X509_Stack()
                        chain = (
                            X509.load_cert(x509_sign_chainfile)
                            if os.path.isfile(x509_sign_chainfile)
                            else X509.load_cert_string(x509_sign_chainfile)
                        )
                        sk.push(chain)
                        s.set_x509_stack(sk)
                except Exception as e:
                    raise RuntimeError(
                        "Something went wrong with certificate or private key loading: <%s>"
                        % str(e)
                    )

                try:
                    if x509_nocerts:
                        flags = SMIME.PKCS7_NOCERTS
                    else:
                        flags = 0
                    if not encrypt:
                        flags += SMIME.PKCS7_DETACHED
                    p7 = s.sign(msg_bio, flags=flags)
                    msg_bio = BIO.MemoryBuffer(
                        payload_in.as_string()
                    )  # Recreate coz sign() has consumed it.
                except Exception as e:
                    raise RuntimeError(
                        "Something went wrong with signing: <%s> %s"
                        % (str(e), str(flags))
                    )

            # ENCRYPT
            if encrypt:
                try:
                    sk = X509.X509_Stack()
                    if not isinstance(x509_crypt_certfiles, (list, tuple)):
                        x509_crypt_certfiles = [x509_crypt_certfiles]

                    # Make an encryption certificate's stack
                    for crypt_certfile in x509_crypt_certfiles:
                        certfile = (
                            X509.load_cert(crypt_certfile)
                            if os.path.isfile(crypt_certfile)
                            else X509.load_cert_string(crypt_certfile)
                        )
                        sk.push(certfile)
                    s.set_x509_stack(sk)

                    s.set_cipher(SMIME.Cipher("des_ede3_cbc"))
                    tmp_bio = BIO.MemoryBuffer()
                    if sign:
                        s.write(tmp_bio, p7)
                    else:
                        tmp_bio.write(payload_in.as_string())
                    p7 = s.encrypt(tmp_bio)
                except Exception as e:
                    raise RuntimeError(
                        "Something went wrong with encrypting: <%s>" % str(e)
                    )

            # Final stage: Sign and Encrypt
            out = BIO.MemoryBuffer()
            if encrypt:
                s.write(out, p7)
            else:
                if sign:
                    s.write(out, p7, msg_bio, SMIME.PKCS7_DETACHED)
                else:
                    out.write("\r\n")
                    out.write(payload_in.as_string())
            out.close()
            st = str(out.read())
            payload = message_from_string(st)
        else:
            # No cryptography process as usual
            payload = payload_in

        if from_address:
            payload["From"] = encoded_or_raw(to_unicode(from_address, encoding))
        else:
            payload["From"] = encoded_or_raw(to_unicode(sender, encoding))
        origTo = to[:]
        if to:
            payload["To"] = encoded_or_raw(to_unicode(", ".join(to), encoding))
        if reply_to:
            payload["Reply-To"] = encoded_or_raw(to_unicode(reply_to, encoding))
        if cc:
            payload["Cc"] = encoded_or_raw(to_unicode(", ".join(cc), encoding))
            to.extend(cc)
        if bcc:
            to.extend(bcc)
        payload["Subject"] = encoded_or_raw(to_unicode(subject, encoding))
        payload["Date"] = email.utils.formatdate()
        for k, v in iteritems(headers):
            payload[k] = encoded_or_raw(to_unicode(v, encoding))
        result = {}
        try:
            if self.settings.server == "logging":
                entry = (
                    "email not sent\n%s\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n%s\n"
                    % ("-" * 40, sender, ", ".join(to), subject, text or html, "-" * 40)
                )
                self.settings.logger.warning(entry)
            elif self.settings.server.startswith("logging:"):
                entry = (
                    "email not sent\n%s\nFrom: %s\nTo: %s\nSubject: %s\n\n%s\n%s\n"
                    % ("-" * 40, sender, ", ".join(to), subject, text or html, "-" * 40)
                )
                open(self.settings.server[8:], "a").write(entry)
            elif self.settings.server == "gae":
                if not GAE:
                    raise RuntimeError("Not running on GAE")
                xcc = dict()
                if cc:
                    xcc["cc"] = cc
                if bcc:
                    xcc["bcc"] = bcc
                if reply_to:
                    xcc["reply_to"] = reply_to

                attachments = attachments and [
                    google_mail.Attachment(
                        a.my_filename, a.my_payload, content_id="<attachment-%s>" % k
                    )
                    for k, a in enumerate(attachments)
                    if not raw
                ]
                if attachments:
                    result = google_mail.send_mail(
                        sender=sender,
                        to=origTo,
                        subject=to_unicode(subject, encoding),
                        body=to_unicode(text or "", encoding),
                        html=html,
                        attachments=attachments,
                        **xcc
                    )
                elif html and (not raw):
                    result = google_mail.send_mail(
                        sender=sender,
                        to=origTo,
                        subject=to_unicode(subject, encoding),
                        body=to_unicode(text or "", encoding),
                        html=html,
                        **xcc
                    )
                else:
                    result = google_mail.send_mail(
                        sender=sender,
                        to=origTo,
                        subject=to_unicode(subject, encoding),
                        body=to_unicode(text or "", encoding),
                        **xcc
                    )
            elif self.settings.server == "aws":
                import boto3
                from botocore.exceptions import ClientError

                client = boto3.client("ses")
                try:
                    raw = {"Data": payload.as_string()}
                    response = client.send_raw_email(
                        RawMessage=raw, Source=sender, Destinations=to
                    )
                    return True
                except ClientError as e:
                    raise RuntimeError()
            else:
                smtp_args = self.settings.server.split(":")
                kwargs = dict(timeout=self.settings.timeout)
                func = smtplib.SMTP_SSL if self.settings.ssl else smtplib.SMTP
                server = func(*smtp_args, **kwargs)
                try:
                    if self.settings.tls and not self.settings.ssl:
                        server.ehlo(self.settings.hostname)
                        server.starttls()
                        server.ehlo(self.settings.hostname)
                    if self.settings.login:
                        server.login(*self.settings.login.split(":", 1))
                    result = server.sendmail(sender, to, payload.as_string())
                finally:
                    # do not want to hide errors raising some exception here
                    try:
                        server.quit()
                    except:
                        pass
                    # ensure to close any socket with SMTP server
                    try:
                        server.close()
                    except:
                        pass
        except Exception as e:
            self.settings.logger.warning("Mailer.send failure:%s" % e)
            self.result = result
            raise
        self.result = result
        self.error = None
        return True
