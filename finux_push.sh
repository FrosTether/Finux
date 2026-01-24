import os
import time
import subprocess
from datetime import datetime

# Fleet configuration
DECKS = ["deck-alpha.local", "deck-beta.local", "deck-gamma.local"]
TARGET_TIME = "01:00:00"

def deploy_update():
    print(f"[{datetime.now()}] Initiating Finux System Update...")
    for deck in DECKS:
        print(f"Syncing with {deck}...")
        # Secure Copy (SCP) the payload to the local node's secure enclave
        subprocess.run(["scp", "-r", "./payload/", f"root@{deck}:/tmp/update/"])
        
        # Trigger the Finux Kernel re-load and restart the Assembly heartbeat
        remote_cmd = "sudo systemctl stop frost_heartbeat && \
                      sudo cp /tmp/update/* /opt/finux/bin/ && \
                      sudo systemctl start frost_heartbeat"
        subprocess.run(["ssh", f"root@{deck}", remote_cmd])
        print(f"Update Successful on {deck}")

# Wait until 01:00
print(f"Finux Update Manager: Standing by for 01:00 window...")
while True:
    current_time = datetime.now().strftime("%H:%M:%S")
    if current_time == TARGET_TIME:
        deploy_update()
        break
    time.sleep(1) # Check every second
