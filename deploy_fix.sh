import requests
from requests.auth import HTTPDigestAuth
import os
import zipfile
import time

# YOUR SPECIFIC CREDENTIALS
ROKU_IP = "192.168.0.2"
USER = "rokudev"
PASS = "7444"

def deploy_frost_os():
    # 1. Zip the channel files
    zip_name = 'frost_os.zip'
    with zipfile.ZipFile(zip_name, 'w') as z:
        # Assumes your files are in these folders
        for folder in ['source', 'components', 'images']:
            if os.path.exists(folder):
                for root, _, files in os.walk(folder):
                    for f in files:
                        z.write(os.path.join(root, f))
        if os.path.exists('manifest'):
            z.write('manifest')

    # 2. Push to Roku (The "Install")
    print(f"Pushing FrostOS to {ROKU_IP}...")
    url = f"http://{ROKU_IP}/plugin_install"
    auth = HTTPDigestAuth(USER, PASS)
    
    try:
        with open(zip_name, 'rb') as f:
            files = {'mysubmit': 'Install', 'archive': f}
            response = requests.post(url, auth=auth, files=files, timeout=10)
        
        if response.status_code == 200:
            print("Successfully deployed FrostOS Skin!")
            # 3. Trigger the Restart on WAN/LAN
            restart_sequence()
        else:
            print(f"Deployment failed. Status code: {response.status_code}")
    except Exception as e:
        print(f"Connection error: {e}")

def restart_sequence():
    print("Initiating Remote Restart...")
    ecp_url = f"http://{ROKU_IP}:8060/keypress/"
    # Secret Reboot Code: Home(5x), Up(1x), Rev(2x), Fwd(2x)
    keys = ["Home"]*5 + ["Up", "Rev", "Rev", "Fwd", "Fwd"]
    for key in keys:
        requests.post(ecp_url + key)
        time.sleep(0.4)
    print("Restart sequence sent. Your Roku should be rebooting now.")

if __name__ == "__main__":
    deploy_frost_os()
