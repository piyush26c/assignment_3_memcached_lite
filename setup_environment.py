import subprocess
import sys
import os
import venv
# Check if Python 3.8.10 or greater is installed
required_version = "3.8.10"
current_version = sys.version.split()[0]

if current_version < required_version:
    print(f"Python version {current_version} is not compatible. Installing Python {required_version}...")
    subprocess.run(["sudo", "apt-get", "install", f"python{required_version}"])


# Install requirements from requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt", "-v"])


print("Virtual environment activated. Installation complete.")
