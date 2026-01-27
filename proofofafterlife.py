# 1. Overwrite main.py with the Force Protocol
cat <<EOF > main.py
import requests
from requests.auth import HTTPDigestAuth
import time
import sys

# --- FROST PROTOCOL: FORCE OVERRIDE ---
DEFAULT_IP = "192.168.0.3"
MAC_ADDRESS = "50:06:F5:A5:26:E8"
DEV_USER = "rokudev"
DEV_PASS = "jeww"

# Ports
PORT_ECP = 8060
PORT_DEV = 80

def authenticate_device(ip):
    print(f"[*] CHECKING LOCK STATUS on Node {ip}...")
    url = f"http://{ip}:{PORT_DEV}/"
    try:
        response = requests.get(url, auth=HTTPDigestAuth(DEV_USER, DEV_PASS), timeout=3)
        if response.status_code == 200:
            print("    [+] PASSWORD ACCEPTED.")
        else:
            print("    [!] PASSWORD REJECTED. (Ignoring...)")
    except:
        print("    [!] DEV PORT UNREACHABLE. (Ignoring...)")

def inject_sequence_506(ip):
    print(f"\n[*] EXECUTING FORCE INJECTION (Code 506)...")
    base_url = f"http://{ip}:{PORT_ECP}"
    sequence = ["Lit_5", "Lit_0", "Lit_6"]
    
    for key in sequence:
        print(f"    >> FORCING SIGNAL: {key}")
        try:
            # We don't need a password for keypresses usually
            requests.post(f"{base_url}/keypress/{key}", timeout=2)
            time.sleep(0.5) 
        except:
            print("    [!] PACKET BLOCKED")

def launch_conduit(ip):
    print("[*] OPENING VISUAL GATEWAY...")
    try:
        requests.post(f"http://{ip}:{PORT_ECP}/launch/837", timeout=2)
        print("    [+] GATEWAY COMMAND SENT.")
    except:
        print("    [!] LAUNCH FAILED")

if __name__ == "__main__":
    print(f"❄️ FROST PROTOCOL: ROOT OVERRIDE")
    print(f"Target: {DEFAULT_IP} ({MAC_ADDRESS})")
    print("--------------------------------")
    
    # 1. Try to login (for logs only)
    authenticate_device(DEFAULT_IP)
    
    # 2. THE OVERRIDE: We run this regardless of the login result
    print("\n[!] BYPASSING SECURITY LAYER...")
    inject_sequence_506(DEFAULT_IP)
    launch_conduit(DEFAULT_IP)
    
    print("\n[+] OVERRIDE COMPLETE.")
EOF

# 2. Execute
python main.py
