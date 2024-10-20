#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Get the project root directory (one level up from the script directory)
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"

# Parse YAML file
SETTINGS_FILE="$PROJECT_ROOT/config/settings.yaml"
BLENDER_PATH=$(grep "blender_executable:" "$SETTINGS_FILE" | cut -d '"' -f 2)

# Check if Blender path is found
if [ -z "$BLENDER_PATH" ]; then
    echo "Error: Blender executable path not found in $SETTINGS_FILE"
    exit 1
fi

# Run Blender with the provided script
# "$BLENDER_PATH" -E help
"$BLENDER_PATH" -b -P "$1"
