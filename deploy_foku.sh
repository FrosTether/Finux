import requests
from requests.auth import HTTPDigestAuth
import zipfile
import os

# --- SETTINGS ---
ROKU_IP = "192.168.1.XX"  # Enter your Roku IP here
PASSWORD = "YOUR_DEV_PASSWORD"

def push_frost():
    # 1. Create the Channel Package
    with zipfile.ZipFile('frost.zip', 'w') as z:
        z.write('manifest')
        for root, _, files in os.walk('components'):
            for f in files: z.write(os.path.join(root, f))
        for root, _, files in os.walk('source'):
            for f in files: z.write(os.path.join(root, f))

    # 2. Push to Roku
    url = f"http://{ROKU_IP}/plugin_install"
    auth = HTTPDigestAuth('rokudev', PASSWORD)
    files = {'mysubmit': 'Install', 'archive': open('frost.zip', 'rb')}
    
    print(f"Pushing FrostOS Skin to {ROKU_IP}...")
    requests.post(url, auth=auth, files=files)

    # 3. Remote Restart via WAN/LAN Sequence
    print("Sending Restart Sequence...")
    ecp_url = f"http://{ROKU_IP}:8060/keypress/"
    for key in ["Home"]*5 + ["Up", "Rev", "Rev", "Fwd", "Fwd"]:
        requests.post(ecp_url + key)
    print("Frost Channel Deployed & System Rebooting.")

if __name__ == "__main__":
    push_frost()
