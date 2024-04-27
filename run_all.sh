#!/bin/bash

######################################################
# run_all.sh
######################################################

# This shell script iterates through each subdirectory
# and runs the individual 'run.sh' shell scripts

# If this process is unsuccessful, run this command
# in the same directory as this file ('run_all.sh'):
# 'chmod +x run_all.sh'

######################################################

# Loop through each directory in slack_bots
for dir in slack_bots/*; do
  # Confirm it's a directory (avoid hidden files etc.)
  if [ -d "$dir" ]; then
    # Change into directory and create venv using uv
    cd "$dir"
    # Set execute permissions for run.sh
    chmod +x run.sh
    # Execute script in separate terminal
    nohup ./run.sh > /dev/null 2>&1 &
    echo "Running $dir..."
    # Move back one directory level
    cd -
  fi
done

echo "Complete!"
