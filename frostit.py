#!/usr/bin/env python3
"""
FROST PROTOCOL v1.4 - HUB INTEGRATION
Author: FrosTether
"""
import os
import sys
import subprocess
from flask import Flask, jsonify, render_template

# --- KERNEL IMPORTS (Live System Check) ---
try:
    import wealth_dashboard as wd
    WEALTH_ACTIVE = True
except ImportError:
    WEALTH_ACTIVE = False

try:
    import watcher
    WATCHER_ACTIVE = True
except ImportError:
    WATCHER_ACTIVE = False

app = Flask(__name__)

class FrostKernel:
    def __init__(self):
        self.id = "FINUX-MAIN-NODE"
        self.version = "5.5 (Deep Freeze)"
    
    def check_integrity(self):
        # Quick verify that spawn.h is working for system calls
        try:
            subprocess.run(['uname'], capture_output=True)
            return True, "SECURE"
        except:
            return False, "COMPROMISED"

kernel = FrostKernel()

@app.route('/')
def home():
    """Renders the Frost Protocol Hub with Live Data"""
    is_stable, msg = kernel.check_integrity()
    
    # 1. Get Wallet Data (Simulated or Real)
    # If wealth_dashboard.py has a function like get_total_assets(), use it:
    # wallet_assets = wd.get_total_assets() if WEALTH_ACTIVE else "0"
    wallet_assets = "SYNCING..." if WEALTH_ACTIVE else "N/A"

    # 2. Get Watcher Data
    scan_status = "LIVE MONITORING" if WATCHER_ACTIVE else "DISABLED"

    return render_template('index.html', 
                           node_id=kernel.id,
                           kernel_version=kernel.version,
                           integrity=is_stable,
                           integrity_msg=msg,
                           wallet_count=wallet_assets,
                           last_scan=scan_status,
                           modules={
                               "arcade": True, # Placeholder for game status
                               "miner": False  # Placeholder for miner status
                           })

@app.route('/api/status')
def api_status():
    """API for external nodes to check this hub"""
    return jsonify({
        "status": "online",
        "node": kernel.id,
        "load": os.getloadavg()
    })

if __name__ == "__main__":
    print(f"❄️  MOUNTING FROST HUB INTERFACE...")
    app.run(host='0.0.0.0', port=5000)
