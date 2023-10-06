#!/bin/bash

# Check if Python 3.8.10 or greater is installed
required_version="3.8.10"
current_version=$(python3 -c "import sys; print(sys.version.split()[0])")

if [ "$(printf '%s\n' "$required_version" "$current_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "Python version $current_version is not compatible. Installing Python $required_version..."
    sudo apt-get install "python$required_version"
fi

# Command 1: Switch to root user
# sudo -s

# Command 2: Update the package list
apt-get update

# Command 3: Install pip
apt-get install python3-pip

# Command 4: Exit from root user shell
# exit 

# Install requirements from requirements.txt
pip install -r requirements.txt -v
