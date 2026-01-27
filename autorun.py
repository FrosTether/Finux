# 1. Create the Watchdog Script
cat <<EOF > autorun.py
import requests
import time
import sys
from datetime import datetime

# --- CONFIGURATION ---
TARGET_IP = "192.168.0.3"
PORT_ECP = 8060
CHECK_INTERVAL = 5 # Seconds between pings

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def inject_kernel():
    print(f"\n[{get_timestamp()}] ⚠️ RESTART DETECTED. AUTO-RUNNING KERNEL...")
    base_url = f"http://{TARGET_IP}:{PORT_ECP}"
    
    # 1. The 5-0-6 Sequence
    sequence = ["Lit_5", "Lit_0", "Lit_6"]
    for key in sequence:
        try:
            requests.post(f"{base_url}/keypress/{key}", timeout=1)
            time.sleep(0.5)
        except:
            pass
            
    # 2. Re-Open the Gate
    try:
        requests.post(f"{base_url}/launch/837", timeout=1)
        print(f"[{get_timestamp()}] ✅ KERNEL RESTORED. GATEWAY ACTIVE.")
    except:
        print(f"[{get_timestamp()}] ❌ INJECTION FAILED.")

def monitor_loop():
    print(f"❄️ FROST WATCHDOG: ACTIVE")
    print(f"Target: {TARGET_IP}")
    print(f"Policy: AUTO-RUN ON RESTART")
    print("--------------------------------")
    
    was_offline = True # Assume offline at start to force initial inject
    
    while True:
        try:
            # Ping the device info endpoint
            requests.get(f"http://{TARGET_IP}:{PORT_ECP}/query/device-info", timeout=2)
            
            if was_offline:
                # Device just came back online (or script just started)
                print(f"[{get_timestamp()}] 🔌 CONNECTION ESTABLISHED.")
                inject_kernel()
                was_offline = False
            else:
                # Standard Heartbeat
                sys.stdout.write(f"\r[{get_timestamp()}] 💓 SYSTEM STABLE...")
                sys.stdout.flush()
                
        except requests.exceptions.RequestException:
            if not was_offline:
                print(f"\n[{get_timestamp()}] 🔻 SIGNAL LOST. WAITING FOR RESTART...")
            was_offline = True
            
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    try:
        monitor_loop()
    except KeyboardInterrupt:
        print("\n\n[!] WATCHDOG TERMINATED.")
EOF

# 2. Activate the Daemon
python autorun.py
