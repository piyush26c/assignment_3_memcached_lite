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

import os
import subprocess
import sys

# Check if pip is already installed
try:
    import pip
    print("pip is already installed.")
except ImportError:
    # Install pip
    print("pip is not installed. Installing pip...")
    try:
        subprocess.check_call([sys.executable, '-m', 'ensurepip', '--default-pip'])
        print("pip has been successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install pip: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Install requirements from requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt", "-v"])


print("Virtual environment activated. Installation complete.")
