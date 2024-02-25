#!/bin/bash
set -x
# Get the current working directory of the script.
CWD="$(dirname "$0")"

# Attempt to source configuration from Codespaces path, adjusting for an additional directory level.
if [ -f "$CWD/../../workspaces/.codespaces/shared/.env" ]; then
    . "$CWD/../../workspaces/.codespaces/shared/.env"
elif [ -f "$CWD/.env.local" ]; then
    # Fallback to a local .env file if Codespaces config doesn't exist.
    # Adjust this path if your .env.local is expected to be at the root or elsewhere relative to the service.
    . "$CWD/.env.local"
else
    # Default values if no .env file is found.
    CODESPACE_NAME="default_codespace"
    GITHUB_REPOSITORY="default/repository"
fi

# Extract WORKSPACE_NAME from GITHUB_REPOSITORY.
WORKSPACE_NAME=$(echo "$GITHUB_REPOSITORY" | sed 's|.*/||')

# Create or update .env file with dynamic or default values.
# Ensure this writes to the correct location based on your setup.
cat <<EOF > "$CWD/.env"
CODESPACE_NAME=$CODESPACE_NAME
VITE_CODESPACE_NAME=$CODESPACE_NAME
WORKSPACE_NAME=$WORKSPACE_NAME
EOF

# Output the .env content for verification.
echo "Generated .env file with the following content in $CWD:"
cat "$CWD/.env"

# Continue with the container's main command.
exec "$@"