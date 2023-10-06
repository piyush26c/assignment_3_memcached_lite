import subprocess
import sys
import os
import venv
import os
import subprocess
import sys


# Check if Python 3.8.10 or greater is installed
required_version = "3.8.10"
current_version = sys.version.split()[0]

if current_version < required_version:
    print(f"Python version {current_version} is not compatible. Installing Python {required_version}...")
    subprocess.run(["sudo", "apt-get", "install", f"python{required_version}"])

# Command 1: Switch to root user
subprocess.run(["sudo", "-s"], check=True)

# Command 2: Update the package list
subprocess.run(["apt-get", "update"], check=True)

# Command 3: Install pip
subprocess.run(["apt-get", "install", "python3-pip"], check=True)

# Command 4: Exit from root user shell
subprocess.run(["exit"], check=True)

# Install requirements from requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt", "-v"])


print("Virtual environment activated. Installation complete.")
