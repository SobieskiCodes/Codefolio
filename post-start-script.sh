#!/bin/bash
RUN pwd && \
    dirname $(pwd) && \
    dirname $(dirname $(pwd)) && \
    dirname $(dirname $(dirname $(pwd)))
RUN echo "hello world" 
# Define the location of the .env file
#ENV_FILE="../workspaces/.codespaces/shared/.env"
#ENV_FILE="../../.codespaces/shared/.env"

# List parent directories up to 3 levels
# PARENT_DIR=$(dirname "$ENV_FILE")
# for i in {1..3}; do
#   echo "Listing contents of $PARENT_DIR:"
#   if [ -d "$PARENT_DIR" ]; then
#     ls -l "$PARENT_DIR"
#   else
#     echo "Directory $PARENT_DIR does not exist."
#   fi
#   PARENT_DIR=$(dirname "$PARENT_DIR")
# done

# # Attempt to find the .env file up to 10 times
# for i in {1..10}
# do
#     echo "Iteration: $i"

#     # Check if the .env file is present
#     if [ -f "$ENV_FILE" ]; then
#       echo ".env file found."
#       break # Exit the loop if found
#     else
#       echo "Waiting for .env file to be available..."
#       sleep 5
#     fi
# done

# # Check if the .env file exists before sourcing
# if [ -f "$ENV_FILE" ]; then
#     echo "Sourcing .env file..."
#     set -a  # Automatically export all variables
#     source "$ENV_FILE"
#     set +a
# else
#     echo "The .env file was not found after 10 iterations."
#     exit 1 # Exit the script with an error
# fi

# Continue with the execution
exec "$@"