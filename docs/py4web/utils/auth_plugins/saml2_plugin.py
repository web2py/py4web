#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
THIS FILE IS A WORK IN PROGRESS AND PROBALY DOES NOT WORK
"""

from saml2 import BINDING_HTTP_POST
from saml2 import BINDING_HTTP_REDIRECT
from saml2.client import Saml2Client
from saml2.config import Config as Saml2Config


def obj2dict(obj, processed=None):
    """
    converts any object into a dict, recursively
    """
    processed = processed if not processed is None else set()
    if obj is None:
        return None
    if isinstance(obj, (int, long, str, unicode, float, bool)):
        return obj
    if id(obj) in processed:
        return "<reference>"
    processed.add(id(obj))
    if isinstance(obj, (list, tuple)):
        return [obj2dict(item, processed) for item in obj]
    if not isinstance(obj, dict) and hasattr(obj, "__dict__"):
        obj = obj.__dict__
    else:
        return repr(obj)
    return dict(
        (key, obj2dict(value, processed))
        for key, value in obj.items()
        if not key.startswith("_")
        and not type(value)
        in (
            types.FunctionType,
            types.LambdaType,
            types.BuiltinFunctionType,
            types.BuiltinMethodType,
        )
    )


def saml2_handler(session, request, config_filename=None, entityid=None):
    config_filename = config_filename or os.path.join(
        request.folder, "private", "sp_conf"
    )
    client = Saml2Client(config_file=config_filename)
    if not entityid:
        idps = client.metadata.with_descriptor("idpsso")
        entityid = idps.keys()[0]
    bindings = [BINDING_HTTP_REDIRECT, BINDING_HTTP_POST]
    binding, destination = client.pick_binding(
        "single_sign_on_service", bindings, "idpsso", entity_id=entityid
    )
    if request.env.request_method == "GET":
        binding = BINDING_HTTP_REDIRECT
    elif request.env.request_method == "POST":
        binding = BINDING_HTTP_POST
    if not request.vars.SAMLResponse:
        req_id, req = client.create_authn_request(
            destination, binding=BINDING_HTTP_POST
        )
        relay_state = web2py_uuid().replace("-", "")
        session.saml_outstanding_queries = {req_id: request.url}
        session.saml_req_id = req_id
        http_args = client.apply_binding(
            binding, str(req), destination, relay_state=relay_state
        )
        return {"url": dict(http_args["headers"])["Location"]}
    else:
        relay_state = request.vars.RelayState
        req_id = session.saml_req_id
        unquoted_response = request.vars.SAMLResponse
        res = {}
        try:
            data = client.parse_authn_request_response(
                unquoted_response, binding, session.saml_outstanding_queries
            )
            res["response"] = data if data else {}
        except Exception as e:
            import traceback

            res["error"] = traceback.format_exc()
        return res


class Saml2Plugin:
    name = "saml2"
    label = "SAMLv2"

    def __init__(
        self,
        config_file,
        maps=None,
        logout_url=None,
        change_password_url=None,
        entityid=None,
    ):
        if maps is None:
            maps = {
                "username": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn",
                "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn",
                "user_id": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn",
            }
        self.config_file = config_file
        self.maps = maps
        self.saml_logout_url = logout_url
        self.saml_change_password_url = change_password_url
        self.entityid = entityid

    def get_login_url(self):
        """returns the url for login"""
        client = Saml2Client(config_file=config_file)
        if not self.entityid:
            idps = client.metadata.with_descriptor("idpsso")
            self.entityid = idps.keys()[0]
        bindings = [BINDING_HTTP_REDIRECT, BINDING_HTTP_POST]
        binding, destination = client.pick_binding(
            "single_sign_on_service", bindings, "idpsso", entity_id=entityid
        )
        req_id, req = client.create_authn_request(
            destination, binding=BINDING_HTTP_POST
        )
        relay_state = web2py_uuid().replace("-", "")
        http_args = client.apply_binding(
            binding, str(req), destination, relay_state=relay_state
        )
        return http_args["headers"]["Location"]

    def callback(self):
        session.saml_outstanding_queries = {req_id: request.url}
        session.saml_req_id = req_id
        return {"url": dict(http_args["headers"])["Location"]}

    def handle_request(self, auth, path, get_vars, post_vars):
        pass

    def login_url(self, next="/"):
        d = saml2_handler(current.session, current.request, entityid=self.entityid)
        if "url" in d:
            redirect(d["url"])
        elif "error" in d:
            current.session.flash = d["error"]
            redirect(URL("default", "index"))
        elif "response" in d:
            # a['assertions'][0]['attribute_statement'][0]['attribute']
            # is list of
            # {'name': 'http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname', 'name_format': None, 'text': None, 'friendly_name': None, 'attribute_value': [{'text': 'CAA\\dev-mdp', 'extension_attributes': "{'{http://www.w3.org/2001/XMLSchema-instance}type': 'xs:string'}", 'extension_elements': []}], 'extension_elements': [], 'extension_attributes': '{}'}
            try:
                attributes = (
                    d["response"].assertions[0].attribute_statement[0].attribute
                )
            except:
                attributes = d["response"].assertion.attribute_statement[0].attribute
            current.session.saml2_info = dict(
                (a.name, [i.text for i in a.attribute_value]) for a in attributes
            )
        return next

    def logout_url(self, next="/"):
        current.session.saml2_info = None
        current.session.auth = None
        self._SAML_logout()
        return next

    def change_password_url(self, next="/"):
        self._SAML_change_password()
        return next

    def get_user(self):
        user = current.session.saml2_info
        if user:
            d = {"source": "web2py saml2"}
            for key in self.maps:
                d[key] = user.get(self.maps[key], [None])[0]
            return d
        return None

    def _SAML_logout(self):
        """
        exposed SAML.logout()
        redirects to the SAML logout page
        """
        redirect(self.saml_logout_url)

    def _SAML_change_password(self):
        redirect(self.saml_change_password_url)
