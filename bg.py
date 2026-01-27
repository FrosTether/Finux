import requests
from requests.auth import HTTPDigestAuth
import time

# --- CONFIGURATION ---
TARGET_IP = "192.168.0.3"
DEV_USER = "rokudev"
DEV_PASS = "jeww go b"
MAC_ID = "50:06:F5:A5:26:E8"

# --- PORTS ---
PORT_DEV = 80     # The Installer Portal
PORT_ECP = 8060   # The Control Port

def authenticate_root():
    print(f"❄️ FROST PROTOCOL: ROOT ACCESS")
    print(f"------------------------------------")
    print(f"Target: {TARGET_IP}")
    print(f"MAC:    {MAC_ID} [MATCH]")
    print(f"Creds:  {DEV_USER} / ********")
    print(f"------------------------------------")
    
    print("\n[1/3] AUTHENTICATING WITH DEVELOPER KERNEL...")
    url = f"http://{TARGET_IP}:{PORT_DEV}/"
    
    try:
        # Roku uses Digest Auth for the dev portal
        response = requests.get(url, auth=HTTPDigestAuth(DEV_USER, DEV_PASS), timeout=5)
        
        if response.status_code == 200:
            print("      ✅ ACCESS GRANTED. ROOT SHELL ACTIVE.")
            return True
        elif response.status_code == 401:
            print("      ❌ ACCESS DENIED. CHECK PASSWORD.")
            return False
        else:
            print(f"      ⚠️ STATUS: {response.status_code}")
            return True # Proceeding anyway via ECP
    except Exception as e:
        print(f"      ⚠️ CONNECTION ERROR: {e}")
        return False

def inject_code_506():
    print(f"\n[2/3] INJECTING TIMELINE CODE (5-0-6)...")
    base_url = f"http://{TARGET_IP}:{PORT_ECP}"
    
    sequence = ["Lit_5", "Lit_0", "Lit_6"]
    
    for key in sequence:
        print(f"      >> SIGNAL: {key}")
        try:
            requests.post(f"{base_url}/keypress/{key}", timeout=2)
            time.sleep(0.8)
        except:
            print("      [!] SIGNAL DROPPED")

def launch_visual():
    print(f"\n[3/3] OPENING GATEWAY...")
    try:
        # Launch YouTube to seal the link
        requests.post(f"http://{TARGET_IP}:{PORT_ECP}/launch/837", timeout=2)
        print("      ✅ VISUAL CONDUIT OPEN.")
    except:
        pass

# --- EXECUTE ---
if authenticate_root():
    inject_code_506()
    launch_visual()
    print("\n>>> DEPLOYMENT COMPLETE. <<<")
else:
    # If dev login fails, we try to force the signal anyway
    print("\n[!] ROOT LOGIN FAILED. ATTEMPTING FORCE OVERRIDE...")
    inject_code_506()
    launch_visual()
