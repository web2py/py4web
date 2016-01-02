#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import portalocker
try:
    import cPickle as pickle
except:
    import pickle
from pickle import Pickler, MARK, DICT, EMPTY_DICT
from types import DictionaryType
import cStringIO
import datetime
import re
import copy_reg
import Cookie
import os
import sys
import traceback
import threading
import cgi
import urlparse
import copy
import tempfile

from gluon.current import current
from gluon.storage import Storage, List
from gluon.utils import web2py_uuid
from gluon.dal import Field
from gluon.fileutils import up
import gluon.recfile as recfile

regex_session_id = re.compile('^([\w\-]+/)?[\w\-\.]+$')

class Session(Storage):
    """
    Defines the session object and the default values of its members (None)

    - session_storage_type   : 'file', 'db', or 'cookie'
    - session_cookie_compression_level :
    - session_cookie_expires : cookie expiration
    - session_cookie_key     : for encrypted sessions in cookies
    - session_id             : a number or None if no session
    - session_id_name        :
    - session_locked         :
    - session_masterapp      :
    - session_new            : a new session obj is being created
    - session_hash           : hash of the pickled loaded session
    - session_pickled        : picked session

    if session in cookie:

    - session_data_name      : name of the cookie for session data

    if session in db:

    - session_db_record_id
    - session_db_table
    - session_db_unique_key

    if session in file:

    - session_file
    - session_filename
    """

    def enable(self,
               db=None,
               tablename='web2py_session',
               masterapp=None,
               migrate=True,
               separate=None,
               check_client=False,
               cookie_key=None,
               cookie_expires=None,
               compression_level=None
               ):

        """
        Used in models, allows to customize Session handling

        Args:
            request: the request object
            response: the response object
            db: to store/retrieve sessions in db (a table is created)
            tablename(str): table name
            masterapp(str): points to another's app sessions. This enables a
                "SSO" environment among apps
            migrate: passed to the underlying db
            separate: with True, creates a folder with the 2 initials of the
                session id. Can also be a function, e.g. ::

                    separate=lambda(session_name): session_name[-2:]

            check_client: if True, sessions can only come from the same ip
            cookie_key(str): secret for cookie encryption
            cookie_expires: sets the expiration of the cookie
            compression_level(int): 0-9, sets zlib compression on the data
                before the encryption
        """

        self._enabled = True        
        request = current.request
        response = current.response
        masterapp = masterapp or request.application
        cookies = request.cookies

        if hasattr(response, 'session_file'):
            self._unlock()

        response.session_masterapp = masterapp
        response.session_db_table = None
        response.session_id_name = 'session_id_%s' % masterapp.lower()
        response.session_data_name = 'session_data_%s' % masterapp.lower()
        response.session_cookie_expires = cookie_expires
        response.session_client = str(request.client).replace(':', '.')
        response.session_cookie_key = cookie_key
        response.session_cookie_compression_level = compression_level
        response.session_new = False
        response.session_file = None
        response.session_storage_type = 'cookie' if cookie_key else 'db' if db else 'file'

        # check if there is a session_id in cookies
        try:
            old_session_id = cookies[response.session_id_name].value
        except KeyError:
            old_session_id = None
        response.session_id = old_session_id

        if response.session_storage_type == 'cookie':
            # check if there is session data in cookies
            if response.session_data_name in cookies:
                session_cookie_data = cookies[response.session_data_name].value
            else:
                session_cookie_data = None
            if session_cookie_data:
                data = secure_loads(session_cookie_data, cookie_key,
                                    compression_level=compression_level)
                if data:
                    self.update(data)
            response.session_id = True

        # else if we are supposed to use file based sessions
        elif response.session_storage_type == 'file':
            # check if the session_id points to a valid sesion filename
            if response.session_id:
                if not regex_session_id.match(response.session_id):
                    response.session_id = None
                else:
                    response.session_filename = \
                        os.path.join(up(request.folder), masterapp,
                                     'sessions', response.session_id)
                    try:
                        response.session_file = \
                            recfile.open(response.session_filename, 'rb+')
                        portalocker.lock(response.session_file,
                                         portalocker.LOCK_EX)
                        response.session_locked = True
                        self.update(pickle.load(response.session_file))
                        response.session_file.seek(0)
                        oc = response.session_filename.split('/')[-1].split('-')[0]
                        if check_client and response.session_client != oc:
                            raise Exception("cookie attack")
                    except:
                        response.session_id = None
            if not response.session_id:
                uuid = web2py_uuid()
                response.session_id = '%s-%s' % (response.session_client, uuid)
                separate = separate and (lambda session_name: session_name[-2:])
                if separate:
                    prefix = separate(response.session_id)
                    response.session_id = '%s/%s' % (prefix, response.session_id)
                response.session_filename = \
                    os.path.join(up(request.folder), masterapp,
                                 'sessions', response.session_id)
                response.session_new = True

        # else the session goes in db
        elif response.session_storage_type == 'db':
            # if had a session on file alreday, close it (yes, can happen)
            if response.session_file:
                self._close(response)
            if masterapp == request.application:
                table_migrate = migrate
            else:
                table_migrate = False
            tname = tablename + '_' + masterapp
            table = db.get(tname, None)
            # Field = db.Field
            if table is None:
                db.define_table(
                    tname,
                    Field('locked', 'boolean', default=False),
                    Field('client_ip', length=64),
                    Field('created_datetime', 'datetime',
                          default=request.now),
                    Field('modified_datetime', 'datetime'),
                    Field('unique_key', length=64),
                    Field('session_data', 'blob'),
                    migrate=table_migrate,
                )
                table = db[tname]  # to allow for lazy table
            response.session_db_table = table
            if response.session_id:
                # Get session data out of the database
                try:
                    (record_id, unique_key) = response.session_id.split(':')
                    record_id = long(record_id)
                except (TypeError, ValueError):
                    record_id = None

                # Select from database
                if record_id:
                    row = table(record_id, unique_key=unique_key)
                    # Make sure the session data exists in the database
                    if row:
                        # rows[0].update_record(locked=True)
                        # Unpickle the data
                        session_data = pickle.loads(row.session_data)
                        self.update(session_data)
                        response.session_new = False
                    else:
                        record_id = None
                if record_id:
                    response.session_id = '%s:%s' % (record_id, unique_key)
                    response.session_db_unique_key = unique_key
                    response.session_db_record_id = record_id
                else:
                    response.session_id = None
                    response.session_new = True
            # if there is no session id yet, we'll need to create a
            # new session
            else:
                response.session_new = True

        # set the cookie now if you know the session_id so user can set
        # cookie attributes in controllers/models
        # cookie will be reset later
        # yet cookie may be reset later
        #   Removed comparison between old and new session ids - should send
        #    the cookie all the time
        if isinstance(response.session_id, str):
            response.cookies[response.session_id_name] = response.session_id
            response.cookies[response.session_id_name]['path'] = '/'
            if cookie_expires:
                response.cookies[response.session_id_name]['expires'] = \
                    cookie_expires.strftime(FMT)

        response.session_hash = self.session_hash()

        if self.flash:
            (response.flash, self.flash) = (self.flash, None)

    def session_hash(self):
        session_pickled = pickle.dumps(self, pickle.HIGHEST_PROTOCOL)
        current.response.session_pickled = session_pickled
        return hashlib.md5(session_pickled).hexdigest()

    def renew(self, clear_session=False):

        if clear_session:
            self.clear()

        request = current.request
        response = current.response
        session = current.session
        masterapp = response.session_masterapp
        cookies = request.cookies

        if response.session_storage_type == 'cookie':
            return

        # if the session goes in file
        if response.session_storage_type == 'file':
            self._close(response)
            uuid = web2py_uuid()
            response.session_id = '%s-%s' % (response.session_client, uuid)
            separate = (lambda s: s[-2:]) if session and response.session_id[2:3] == "/" else None
            if separate:
                prefix = separate(response.session_id)
                response.session_id = '%s/%s' % \
                    (prefix, response.session_id)
            response.session_filename = \
                os.path.join(up(request.folder), masterapp,
                             'sessions', response.session_id)
            response.session_new = True

        # else the session goes in db
        elif response.session_storage_type == 'db':
            table = response.session_db_table

            # verify that session_id exists
            if response.session_file:
                self._close(response)
            if response.session_new:
                return
            # Get session data out of the database
            if response.session_id is None:
                return
            (record_id, sep, unique_key) = response.session_id.partition(':')

            if record_id.isdigit() and long(record_id) > 0:
                new_unique_key = web2py_uuid()
                row = table(record_id)
                if row and row.unique_key == unique_key:
                    table._db(table.id == record_id).update(unique_key=new_unique_key)
                else:
                    record_id = None
            if record_id:
                response.session_id = '%s:%s' % (record_id, new_unique_key)
                response.session_db_record_id = record_id
                response.session_db_unique_key = new_unique_key
            else:
                response.session_new = True

    def _fixup_before_save(self):
        response = current.response
        rcookies = response.cookies
        scookies = rcookies.get(response.session_id_name)
        if not scookies:
            return
        if not self._enabled:
            del rcookies[response.session_id_name]
            return
        if self.get('httponly_cookies',True):
            scookies['HttpOnly'] = True
        if self._secure:
            scookies['secure'] = True

    def clear_session_cookies(self):
        request = current.request
        response = current.response
        session = current.session
        masterapp = response.session_masterapp
        cookies = request.cookies
        rcookies = response.cookies
        # if not cookie_key, but session_data_name in cookies
        # expire session_data_name from cookies
        if response.session_data_name in cookies:
            rcookies[response.session_data_name] = 'expired'
            rcookies[response.session_data_name]['path'] = '/'
            rcookies[response.session_data_name]['expires'] = PAST
        if response.session_id_name in rcookies:
            del rcookies[response.session_id_name]

    def save_session_id_cookie(self):
        request = current.request
        response = current.response
        session = current.session
        masterapp = response.session_masterapp
        cookies = request.cookies
        rcookies = response.cookies

        # if not cookie_key, but session_data_name in cookies
        # expire session_data_name from cookies
        if not response.session_cookie_key:
            if response.session_data_name in cookies:
                rcookies[response.session_data_name] = 'expired'
                rcookies[response.session_data_name]['path'] = '/'
                rcookies[response.session_data_name]['expires'] = PAST
        if response.session_id:
            rcookies[response.session_id_name] = response.session_id
            rcookies[response.session_id_name]['path'] = '/'
            expires = response.session_cookie_expires
            if isinstance(expires, datetime.datetime):
                expires = expires.strftime(FMT)
            if expires:
                rcookies[response.session_id_name]['expires'] = expires

    def clear(self):
        # see https://github.com/web2py/web2py/issues/735
        response = current.response
        if response.session_storage_type == 'file':
            target = recfile.generate(response.session_filename)
            try:
                self._close(response)
                os.unlink(target)
            except:
                pass
        elif response.session_storage_type == 'db':
            table = response.session_db_table
            if response.session_id:
                (record_id, sep, unique_key) = response.session_id.partition(':')
                if record_id.isdigit() and long(record_id) > 0:
                    table._db(table.id == record_id).delete()
        Storage.clear(self)

    def is_new(self):
        if self._start_timestamp:
            return False
        else:
            self._start_timestamp = datetime.datetime.today()
            return True

    def is_expired(self, seconds=3600):
        now = datetime.datetime.today()
        if not self._last_timestamp or \
                self._last_timestamp + datetime.timedelta(seconds=seconds) > now:
            self._last_timestamp = now
            return False
        else:
            return True

    def secure(self):
        self._secure = True

    def forget(self):
        self._close(current.response)
        self._enabled = False

    def _try_store_in_cookie(self, request, response):
        if not self._enabled or self._unchanged(response):
            # self.save_session_id_cookie() # CHECK THIS
            return False
        name = response.session_data_name
        compression_level = response.session_cookie_compression_level
        value = secure_dumps(dict(self),
                             response.session_cookie_key,
                             compression_level=compression_level)
        rcookies = response.cookies
        rcookies.pop(name, None)
        rcookies[name] = value
        rcookies[name]['path'] = '/'
        expires = response.session_cookie_expires
        if isinstance(expires, datetime.datetime):
            expires = expires.strftime(FMT)
        if expires:
            rcookies[name]['expires'] = expires
        return True

    def _unchanged(self, response):
        return response.session_hash == self.session_hash()

    def _try_store_in_db(self, request, response):
        # don't save if file-based sessions,
        # no session id, or session being forgotten
        # or no changes to session (Unless the session is new)
        if not self._enabled: return False
            
        if not response.session_db_table or (self._unchanged(response) and not response.session_new):
            return False

        table = response.session_db_table
        record_id = response.session_db_record_id
        if response.session_new:
            unique_key = web2py_uuid()
        else:
            unique_key = response.session_db_unique_key

        session_pickled = response.session_pickled or pickle.dumps(self, pickle.HIGHEST_PROTOCOL)

        dd = dict(locked=False,
                  client_ip=response.session_client,
                  modified_datetime=request.now,
                  session_data=session_pickled,
                  unique_key=unique_key)
        if record_id:
            if not table._db(table.id == record_id).update(**dd):
                record_id = None
        if not record_id:
            record_id = table.insert(**dd)
            response.session_id = '%s:%s' % (record_id, unique_key)
            response.session_db_unique_key = unique_key
            response.session_db_record_id = record_id

        self.save_session_id_cookie()
        return True

    def _try_store_in_cookie_or_file(self, request, response):
        if not self._enabled: return
        if response.session_storage_type == 'file':
            return self._try_store_in_file(request, response)
        elif response.session_storage_type == 'cookie':
            return self._try_store_in_cookie(request, response)

    def _try_store_in_file(self, request, response):
        if not self._enabled: return
        try:
            if (not response.session_id or self._unchanged(response)):
                # self.save_session_id_cookie() # CHECK THIS
                return False
            if response.session_new or not response.session_file:
                # Tests if the session sub-folder exists, if not, create it
                session_folder = os.path.dirname(response.session_filename)
                if not os.path.exists(session_folder):
                    os.mkdir(session_folder)
                response.session_file = recfile.open(response.session_filename, 'wb')
                portalocker.lock(response.session_file, portalocker.LOCK_EX)
                response.session_locked = True
            if response.session_file:
                session_pickled = response.session_pickled or pickle.dumps(self, pickle.HIGHEST_PROTOCOL)
                response.session_file.write(session_pickled)
                response.session_file.truncate()
        finally:
            self._close(response)

        self.save_session_id_cookie()
        return True

    def _unlock(self):
        response = current.response
        if response and getattr(response,'session_file',None) and getattr(response,'session_locked',None):
            try:
                portalocker.unlock(response.session_file)
                response.session_locked = False
            except:  # this should never happen but happens in Windows
                pass

    def _close(self, response):
        if response and response.session_file:
            self._unlock()
            try:
                response.session_file.close()
                del response.session_file
            except:
                pass

def pickle_session(s):
    return Session, (dict(s),)

copy_reg.pickle(Session, pickle_session)
