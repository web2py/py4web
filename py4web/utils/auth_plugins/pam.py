# Modified 2013-2014 Leon Weber <leon@leonweber.de>:
# See README.md for changelog
#
# Original author:
# (c) 2007 Chris AtLee <chris@atlee.ca>
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
"""
PAM module for python
Provides an authenticate function that will allow the caller to authenticate
a user against the Pluggable Authentication Modules (PAM) on the system.
Implemented using ctypes, so no compilation is necessary.
"""
__all__ = ['authenticate']

from ctypes import CDLL, POINTER, Structure, CFUNCTYPE, cast, byref, sizeof
from ctypes import c_void_p, c_uint, c_char_p, c_char, c_int
from ctypes.util import find_library
import sys

libpam = CDLL(find_library("pam"))
libc = CDLL(find_library("c"))

calloc = libc.calloc
calloc.restype = c_void_p
calloc.argtypes = [c_uint, c_uint]

strdup = libc.strdup
strdup.argstypes = [c_char_p]
strdup.restype = POINTER(c_char)  # NOT c_char_p !!!!

# Various constants
PAM_PROMPT_ECHO_OFF = 1
PAM_PROMPT_ECHO_ON = 2
PAM_ERROR_MSG = 3
PAM_TEXT_INFO = 4

PAM_REINITIALIZE_CRED = 0x0008  # This constant is libpam-specific.


class PamHandle(Structure):
    """wrapper class for pam_handle_t"""
    _fields_ = [
        ("handle", c_void_p)
    ]

    def __init__(self):
        Structure.__init__(self)
        self.handle = 0


class PamMessage(Structure):
    """wrapper class for pam_message structure"""
    _fields_ = [
        ("msg_style", c_int),
        ("msg", c_char_p),
    ]

    def __repr__(self):
        return "<PamMessage %i '%s'>" % (self.msg_style, self.msg)


class PamResponse(Structure):
    """wrapper class for pam_response structure"""
    _fields_ = [
        ("resp", c_char_p),
        ("resp_retcode", c_int),
    ]

    def __repr__(self):
        return "<PamResponse %i '%s'>" % (self.resp_retcode, self.resp)

conv_func = CFUNCTYPE(c_int, c_int, POINTER(POINTER(PamMessage)),
                      POINTER(POINTER(PamResponse)), c_void_p)


class PamConv(Structure):
    """wrapper class for pam_conv structure"""
    _fields_ = [
        ("conv", conv_func),
        ("appdata_ptr", c_void_p)
    ]

pam_start = libpam.pam_start
pam_start.restype = c_int
pam_start.argtypes = [c_char_p, c_char_p, POINTER(PamConv),
                      POINTER(PamHandle)]

pam_authenticate = libpam.pam_authenticate
pam_authenticate.restype = c_int
pam_authenticate.argtypes = [PamHandle, c_int]

pam_setcred = libpam.pam_setcred
pam_setcred.restype = c_int
pam_setcred.argtypes = [PamHandle, c_int]

pam_end = libpam.pam_end
pam_end.restype = c_int
pam_end.argtypes = [PamHandle, c_int]


def authenticate(username, password, service='login', encoding='utf-8',
                 resetcred=True):
    """Returns True if the given username and password authenticate for the
    given service.  Returns False otherwise.
    ``username``: the username to authenticate
    ``password``: the password in plain text
    ``service``: the PAM service to authenticate against.
                 Defaults to 'login'
    The above parameters can be strings or bytes.  If they are strings,
    they will be encoded using the encoding given by:
    ``encoding``: the encoding to use for the above parameters if they
                  are given as strings.  Defaults to 'utf-8'
    ``resetcred``: Use the pam_setcred() function to
                   reinitialize the credentials.
                   Defaults to 'True'.
    """

    if sys.version_info >= (3,):
        if isinstance(username, str):
            username = username.encode(encoding)
        if isinstance(password, str):
            password = password.encode(encoding)
        if isinstance(service, str):
            service = service.encode(encoding)

    @conv_func
    def my_conv(n_messages, messages, p_response, app_data):
        """Simple conversation function that responds to any
        prompt where the echo is off with the supplied password"""
        # Create an array of n_messages response objects
        addr = calloc(n_messages, sizeof(PamResponse))
        p_response[0] = cast(addr, POINTER(PamResponse))
        for i in range(n_messages):
            if messages[i].contents.msg_style == PAM_PROMPT_ECHO_OFF:
                pw_copy = strdup(password)
                p_response.contents[i].resp = cast(pw_copy, c_char_p)
                p_response.contents[i].resp_retcode = 0
        return 0

    handle = PamHandle()
    conv = PamConv(my_conv, 0)
    retval = pam_start(service, username, byref(conv), byref(handle))

    if retval != 0:
        # TODO: This is not an authentication error, something
        # has gone wrong starting up PAM
        return False

    retval = pam_authenticate(handle, 0)
    auth_success = (retval == 0)

    # Re-initialize credentials (for Kerberos users, etc)
    # Don't check return code of pam_setcred(), it shouldn't matter
    # if this fails
    if auth_success and resetcred:
        retval = pam_setcred(handle, PAM_REINITIALIZE_CRED)

    pam_end(handle, retval)

    return auth_success

if __name__ == "__main__":
    import getpass
    print(authenticate(getpass.getuser(), getpass.getpass()))
    