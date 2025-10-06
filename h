import subprocess
import sys

# Automatically install requests if it's missing
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
print("requests installed successfully!")