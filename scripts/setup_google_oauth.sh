#!/usr/bin/env bash
#
# setup_google_oauth.sh
#
# Automates the creation of Google OAuth 2.0 credentials for py4web Google SSO.
#
# Prerequisites:
#   - gcloud CLI installed and authenticated (run: gcloud auth login)
#   - A Google Cloud billing account (required to enable APIs)
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
        curl -sf -X "$method" "$url" \
            -H "Authorization: Bearer $token" \
            -H "Content-Type: application/json" \
            -d "$body"
    else
        curl -sf -X "$method" "$url" \
            -H "Authorization: Bearer $token"
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

# ---------- step 2: enable required APIs ----------
info "Enabling required APIs (this may take a moment)..."
gcloud services enable \
    iap.googleapis.com \
    people.googleapis.com \
    oauth2.googleapis.com \
    --quiet 2>/dev/null || {
    warn "Some APIs may require billing. Checking..."
    # Try enabling one at a time for clearer errors
    for api in iap.googleapis.com people.googleapis.com; do
        if ! gcloud services enable "$api" --quiet 2>/dev/null; then
            warn "Could not enable $api — billing may be required."
            echo "  Enable billing: https://console.cloud.google.com/billing/linkedaccount?project=$PROJECT_ID"
            echo "  Then re-run this script with: --project-id $PROJECT_ID"
            fail "Billing required to enable APIs."
        fi
    done
}
ok "APIs enabled."

# ---------- step 3: create OAuth consent screen (brand) ----------
info "Configuring OAuth consent screen..."

# Check if brand already exists
EXISTING_BRAND=$(gcp_api GET \
    "https://iap.googleapis.com/v1/projects/$PROJECT_NUMBER/brands" \
    | jq -r '.brands[0].name // empty' 2>/dev/null) || true

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

    BRAND_NAME=$(echo "$BRAND_RESP" | jq -r '.name // empty')
    if [[ -z "$BRAND_NAME" ]]; then
        warn "Could not create brand via API. Response:"
        echo "$BRAND_RESP"
        fail "OAuth consent screen creation failed."
    fi
    ok "OAuth consent screen created."
fi

# ---------- step 4: create OAuth client ----------
info "Creating OAuth 2.0 client credentials..."

CLIENT_BODY=$(jq -n --arg name "py4web SSO Client" '{displayName: $name}')

CLIENT_RESP=$(gcp_api POST \
    "https://iap.googleapis.com/v1/${BRAND_NAME}/identityAwareProxyClients" \
    "$CLIENT_BODY")

CLIENT_ID=$(echo "$CLIENT_RESP" | jq -r '.name // empty' | awk -F/ '{print $NF}')
CLIENT_SECRET=$(echo "$CLIENT_RESP" | jq -r '.secret // empty')

if [[ -z "$CLIENT_ID" || -z "$CLIENT_SECRET" ]]; then
    warn "IAP client creation response:"
    echo "$CLIENT_RESP"
    fail "Could not create OAuth client credentials."
fi

ok "OAuth client created."

# ---------- step 5: configure redirect URIs ----------
# The IAP API creates clients but redirect URIs must be set via the Cloud Console
# or the OAuth2 config API. We'll try the newer endpoint.

# Determine the redirect URI
if [[ "$HOST" == localhost* || "$HOST" == 127.0.0.1* ]]; then
    SCHEME="http"
else
    SCHEME="https"
fi
REDIRECT_URI="${SCHEME}://${HOST}/${APP_NAME}/auth/plugin/oauth2google/callback"
SCOPED_REDIRECT_URI="${SCHEME}://${HOST}/${APP_NAME}/auth/plugin/oauth2googlescoped/callback"

info "Configuring redirect URIs..."

# Try to set redirect URIs via the Cloud Console REST API
OAUTH_CLIENT_FULL_ID="projects/$PROJECT_NUMBER/brands/$PROJECT_NUMBER/identityAwareProxyClients/$CLIENT_ID"

# The redirect URI configuration often requires manual steps.
# We'll attempt to use the newer Google Auth Platform API if available.
REDIRECT_SET=false

# Try the googleapis.com credentials API
CRED_BODY=$(jq -n \
    --arg redirect "$REDIRECT_URI" \
    --arg scoped_redirect "$SCOPED_REDIRECT_URI" \
    --arg origin "${SCHEME}://${HOST}" \
    '{
        web: {
            redirect_uris: [$redirect, $scoped_redirect],
            javascript_origins: [$origin]
        }
    }')

# This endpoint may not be publicly available; we try and fall back gracefully
if gcp_api PUT \
    "https://oauth2.googleapis.com/v1/projects/$PROJECT_NUMBER/oauthClients/$CLIENT_ID" \
    "$CRED_BODY" &>/dev/null; then
    REDIRECT_SET=true
    ok "Redirect URIs configured automatically."
fi

# ---------- step 6: output results ----------
echo ""
echo "=============================================="
echo "  Google OAuth Credentials for py4web"
echo "=============================================="
echo ""
echo "  Client ID:     $CLIENT_ID"
echo "  Client Secret:  $CLIENT_SECRET"
echo ""
echo "  Redirect URI:   $REDIRECT_URI"
if $SCOPED; then
    echo "  Scoped Redirect: $SCOPED_REDIRECT_URI"
fi
echo ""

if ! $REDIRECT_SET; then
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
    warn "You selected EXTERNAL user type."
    echo "  Add test users at: https://console.cloud.google.com/apis/credentials/consent?project=$PROJECT_ID"
    echo "  Until the app is verified, only test users can log in."
    echo ""
fi

# ---------- step 7: write py4web settings ----------
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
    # Write the scoped credentials JSON file
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

    echo "  Add to apps/${APP_NAME}/settings.py:"
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
