# webauthn_plugin.py (VERSIÓN FINAL CON RENDERIZADO Y GUARDADO ROBUSTO)

import json
import logging
import base64

from yatl.helpers import A, DIV, H4, P, SPAN, UL, LI, BUTTON
from py4web.core import Field, request, response, HTTP, URL
from pydal.validators import IS_EMAIL
# i18n settings

from webauthn import (
    generate_registration_options,
    verify_registration_response,
    generate_authentication_options,
    verify_authentication_response,
    options_to_json,
    base64url_to_bytes,
)
from webauthn.helpers.structs import (
    AuthenticatorSelectionCriteria,
    AuthenticatorAttachment,
    PublicKeyCredentialDescriptor,
)

log = logging.getLogger(__name__)


# --- Helpers functions ---
def contains_dangerous_chars(text, dangerous_chars):
  """
  Checks if any character from a list of dangerous characters is present in a string.

  Args:
    text: The string to check.
    dangerous_chars: A list of characters considered dangerous.

  Returns:
    True if any dangerous character is found in the string, False otherwise.
  """
  for char in dangerous_chars:
    if char in text:
      return True
  return False

def bytes_to_urlsafe_b64(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode('utf-8')

def urlsafe_b64_to_bytes(data: str) -> bytes:
    padding = b'=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data.encode('utf-8') + padding)


class WebAuthnPlugin:
    def __init__(self, auth, session, rp_name: str, rp_id: str, origin: str):
        self.auth = auth; self.db = auth.db; self.session = session; self.rp_name = rp_name
        self.rp_id = rp_id; self.origin = origin; self.define_tables()

    def define_tables(self):
        self.db.define_table("webauthn_credentials", Field("user_id", "reference auth_user", ondelete="CASCADE"), Field("name", "string"), Field("credential_id", "string", unique=True), Field("public_key", "string"), Field("sign_count", "integer", default=0))
        self.db.commit()

    def handle_request(self, path: str):
        if path == "manage": return self._manage()
        elif path == "register_begin": return self._register_begin()
        elif path == "register_complete": return self._register_complete()
        elif path == "login_begin": return self._login_begin()
        elif path == "login_complete": return self._login_complete()
        elif path == "delete": return self._delete_credential()
        else: raise HTTP(404)

    def _manage(self):
        #print(self.auth.current_user)
        if not self.auth.current_user: raise HTTP(401)
        user_id = self.auth.current_user["id"]
        creds = self.db(self.db.webauthn_credentials.user_id == user_id).select()
        #print(creds)
        cred_list_items = []
        for cred in creds:
            #log.error(cred)
            HTML_ELEMENT = DIV(
                H4(cred.name or "Key without name", _class="is-size-5"),
                P(f"ID: {cred.credential_id[:8]}...", _class="has-text-grey"),
                BUTTON("Delete", _class="button is-danger is-small", _onclick=f"deleteCredential('{cred.id}')"),
            _class="box"
            )

            cred_list_items.append(HTML_ELEMENT)
        cred_list_items = UL(*cred_list_items, _class="webauthn-credentials-list")
        
        return DIV(H4("Register a new security key or passkeys"),
                   P("Name for the new key/passkeys"),
                   DIV(A("Register new key", _id="btn-register", _class="button is-primary"), _class="my-4"),
                   H4("Registered Keys"),
                   DIV(cred_list_items) if cred_list_items else P("There are no registered keys."), P(_id="status", _class="has-text-info mt-4"))

    def _delete_credential(self):
        if not self.auth.current_user: raise HTTP(401)
        cred_id = request.json.get("id")
        if not cred_id: raise HTTP(400)
        num_deleted = self.db((self.db.webauthn_credentials.id == cred_id) & (self.db.webauthn_credentials.user_id == self.auth.current_user["id"])).delete()
        if num_deleted == 0: raise HTTP(404)
        return {"status": "ok"}
        
    def _register_begin(self):
        if not self.auth.current_user: raise HTTP(401)
        user = self.auth.current_user
        creds = self.db(self.db.webauthn_credentials.user_id == user["id"]).select()
        exclude_credentials = [PublicKeyCredentialDescriptor(id=bytes.fromhex(c.credential_id)) for c in creds]
        options = generate_registration_options(rp_id=self.rp_id, rp_name=self.rp_name, user_id=str(user["id"]).encode("utf-8"), user_name=user["email"], exclude_credentials=exclude_credentials)
        self.session["webauthn_challenge"] = bytes_to_urlsafe_b64(options.challenge)
        response.headers["Content-Type"] = "application/json"
        return options_to_json(options)

    def _register_complete(self):
        if not self.auth.current_user: raise HTTP(401)
        credential = request.json
        challenge_b64 = self.session.get("webauthn_challenge")
        if not challenge_b64: raise HTTP(400)
        challenge = urlsafe_b64_to_bytes(challenge_b64)
        
        key_name = credential.pop("name", "No name key")
        # HIGHLIGHT 2: Si el nombre viene vacío o solo con espacios, usamos un valor por defecto.
        if not key_name or not key_name.strip():
            key_name = "No name key"

        try:
            verification = verify_registration_response(credential=credential, expected_challenge=challenge, expected_origin=self.origin, expected_rp_id=self.rp_id)
            self.db.webauthn_credentials.insert(user_id=self.auth.current_user["id"], name=key_name, credential_id=verification.credential_id.hex(), public_key=verification.credential_public_key.hex(), sign_count=verification.sign_count)
            return {"verified": True}
        except Exception as e:
            log.error(f"Error en registro WebAuthn: {e}"); raise HTTP(400, f"Error en la verificación: {e}")
            

    def _login_begin(self):
        email = request.json.get("email")
        if not email: raise HTTP(400, "Please enter your email.")
        #make a filter to check if the email is valid, find  chars like '",:  and others that are not allowed in an email
        # HIGHLIGHT 1: Validación del email usando IS_EMAIL de pydal
        #print(IS_EMAIL()(email))
        if IS_EMAIL()(email)[1] is not None: raise HTTP(400, "Invalid email format.")
        if contains_dangerous_chars(email, ['"', "'", ':', ';', '<', '>', '\\', '/', '|', '?', '*']): 
            raise HTTP(400, "Email contains invalid characters.")
        user = self.db(self.db.auth_user.email == email).select().first()
        if user is None: raise HTTP(200, "Invalid authentication method for user.")
        #if not user:
            # options = generate_authentication_options(rp_id=self.rp_id)
            # response.headers["Content-Type"] = "application/json"
            # return options_to_json(options)
        creds = self.db(self.db.webauthn_credentials.user_id == user.id).select()
        if not creds: raise HTTP(404, "Invaid authentication method")
        allow_credentials = [PublicKeyCredentialDescriptor(id=bytes.fromhex(c.credential_id)) for c in creds]
        options = generate_authentication_options(rp_id=self.rp_id, allow_credentials=allow_credentials)
        self.session["webauthn_challenge"] = bytes_to_urlsafe_b64(options.challenge)
        self.session["webauthn_user_id"] = user.id
        response.headers["Content-Type"] = "application/json"
        return options_to_json(options)
        
    def _login_complete(self):
        credential = request.json
        challenge_b64 = self.session.get("webauthn_challenge")
        user_id = self.session.get("webauthn_user_id")
        if not all([credential, challenge_b64, user_id]): raise HTTP(400)
        challenge = urlsafe_b64_to_bytes(challenge_b64)
        cred_id_from_client_bytes = base64url_to_bytes(credential["id"])
        cred_in_db = self.db((self.db.webauthn_credentials.user_id == user_id) & (self.db.webauthn_credentials.credential_id == cred_id_from_client_bytes.hex())).select().first()
        if not cred_in_db: raise HTTP(404)
        try:
            public_key_bytes = bytes.fromhex(cred_in_db.public_key)
            verification = verify_authentication_response(credential=credential, expected_challenge=challenge, expected_origin=self.origin, expected_rp_id=self.rp_id, credential_public_key=public_key_bytes, credential_current_sign_count=cred_in_db.sign_count)
            cred_in_db.update_record(sign_count=verification.new_sign_count)
            user = self.db.auth_user(user_id)
            self.session["user"] = user.as_dict()
            del self.session["webauthn_challenge"]
            del self.session["webauthn_user_id"]
            return {"verified": True, "redirect_url": URL("index")}
        except Exception as e:
            log.error(f"Error en login WebAuthn: {e}"); raise HTTP(403, f"Invalid authentication response")