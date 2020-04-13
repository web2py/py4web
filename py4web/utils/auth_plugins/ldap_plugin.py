# -*- coding: utf-8 -*-
#
# last tinkered with by korylprince at gmail.com on 2012-07-12
#

import sys
import logging
import ldap  # python-ldap
import ldap.filter
from py4web.utils.tags import Tags

ldap.set_option(ldap.OPT_REFERRALS, 0)


class LDAPPlugin(object):

    name = "ldap"

    """
    to use ldap login with MS Active Directory:

          auth.register_plugin(LDAPPlugin(
            mode='ad', server='my.domain.controller',
            base_dn='ou=Users,dc=domain,dc=com'))

    to use ldap login with Notes Domino:

          auth.register_plugin(LDAPPlugin(
            mode='domino',server='my.domino.server'))

    to use ldap login with OpenLDAP:

        auth.register_plugin(LDAPPlugin(
            mode='cn', server='my.ldap.server', base_dn='ou=Users,dc=domain,dc=com'))

    to use ldap login with OpenLDAP and subtree search and (optionally)
    multiple DNs:

        auth.register_plugin(LDAPPlugin(
            mode='uid_r', server='my.ldap.server',
            base_dn=['ou=Users,dc=domain,dc=com','ou=Staff,dc=domain,dc=com']))

    or (if using CN):

        auth.register_plugin(LDAPPlugin(
            mode='cn', server='my.ldap.server',
            base_dn='ou=Users,dc=domain,dc=com'))

    or you can full customize the search for user:

        auth.register_plugin(LDAPPlugin(
            mode='custom', server='my.ldap.server',
            base_dn='ou=Users,dc=domain,dc=com',
            username_attrib='uid',
            custom_scope='subtree'))

    the custom_scope can be: base, onelevel, subtree.

    If using secure ldaps:// pass secure=True and cert_path="..."
    If ldap is using GnuTLS then you need cert_file="..." instead cert_path
    because cert_path isn't implemented in GnuTLS :(

    To enable TLS, set tls=True:

        auth.register_plugin(LDAPPlugin(
            server='my.ldap.server',
            base_dn='ou=Users,dc=domain,dc=com',
            tls=True))

    If you need to bind to the directory with an admin account in order to
    search it then specify bind_dn & bind_pw to use for this.
    - currently only implemented for Active Directory

    If you need to restrict the set of allowed users (e.g. to members of a
    department) then specify an rfc4515 search filter string.
    - currently only implemented for mode in ['ad', 'company', 'uid_r']

    You can manage user attributes first name, last name, email from ldap:

        auth.register_plugin(LDAPPlugin(
            ...as usual...,
            manage_user=True,
            user_firstname_attrib='cn:1',
            user_lastname_attrib='cn:2',
            user_mail_attrib='mail'
           ))

    Where:
    manage_user - let web2py handle user data from ldap
    user_firstname_attrib - the attribute containing the user's first name
                            optionally you can specify parts.
                            Example: cn: "John Smith" - 'cn:1'='John'
    user_lastname_attrib - the attribute containing the user's last name
                            optionally you can specify parts.
                            Example: cn: "John Smith" - 'cn:2'='Smith'
    user_mail_attrib - the attribute containing the user's email address


    If you need group control from ldap to py4web app's database feel free
    to set:

        auth.register_plugin(LDAPPlugin(
            ...as usual...,
            manage_groups=True,
            db=db,
            group_dn='ou=Groups,dc=domain,dc=com',
            group_name_attrib='cn',
            group_member_attrib='memberUid',
            group_filterstr='objectClass=*'
           ))

        Where:
        manage_groups - let web2py handle the groups from ldap
        db - is the database object (need to have auth_user, auth_group,
            auth_membership)
        group_dn - the ldap branch of the groups
        group_name_attrib - the attribute where the group name is stored
        group_member_attrib - the attribute containing the group members name
        group_filterstr - as the filterstr but for group select

    **allowed_groups still to be implemented in py4web**
    You can restrict login access to specific groups if you specify:

        auth.register_plugin(LDAPPlugin(
            ...as usual...,
            allowed_groups=[...],
            group_dn='ou=Groups,dc=domain,dc=com',
            group_name_attrib='cn',
            group_member_attrib='memberUid',#use 'member' for Active Directory
            group_filterstr='objectClass=*'
           ))

        Where:
        allowed_groups - a list with allowed ldap group names
        group_dn - the ldap branch of the groups
        group_name_attrib - the attribute where the group name is stored
        group_member_attrib - the attribute containing the group members name
        group_filterstr - as the filterstr but for group select

    If using Active Directory you must specify bind_dn and bind_pw for
    allowed_groups unless anonymous bind works.

    You can set the logging level with the "logging_level" parameter, default
    is "error" and can be set to error, warning, info, debug.
    """

    def __init__(
        self,
        server="ldap",
        port=None,
        base_dn="ou=users,dc=domain,dc=com",
        mode="uid",
        secure=False,
        self_signed_certificate=None,  # See NOTE below
        cert_path=None,
        cert_file=None,
        cacert_path=None,
        cacert_file=None,
        key_file=None,
        bind_dn=None,
        bind_pw=None,
        filterstr="objectClass=*",
        username_attrib="uid",
        custom_scope="subtree",
        allowed_groups=None,
        manage_user=False,
        user_firstname_attrib="cn:1",
        user_lastname_attrib="cn:2",
        user_mail_attrib="mail",
        manage_groups=False,
        manage_groups_callback=[],
        db=None,
        group_dn=None,
        group_name_attrib="cn",
        group_member_attrib="memberUid",
        group_filterstr="objectClass=*",
        group_mapping={},
        tls=False,
        logger=logging,
        groups=None,
    ):

        self.server = server
        self.port = port
        self.base_dn = base_dn
        self.mode = mode
        self.secure = secure
        self.self_signed_certificate = self_signed_certificate
        self.cert_path = cert_path
        self.cert_file = cert_file
        self.cacert_path = cacert_path
        self.cacert_file = cacert_file
        self.key_file = key_file
        self.bind_dn = bind_dn
        self.bind_pw = bind_pw
        self.filterstr = filterstr
        self.username_attrib = username_attrib
        self.custom_scope = custom_scope
        self.allowed_groups = allowed_groups
        self.manage_user = manage_user
        self.user_firstname_attrib = user_firstname_attrib
        self.user_lastname_attrib = user_lastname_attrib
        self.user_mail_attrib = user_mail_attrib
        self.manage_groups = manage_groups
        self.manage_groups_callback = manage_groups_callback
        self.db = db
        self.group_dn = group_dn
        self.group_name_attrib = group_name_attrib
        self.group_member_attrib = group_member_attrib
        self.group_filterstr = group_filterstr
        self.group_mapping = group_mapping
        self.tls = tls
        self.logger = logger
        # rfc4515 syntax
        self.filterstr = self.filterstr.lstrip("(").rstrip(")")
        self.groups = groups

    def check_credentials(self, username, password):

        server = self.server
        port = self.port
        base_dn = self.base_dn
        mode = self.mode
        secure = self.secure
        self_signed_certificate = self.self_signed_certificate
        cert_path = self.cert_path
        cert_file = self.cert_file
        cacert_path = self.cacert_path
        cacert_file = self.cacert_file
        key_file = self.key_file
        bind_dn = self.bind_dn
        bind_pw = self.bind_pw
        filterstr = self.filterstr
        username_attrib = self.username_attrib
        custom_scope = self.custom_scope
        allowed_groups = self.allowed_groups
        manage_user = self.manage_user
        user_firstname_attrib = self.user_firstname_attrib
        user_lastname_attrib = self.user_lastname_attrib
        user_mail_attrib = self.user_mail_attrib
        manage_groups = self.manage_groups
        manage_groups_callback = self.manage_groups_callback
        db = self.db
        group_dn = self.db
        group_name_attrib = self.group_name_attrib
        group_member_attrib = self.group_member_attrib
        group_filterstr = self.group_filterstr
        group_mapping = self.group_mapping
        tls = self.tls
        logger = self.logger

        if password == "":  # http://tools.ietf.org/html/rfc4513#section-5.1.2
            logger.warning("blank password not allowed")
            return False
        logger.debug(
            "mode: [%s] manage_user: [%s] custom_scope: [%s] manage_groups: [%s]"
            % (str(mode), str(manage_user), str(custom_scope), str(manage_groups))
        )
        if manage_user:
            if user_firstname_attrib.count(":") > 0:
                (
                    user_firstname_attrib,
                    user_firstname_part,
                ) = user_firstname_attrib.split(":", 1)
                user_firstname_part = int(user_firstname_part) - 1
            else:
                user_firstname_part = None
            if user_lastname_attrib.count(":") > 0:
                (user_lastname_attrib, user_lastname_part) = user_lastname_attrib.split(
                    ":", 1
                )
                user_lastname_part = int(user_lastname_part) - 1
            else:
                user_lastname_part = None
            user_firstname_attrib = ldap.filter.escape_filter_chars(
                user_firstname_attrib
            )
            user_lastname_attrib = ldap.filter.escape_filter_chars(user_lastname_attrib)
            user_mail_attrib = ldap.filter.escape_filter_chars(user_mail_attrib)
        try:
            # if allowed_groups:
            #    if not self.is_user_in_allowed_groups(
            #        username, password, allowed_groups
            #    ):
            #        return False
            con = self._init_ldap()
            if mode == "ad":
                # Microsoft Active Directory
                if "@" not in username:
                    domain = []
                    for x in base_dn.split(","):
                        if "DC=" in x.upper():
                            domain.append(x.split("=")[-1])
                    username = "%s@%s" % (username, ".".join(domain))
                username_bare = username.split("@")[0]
                con.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
                # In cases where ForestDnsZones and DomainDnsZones are found,
                # result will look like the following:
                # ['ldap://ForestDnsZones.domain.com/DC=ForestDnsZones,
                #    DC=domain,DC=com']
                if bind_dn:
                    # need to search directory with an admin account 1st
                    con.simple_bind_s(bind_dn, bind_pw)
                else:
                    # credentials should be in the form of username@domain.tld
                    con.simple_bind_s(username, password)
                # this will throw an index error if the account is not found
                # in the base_dn
                requested_attrs = ["sAMAccountName"]
                if manage_user:
                    requested_attrs.extend(
                        [user_firstname_attrib, user_lastname_attrib, user_mail_attrib]
                    )

                result = con.search_ext_s(
                    base_dn,
                    ldap.SCOPE_SUBTREE,
                    "(&(sAMAccountName=%s)(%s))"
                    % (ldap.filter.escape_filter_chars(username_bare), filterstr),
                    requested_attrs,
                )[0][1]
                if not isinstance(result, dict):
                    # result should be a dict in the form
                    # {'sAMAccountName': [username_bare]}
                    logger.warning("User [%s] not found!" % username)
                    return False
                if bind_dn:
                    # We know the user exists & is in the correct OU
                    # so now we just check the password
                    con.simple_bind_s(username, password)
                username = username_bare

            if mode == "domino":
                # Notes Domino
                if "@" in username:
                    username = username.split("@")[0]
                con.simple_bind_s(username, password)
                if manage_user:
                    # TODO: sorry I have no clue how to query attrs in domino
                    result = {
                        user_firstname_attrib: username,
                        user_lastname_attrib: None,
                        user_mail_attrib: None,
                    }

            if mode == "cn":
                # OpenLDAP (CN)
                if bind_dn and bind_pw:
                    con.simple_bind_s(bind_dn, bind_pw)
                dn = "cn=" + username + "," + base_dn
                con.simple_bind_s(dn, password)
                if manage_user:
                    result = con.search_s(
                        dn,
                        ldap.SCOPE_BASE,
                        "(objectClass=*)",
                        [user_firstname_attrib, user_lastname_attrib, user_mail_attrib],
                    )[0][1]

            if mode == "uid":
                # OpenLDAP (UID)
                if bind_dn and bind_pw:
                    con.simple_bind_s(bind_dn, bind_pw)
                    dn = "uid=" + username + "," + base_dn
                    dn = con.search_s(
                        base_dn, ldap.SCOPE_SUBTREE, "(uid=%s)" % username, [""]
                    )[0][0]
                else:
                    dn = "uid=" + username + "," + base_dn
                con.simple_bind_s(dn, password)
                if manage_user:
                    result = con.search_s(
                        dn,
                        ldap.SCOPE_BASE,
                        "(objectClass=*)",
                        [user_firstname_attrib, user_lastname_attrib, user_mail_attrib],
                    )[0][1]

            if mode == "company":
                # no DNs or password needed to search directory
                dn = ""
                pw = ""
                # bind anonymously
                con.simple_bind_s(dn, pw)
                # search by e-mail address
                filter = "(&(mail=%s)(%s))" % (
                    ldap.filter.escape_filter_chars(username),
                    filterstr,
                )
                # find the uid
                attrs = ["uid"]
                if manage_user:
                    attrs.extend(
                        [user_firstname_attrib, user_lastname_attrib, user_mail_attrib]
                    )
                # perform the actual search
                company_search_result = con.search_s(
                    base_dn, ldap.SCOPE_SUBTREE, filter, attrs
                )
                dn = company_search_result[0][0]
                result = company_search_result[0][1]
                # perform the real authentication test
                con.simple_bind_s(dn, password)

            if mode == "uid_r":
                # OpenLDAP (UID) with subtree search and multiple DNs
                if isinstance(base_dn, list):
                    basedns = base_dn
                else:
                    basedns = [base_dn]
                filter = "(&(uid=%s)(%s))" % (
                    ldap.filter.escape_filter_chars(username),
                    filterstr,
                )
                found = False
                for basedn in basedns:
                    try:
                        result = con.search_s(basedn, ldap.SCOPE_SUBTREE, filter)
                        if result:
                            user_dn = result[0][0]
                            # Check the password
                            con.simple_bind_s(user_dn, password)
                            found = True
                            break
                    except ldap.LDAPError as detail:
                        (exc_type, exc_value) = sys.exc_info()[:2]
                        logger.warning(
                            "ldap_auth: searching %s for %s resulted in %s: %s\n"
                            % (basedn, filter, exc_type, exc_value)
                        )
                if not found:
                    logger.warning("User [%s] not found!" % username)
                    return False
                result = result[0][1]
            if mode == "custom":
                # OpenLDAP (username_attrs) with subtree search and
                # multiple DNs
                if isinstance(base_dn, list):
                    basedns = base_dn
                else:
                    basedns = [base_dn]
                filter = "(&(%s=%s)(%s))" % (
                    username_attrib,
                    ldap.filter.escape_filter_chars(username),
                    filterstr,
                )
                if custom_scope == "subtree":
                    scope = ldap.SCOPE_SUBTREE
                elif custom_scope == "base":
                    scope = ldap.SCOPE_BASE
                elif custom_scope == "onelevel":
                    scope = ldap.SCOPE_ONELEVEL
                found = False
                for basedn in basedns:
                    try:
                        result = con.search_s(basedn, scope, filter)
                        if result:
                            user_dn = result[0][0]
                            # Check the password
                            con.simple_bind_s(user_dn, password)
                            found = True
                            break
                    except ldap.LDAPError as detail:
                        (exc_type, exc_value) = sys.exc_info()[:2]
                        logger.warning(
                            "ldap_auth: searching %s for %s resulted in %s: %s\n"
                            % (basedn, filter, exc_type, exc_value)
                        )
                if not found:
                    logger.warning("User [%s] not found!" % username)
                    return False
                result = result[0][1]
            if manage_user:
                logger.info("[%s] Manage user data" % str(username))
                try:
                    store_sso_id = "ldap:" + username
                    user_firstname = result[user_firstname_attrib][0]
                    if user_firstname_part is not None:
                        store_user_firstname = user_firstname.split(
                            b" " if isinstance(user_firstname, bytes) else " ", 1
                        )[user_firstname_part]
                    else:
                        store_user_firstname = user_firstname
                except KeyError as e:
                    store_user_firstname = None
                try:
                    user_lastname = result[user_lastname_attrib][0]
                    if user_lastname_part is not None:
                        store_user_lastname = user_lastname.split(
                            b" " if isinstance(user_lastname, bytes) else " ", 1
                        )[user_lastname_part]
                    else:
                        store_user_lastname = user_lastname
                except KeyError as e:
                    store_user_lastname = None
                try:
                    store_user_mail = result[user_mail_attrib][0]
                except KeyError as e:
                    store_user_mail = None
                update_or_insert_values = {
                    "first_name": store_user_firstname,
                    "last_name": store_user_lastname,
                    "email": store_user_mail,
                    "username": username,
                    "sso_id": store_sso_id,
                }
                if "@" not in username:
                    # user as username
                    # ################
                    fields = ["first_name", "last_name", "email"]
                    user_in_db = db(db.auth_user.username == username)
                elif "@" in username:
                    # user as email
                    # #############
                    fields = ["first_name", "last_name"]
                    user_in_db = db(db.auth_user.email == username)
                    update_or_insert_values = dict(
                        ((f, update_or_insert_values[f]) for f in fields)
                    )

                if user_in_db.count() > 0:
                    actual_values = (
                        user_in_db.select(*[db.auth_user[f] for f in fields])
                        .first()
                        .as_dict()
                    )
                    if (
                        update_or_insert_values != actual_values
                    ):  # We don't update record if values are the same
                        user_in_db.update(**update_or_insert_values)
                else:
                    db.auth_user.insert(**update_or_insert_values)

                if manage_groups:
                    if not self.do_manage_groups(con, username, group_mapping):
                        return False

            con.unbind()
            return True
        except ldap.INVALID_CREDENTIALS as e:
            return False
        except ldap.LDAPError as e:
            import traceback

            logger.warning("[%s] Error in ldap processing" % str(username))
            logger.debug(traceback.format_exc())
            print(traceback.format_exc())
            return False
        except IndexError as ex:  # for AD membership test
            import traceback

            logger.warning("[%s] Ldap result indexing error" % str(username))
            logger.debug(traceback.format_exc())
            return False

    def is_user_in_allowed_groups(self, username, password=None):

        server = self.server
        port = self.port
        base_dn = self.base_dn
        mode = self.mode
        secure = self.secure
        self_signed_certificate = self.self_signed_certificate
        cert_path = self.cert_path
        cert_file = self.cert_file
        cacert_path = self.cacert_path
        cacert_file = self.cacert_file
        key_file = self.key_file
        bind_dn = self.bind_dn
        bind_pw = self.bind_pw
        filterstr = self.filterstr
        username_attrib = self.username_attrib
        custom_scope = self.custom_scope
        allowed_groups = self.allowed_groups
        manage_user = self.manage_user
        user_firstname_attrib = self.user_firstname_attrib
        user_lastname_attrib = self.user_lastname_attrib
        user_mail_attrib = self.user_mail_attrib
        manage_groups = self.manage_groups
        manage_groups_callback = self.manage_groups_callback
        db = self.db
        group_dn = self.db
        group_name_attrib = self.group_name_attrib
        group_member_attrib = self.group_member_attrib
        group_filterstr = self.group_filterstr
        group_mapping = self.group_mapping
        tls = self.tls
        logger = self.logger

        """
        Figure out if the username is a member of an allowed group
        in ldap or not
        """
        #
        # Get all group name where the user is in actually in ldap
        # #########################################################
        self.groups = self.get_user_groups_from_ldap(username, password)

        # search for allowed group names
        if not isinstance(allowed_groups, list):
            allowed_groups = [allowed_groups]
        for group in allowed_groups:
            if group in self.groups:
                # Match
                return True
        # No match
        return False

    def do_manage_groups(self, con, username, group_mapping={}):
        """
        Manage user groups

        Get all user's groups from ldap and refresh the already stored
        ones in py4web's application database or create new groups
        according to ldap.
        """
        server = self.server
        port = self.port
        base_dn = self.base_dn
        mode = self.mode
        secure = self.secure
        self_signed_certificate = self.self_signed_certificate
        cert_path = self.cert_path
        cert_file = self.cert_file
        cacert_path = self.cacert_path
        cacert_file = self.cacert_file
        key_file = self.key_file
        bind_dn = self.bind_dn
        bind_pw = self.bind_pw
        filterstr = self.filterstr
        username_attrib = self.username_attrib
        custom_scope = self.custom_scope
        allowed_groups = self.allowed_groups
        manage_user = self.manage_user
        user_firstname_attrib = self.user_firstname_attrib
        user_lastname_attrib = self.user_lastname_attrib
        user_mail_attrib = self.user_mail_attrib
        manage_groups = self.manage_groups
        manage_groups_callback = self.manage_groups_callback
        db = self.db
        group_dn = self.db
        group_name_attrib = self.group_name_attrib
        group_member_attrib = self.group_member_attrib
        group_filterstr = self.group_filterstr
        group_mapping = self.group_mapping
        tls = self.tls
        logger = self.logger
        groups = self.groups

        logger.info("[%s] Manage user groups" % str(username))
        try:
            #
            # Get all group name where the user is in actually in ldap
            # #########################################################
            ldap_groups_of_the_user = self.get_user_groups_from_ldap(con, username)

            if group_mapping != {}:
                l = []
                for group in ldap_groups_of_the_user:
                    if group in group_mapping:
                        l.append(group_mapping[group])
                ldap_groups_of_the_user = l
                logger.info("User groups after remapping: %s" % str(l))

            #
            # Get all group name where the user is in actually in local db
            # #############################################################
            try:
                db_user_id = (
                    db(db.auth_user.username == username)
                    .select(db.auth_user.id)
                    .first()
                    .id
                )
            except:
                try:
                    db_user_id = (
                        db(db.auth_user.email == username)
                        .select(db.auth_user.id)
                        .first()
                        .id
                    )
                except AttributeError as e:
                    #
                    # There is no user in local db
                    # We create one
                    # ##############################
                    try:
                        db_user_id = db.auth_user.insert(
                            username=username, first_name=username
                        )
                    except AttributeError as e:
                        db_user_id = db.auth_user.insert(
                            email=username, first_name=username
                        )
            if not db_user_id:
                logger.error("There is no username or email for %s!" % username)
                raise
            db_groups_of_the_user = groups.get(db_user_id)

            auth_membership_changed = False
            #
            # Delete user membership from groups where user is not anymore
            # #############################################################
            for group_to_del in db_groups_of_the_user:
                if ldap_groups_of_the_user.count(group_to_del) == 0:
                    groups.remove(db_user_id, group_to_del)
                    auth_membership_changed = True

            #
            # Create user membership in groups where user is not in already
            # ##############################################################
            for group_to_add in ldap_groups_of_the_user:
                if db_groups_of_the_user.count(group_to_add) == 0:
                    groups.add(db_user_id, group_to_add)
                    auth_membership_changed = True

            if auth_membership_changed:
                for callback in manage_groups_callback:
                    callback()
        except:
            logger.warning("[%s] Groups are not managed successfully!" % str(username))
            import traceback

            logger.debug(traceback.format_exc())
            return False
        return True

    def _init_ldap(self):
        """
        Inicialize ldap connection
        """

        server = self.server
        port = self.port
        base_dn = self.base_dn
        mode = self.mode
        secure = self.secure
        self_signed_certificate = self.self_signed_certificate
        cert_path = self.cert_path
        cert_file = self.cert_file
        cacert_path = self.cacert_path
        cacert_file = self.cacert_file
        key_file = self.key_file
        bind_dn = self.bind_dn
        bind_pw = self.bind_pw
        filterstr = self.filterstr
        username_attrib = self.username_attrib
        custom_scope = self.custom_scope
        allowed_groups = self.allowed_groups
        manage_user = self.manage_user
        user_firstname_attrib = self.user_firstname_attrib
        user_lastname_attrib = self.user_lastname_attrib
        user_mail_attrib = self.user_mail_attrib
        manage_groups = self.manage_groups
        manage_groups_callback = self.manage_groups_callback
        db = self.db
        group_dn = self.db
        group_name_attrib = self.group_name_attrib
        group_member_attrib = self.group_member_attrib
        group_filterstr = self.group_filterstr
        group_mapping = self.group_mapping
        tls = self.tls
        logger = self.logger

        logger.info("[%s] Initialize ldap connection" % str(server))
        if secure:
            if not port:
                port = 636

            if self_signed_certificate:
                # NOTE : If you have a self-signed SSL Certificate pointing over "port=686" and "secure=True" alone
                #        will not work, you need also to set "self_signed_certificate=True".
                # Ref1: https://onemoretech.wordpress.com/2015/06/25/connecting-to-ldap-over-self-signed-tls-with-python/
                # Ref2: http://bneijt.nl/blog/post/connecting-to-ldaps-with-self-signed-cert-using-python/
                ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

            if cacert_path:
                ldap.set_option(ldap.OPT_X_TLS_CACERTDIR, cacert_path)

            if cacert_file:
                ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
                ldap.set_option(ldap.OPT_X_TLS_CACERTFILE, cacert_file)
            if cert_file:
                ldap.set_option(ldap.OPT_X_TLS_CERTFILE, cert_file)
            if key_file:
                ldap.set_option(ldap.OPT_X_TLS_KEYFILE, key_file)

            con = ldap.initialize("ldaps://" + server + ":" + str(port))
        else:
            if not port:
                port = 389
            con = ldap.initialize("ldap://" + server + ":" + str(port))
        if tls:
            con.start_tls_s()
        return con

    def get_user_groups_from_ldap(self, con, username):
        """
        Get all group names from ldap where the user is in
        """

        server = self.server
        port = self.port
        base_dn = self.base_dn
        mode = self.mode
        secure = self.secure
        self_signed_certificate = self.self_signed_certificate
        cert_path = self.cert_path
        cert_file = self.cert_file
        cacert_path = self.cacert_path
        cacert_file = self.cacert_file
        key_file = self.key_file
        bind_dn = self.bind_dn
        bind_pw = self.bind_pw
        filterstr = self.filterstr
        username_attrib = self.username_attrib
        custom_scope = self.custom_scope
        allowed_groups = self.allowed_groups
        manage_user = self.manage_user
        user_firstname_attrib = self.user_firstname_attrib
        user_lastname_attrib = self.user_lastname_attrib
        user_mail_attrib = self.user_mail_attrib
        manage_groups = self.manage_groups
        manage_groups_callback = self.manage_groups_callback
        db = self.db
        group_dn = self.group_dn
        group_name_attrib = self.group_name_attrib
        group_member_attrib = self.group_member_attrib
        group_filterstr = self.group_filterstr
        group_mapping = self.group_mapping
        tls = self.tls
        logger = self.logger
        groups = self.groups

        logger.info("[%s] Get user groups from ldap" % str(username))
        #
        # Get all group name where the user is in actually in ldap
        # #########################################################
        if mode == "ad":
            #
            # Get the AD username
            # ####################
            if "@" not in username:
                domain = []
                for x in base_dn.split(","):
                    if "DC=" in x.upper():
                        domain.append(x.split("=")[-1])
                username = "%s@%s" % (username, ".".join(domain))
            username_bare = username.split("@")[0]
            con.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
            # In cases where ForestDnsZones and DomainDnsZones are found,
            # result will look like the following:
            # ['ldap://ForestDnsZones.domain.com/DC=ForestDnsZones,
            #     DC=domain,DC=com']
            # We have to use the full string
            bare = ldap.filter.escape_filter_chars(username_bare)
            username = con.search_ext_s(
                base_dn,
                ldap.SCOPE_SUBTREE,
                "(&(sAMAccountName=%s)(%s))" % (bare, filterstr),
                ["cn"],
            )[0][0]

        # if username is None, return empty list
        if username is None:
            return []
        # search for groups where user is in
        filter = "(&(%s=%s)(%s))" % (
            ldap.filter.escape_filter_chars(group_member_attrib),
            ldap.filter.escape_filter_chars(username),
            group_filterstr,
        )
        group_search_result = con.search_s(
            group_dn, ldap.SCOPE_SUBTREE, filter, [group_name_attrib]
        )
        ldap_groups_of_the_user = list()
        for group_row in group_search_result:
            group = group_row[1]
            if isinstance(group, dict) and group_name_attrib in group:
                ldap_groups_of_the_user.append(
                    str(group[group_name_attrib][0], encoding="utf-8")
                )
                print(ldap_groups_of_the_user)

        logger.debug("User groups: %s" % ldap_groups_of_the_user)
        return list(ldap_groups_of_the_user)

        if filterstr[0] == "(" and filterstr[-1] == ")":  # rfc4515 syntax
            filterstr = filterstr[1:-1]  # parens added again where used
        return []
