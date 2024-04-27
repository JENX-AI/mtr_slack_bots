#!/bin/bash

######################################################
# install.sh
######################################################

# This shell script installs the Astral uv package manager
# then iterates through each subdirectory to create
# a virtual environment and install dependencies

# If this process is unsuccessful, run this command
# in the same directory as this file ('install.sh'):
# 'chmod +x install.sh'

######################################################

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# Pin uv to PATH
source $HOME/.cargo/env

# Loop through each directory in slack_bots
for dir in slack_bots/*; do
  # Confirm it's a directory (avoid hidden files etc.)
  if [ -d "$dir" ]; then
    # Change into directory and create venv using uv
    cd "$dir"
    uv venv
    echo "Virtual environment created in: $dir"
    # Activate venv
    source .venv/bin/activate
    echo "Virtual environment activated in: $dir"
    # Install dependencies
    uv pip install -r requirements.txt
    echo "Installing..."
    # Wait while packages install
    sleep 5
    # Deactivate venv
    deactivate
    echo "Virtual environment deactivated"
    # Move back one directory level
    cd -
  fi
done

echo "Installation complete!"
