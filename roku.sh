import requests
from requests.auth import HTTPDigestAuth
import os
import zipfile

# CONFIGURATION
ROKU_IP = "192.168.1.XX"  # Change to your Roku's IP
DEV_PASSWORD = "YOUR_PASSWORD"  # The password you set in Developer Mode
APP_ZIP = "frost_channel.zip"

def create_bundle():
    """Zips the FrostOS files for deployment."""
    with zipfile.ZipFile(APP_ZIP, 'w') as zipf:
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith(('.brs', '.xml', 'manifest')):
                    zipf.write(os.path.join(root, file))
    print("Bundle 'frost_channel.zip' created.")

def push_to_roku():
    """Pushes the zip to the Roku Developer web portal."""
    url = f"http://{ROKU_IP}/plugin_install"
    auth = HTTPDigestAuth('rokudev', DEV_PASSWORD)
    
    files = {'mysubmit': 'Install', 'archive': open(APP_ZIP, 'rb')}
    
    print(f"Pushing FrostOS to {ROKU_IP}...")
    response = requests.post(url, auth=auth, files=files)
    
    if response.status_code == 200:
        print("Success! Frost Channel is now live.")
    else:
        print(f"Failed to push. Status: {response.status_code}")

def remote_restart():
    """Sends the secret reboot sequence via WAN/LAN."""
    print("Restarting Roku to apply Frost Skin...")
    base_url = f"http://{ROKU_IP}:8060/keypress/"
    sequence = ["Home"]*5 + ["Up", "Rev", "Rev", "Fwd", "Fwd"]
    for key in sequence:
        requests.post(base_url + key)
    print("Restart sequence complete.")

if __name__ == "__main__":
    create_bundle()
    push_to_roku()
    remote_restart()
