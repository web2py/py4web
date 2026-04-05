#!/usr/bin/env bash
#
# setup_google_oauth.sh
#
# Automates the creation of Google OAuth 2.0 credentials for py4web Google SSO.
# Works for both organization and personal Google accounts.
#
# Prerequisites:
#   - gcloud CLI installed and authenticated (run: gcloud auth login)
#   - A Google Cloud billing account (may be required to enable APIs)
#
# Usage:
#   ./scripts/setup_google_oauth.sh [OPTIONS]
#
# Options:
#   --project-id ID        GCP project ID (default: auto-generated)
#   --project-name NAME    GCP project display name (default: "py4web OAuth")
#   --app-name NAME        py4web app name (default: "_scaffold")
#   --host HOST            App host for redirect URIs (default: "localhost:8000")
#   --support-email EMAIL  OAuth consent screen email (default: gcloud account email)
#   --external             Set consent screen to external (default: internal)
#   --scoped               Also output config for OAuth2GoogleScoped
#   --help                 Show this help
#
set -euo pipefail

# ---------- defaults ----------
PROJECT_ID=""
PROJECT_NAME="py4web OAuth"
APP_NAME="_scaffold"
HOST="localhost:8000"
SUPPORT_EMAIL=""
USER_TYPE="INTERNAL"
SCOPED=false

# ---------- parse args ----------
while [[ $# -gt 0 ]]; do
    case $1 in
        --project-id)    PROJECT_ID="$2"; shift 2 ;;
        --project-name)  PROJECT_NAME="$2"; shift 2 ;;
        --app-name)      APP_NAME="$2"; shift 2 ;;
        --host)          HOST="$2"; shift 2 ;;
        --support-email) SUPPORT_EMAIL="$2"; shift 2 ;;
        --external)      USER_TYPE="EXTERNAL"; shift ;;
        --scoped)        SCOPED=true; shift ;;
        --help)
            sed -n '3,/^set /p' "$0" | head -n -1
            exit 0
            ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

# ---------- helpers ----------
info()  { echo -e "\033[1;34m==>\033[0m $*"; }
ok()    { echo -e "\033[1;32m==>\033[0m $*"; }
warn()  { echo -e "\033[1;33m==>\033[0m $*"; }
fail()  { echo -e "\033[1;31mERROR:\033[0m $*" >&2; exit 1; }

require_cmd() {
    command -v "$1" >/dev/null 2>&1 || fail "'$1' is required but not installed."
}

gcp_api() {
    # $1 = method, $2 = url, $3 = optional JSON body
    local method="$1" url="$2" body="${3:-}"
    local token
    token=$(gcloud auth print-access-token 2>/dev/null) || fail "Not authenticated. Run: gcloud auth login"
    if [[ -n "$body" ]]; then
        curl -s --connect-timeout 10 --max-time 30 -X "$method" "$url" \
            -H "Authorization: Bearer $token" \
            -H "Content-Type: application/json" \
            -d "$body"
    else
        curl -s --connect-timeout 10 --max-time 30 -X "$method" "$url" \
            -H "Authorization: Bearer $token"
    fi
}

open_url() {
    local url="$1"
    if command -v xdg-open &>/dev/null; then
        xdg-open "$url" 2>/dev/null || true
    elif command -v open &>/dev/null; then
        open "$url" 2>/dev/null || true
    else
        echo "  Open in your browser: $url"
    fi
}

# ---------- preflight ----------
require_cmd gcloud
require_cmd curl
require_cmd jq

# Verify gcloud is authenticated
info "Checking gcloud authentication..."
ACCOUNT=$(gcloud config get-value account 2>/dev/null) || true
if [[ -z "$ACCOUNT" || "$ACCOUNT" == "(unset)" ]]; then
    fail "Not authenticated. Run: gcloud auth login"
fi
ok "Authenticated as $ACCOUNT"

if [[ -z "$SUPPORT_EMAIL" ]]; then
    SUPPORT_EMAIL="$ACCOUNT"
fi

# ---------- step 1: create or select project ----------
if [[ -z "$PROJECT_ID" ]]; then
    PROJECT_ID="py4web-oauth-$(date +%s | tail -c 7)"
fi

info "Checking if project '$PROJECT_ID' exists..."
if gcloud projects describe "$PROJECT_ID" &>/dev/null; then
    ok "Project '$PROJECT_ID' already exists, using it."
else
    info "Creating project '$PROJECT_ID'..."
    gcloud projects create "$PROJECT_ID" --name="$PROJECT_NAME" --quiet
    ok "Project created."
fi

gcloud config set project "$PROJECT_ID" --quiet

# Get project number (needed for REST APIs)
PROJECT_NUMBER=$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')
info "Project number: $PROJECT_NUMBER"

# Check if project belongs to an organization
ORG_ID=$(gcloud projects describe "$PROJECT_ID" --format='value(parent.id)' 2>/dev/null) || true
PARENT_TYPE=$(gcloud projects describe "$PROJECT_ID" --format='value(parent.type)' 2>/dev/null) || true
HAS_ORG=false
if [[ "$PARENT_TYPE" == "organization" && -n "$ORG_ID" ]]; then
    HAS_ORG=true
    info "Project belongs to organization: $ORG_ID"
else
    info "Project is a personal project (no organization)."
fi

# ---------- step 2: enable required APIs ----------
info "Enabling required APIs (this may take a moment)..."

REQUIRED_APIS=(people.googleapis.com)
if $HAS_ORG; then
    REQUIRED_APIS+=(iap.googleapis.com)
fi

for api in "${REQUIRED_APIS[@]}"; do
    if ! gcloud services enable "$api" --quiet 2>/dev/null; then
        warn "Could not enable $api — billing may be required."
        echo "  Enable billing: https://console.cloud.google.com/billing/linkedaccount?project=$PROJECT_ID"
        echo "  Then re-run this script with: --project-id $PROJECT_ID"
        fail "Billing required to enable APIs."
    fi
done
ok "APIs enabled."

# ---------- compute redirect URIs ----------
if [[ "$HOST" == localhost* || "$HOST" == 127.0.0.1* ]]; then
    SCHEME="http"
else
    SCHEME="https"
fi
REDIRECT_URI="${SCHEME}://${HOST}/${APP_NAME}/auth/plugin/oauth2google/callback"
SCOPED_REDIRECT_URI="${SCHEME}://${HOST}/${APP_NAME}/auth/plugin/oauth2googlescoped/callback"

# ==========================================================================
#  Two paths: organization projects use the IAP API (fully automated),
#  personal projects use interactive browser-assisted flow.
# ==========================================================================

if $HAS_ORG; then
    # ---- ORGANIZATION PATH: fully automated via IAP API ----

    # step 3: create OAuth consent screen (brand)
    info "Configuring OAuth consent screen via IAP API..."

    BRAND_LIST_RESP=$(gcp_api GET \
        "https://iap.googleapis.com/v1/projects/$PROJECT_NUMBER/brands") || true

    if [[ -z "$BRAND_LIST_RESP" ]]; then
        fail "Cannot query OAuth brands. Check that iap.googleapis.com is enabled and you have Owner/Editor role."
    fi

    EXISTING_BRAND=$(echo "$BRAND_LIST_RESP" | jq -r '.brands[0].name // empty' 2>/dev/null) || true

    if [[ -n "$EXISTING_BRAND" ]]; then
        ok "OAuth consent screen already configured."
        BRAND_NAME="$EXISTING_BRAND"
    else
        BRAND_BODY=$(jq -n \
            --arg title "$PROJECT_NAME" \
            --arg email "$SUPPORT_EMAIL" \
            '{applicationTitle: $title, supportEmail: $email}')

        BRAND_RESP=$(gcp_api POST \
            "https://iap.googleapis.com/v1/projects/$PROJECT_NUMBER/brands" \
            "$BRAND_BODY")

        if [[ -z "$BRAND_RESP" ]]; then
            fail "OAuth consent screen creation failed (empty response)."
        fi

        BRAND_NAME=$(echo "$BRAND_RESP" | jq -r '.name // empty')
        if [[ -z "$BRAND_NAME" ]]; then
            warn "Response: $BRAND_RESP"
            fail "OAuth consent screen creation failed."
        fi
        ok "OAuth consent screen created."
    fi

    # step 4: create OAuth client
    info "Creating OAuth 2.0 client credentials..."

    CLIENT_BODY=$(jq -n --arg name "py4web SSO Client" '{displayName: $name}')

    CLIENT_RESP=$(gcp_api POST \
        "https://iap.googleapis.com/v1/${BRAND_NAME}/identityAwareProxyClients" \
        "$CLIENT_BODY")

    CLIENT_ID=$(echo "$CLIENT_RESP" | jq -r '.name // empty' | awk -F/ '{print $NF}')
    CLIENT_SECRET=$(echo "$CLIENT_RESP" | jq -r '.secret // empty')

    if [[ -z "$CLIENT_ID" || -z "$CLIENT_SECRET" ]]; then
        warn "Response: $CLIENT_RESP"
        fail "Could not create OAuth client credentials."
    fi

    ok "OAuth client created via IAP API."

    # Try to set redirect URIs (may not work via public API)
    REDIRECT_SET=false
    info "Attempting to configure redirect URIs..."
    # The IAP-created clients need redirect URIs set via Console
    warn "Redirect URIs must be configured in the Cloud Console (see instructions below)."

else
    # ---- PERSONAL ACCOUNT PATH: browser-assisted ----

    info "Personal account detected. Using browser-assisted setup."
    echo ""

    # step 3: consent screen — must be done in browser
    CONSENT_URL="https://console.cloud.google.com/apis/credentials/consent?project=$PROJECT_ID"
    echo "  Step 1: Configure the OAuth consent screen"
    echo ""
    echo "  Opening the OAuth consent screen configuration page..."
    echo "  If it doesn't open automatically, visit:"
    echo "    $CONSENT_URL"
    echo ""
    echo "  In the consent screen form:"
    echo "    - User Type: External (select and click Create)"
    echo "    - App name: $PROJECT_NAME"
    echo "    - User support email: $SUPPORT_EMAIL"
    echo "    - Developer contact email: $SUPPORT_EMAIL"
    echo "    - Click 'Save and Continue' through Scopes and Test Users"
    echo ""
    open_url "$CONSENT_URL"

    read -rp "  Press Enter once you've saved the consent screen... "
    echo ""

    # step 4: create credentials — must be done in browser
    # Pre-fill as much as possible via URL parameters
    CRED_URL="https://console.cloud.google.com/apis/credentials/oauthclient?project=$PROJECT_ID"
    echo "  Step 2: Create OAuth 2.0 Client ID"
    echo ""
    echo "  Opening the credential creation page..."
    echo "  If it doesn't open automatically, visit:"
    echo "    $CRED_URL"
    echo ""
    echo "  In the form:"
    echo "    - Application type: Web application"
    echo "    - Name: py4web SSO Client"
    echo "    - Authorized JavaScript origins: ${SCHEME}://${HOST}"
    echo "    - Authorized redirect URIs:"
    echo "        $REDIRECT_URI"
    if $SCOPED; then
        echo "        $SCOPED_REDIRECT_URI"
    fi
    echo "    - Click Create"
    echo ""
    echo "  After creation, Google will show the Client ID and Secret."
    echo ""
    open_url "$CRED_URL"

    read -rp "  Paste Client ID: " CLIENT_ID
    read -rp "  Paste Client Secret: " CLIENT_SECRET

    if [[ -z "$CLIENT_ID" || -z "$CLIENT_SECRET" ]]; then
        fail "Client ID and Secret are required."
    fi

    ok "Credentials received."
    REDIRECT_SET=true   # User configured redirect URIs manually
fi

# ---------- output results ----------
echo ""
echo "=============================================="
echo "  Google OAuth Credentials for py4web"
echo "=============================================="
echo ""
echo "  Client ID:      $CLIENT_ID"
echo "  Client Secret:  $CLIENT_SECRET"
echo ""
echo "  Redirect URI:   $REDIRECT_URI"
if $SCOPED; then
    echo "  Scoped Redirect: $SCOPED_REDIRECT_URI"
fi
echo ""

if [[ "${REDIRECT_SET:-false}" != "true" ]]; then
    warn "Redirect URIs must be configured manually:"
    echo "  1. Go to: https://console.cloud.google.com/apis/credentials?project=$PROJECT_ID"
    echo "  2. Click on the OAuth 2.0 Client ID just created"
    echo "  3. Under 'Authorized redirect URIs', add:"
    echo "       $REDIRECT_URI"
    if $SCOPED; then
        echo "       $SCOPED_REDIRECT_URI"
    fi
    echo "  4. Under 'Authorized JavaScript origins', add:"
    echo "       ${SCHEME}://${HOST}"
    echo "  5. Click Save"
    echo ""
fi

if [[ "$USER_TYPE" == "EXTERNAL" ]]; then
    warn "External consent screen: until the app is verified, only test users can log in."
    echo "  Add test users at: https://console.cloud.google.com/apis/credentials/consent?project=$PROJECT_ID"
    echo ""
fi

# ---------- write py4web settings ----------
echo "----------------------------------------------"
echo "  py4web Configuration"
echo "----------------------------------------------"
echo ""
echo "  Add to apps/${APP_NAME}/settings.py:"
echo ""
echo "    OAUTH2GOOGLE_CLIENT_ID = \"$CLIENT_ID\""
echo "    OAUTH2GOOGLE_CLIENT_SECRET = \"$CLIENT_SECRET\""
echo ""

if $SCOPED; then
    SECRETS_FILE="apps/${APP_NAME}/private/google_client_secrets.json"
    SECRETS_DIR="$(dirname "$SECRETS_FILE")"

    echo "  For OAuth2GoogleScoped, a secrets file will be written to:"
    echo "    $SECRETS_FILE"
    echo ""

    mkdir -p "$SECRETS_DIR"

    jq -n \
        --arg client_id "$CLIENT_ID" \
        --arg client_secret "$CLIENT_SECRET" \
        --arg redirect "$SCOPED_REDIRECT_URI" \
        --arg project_id "$PROJECT_ID" \
        '{
            web: {
                client_id: $client_id,
                client_secret: $client_secret,
                project_id: $project_id,
                auth_uri: "https://accounts.google.com/o/oauth2/auth",
                token_uri: "https://oauth2.googleapis.com/token",
                auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
                redirect_uris: [$redirect]
            }
        }' > "$SECRETS_FILE"

    echo "  Also add to apps/${APP_NAME}/settings.py:"
    echo ""
    echo "    OAUTH2GOOGLE_SCOPED_CREDENTIALS_FILE = \"private/google_client_secrets.json\""
    echo ""
fi

echo "----------------------------------------------"
echo ""
ok "Done! Your Google OAuth credentials are ready."
echo ""
echo "  Console: https://console.cloud.google.com/apis/credentials?project=$PROJECT_ID"
echo ""
