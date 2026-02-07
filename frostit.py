#!/usr/bin/env python3
"""
FROST PROTOCOL - Core Node Module
Part of the Finux/FrostOS Project
Author: FrosTether
"""

import os
import sys
import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

class FrostNode:
    def __init__(self):
        self.version = "1.2"
        self.status = "FROZEN"
        print(f"❄️  FROSTIT NODE v{self.version} INITIALIZED")

    def check_system_integrity(self):
        """Verifies environment variables and subprocess spawning."""
        try:
            # Verifying the spawn.h fix by attempting a system call
            result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
            return True, result.stdout.strip()
        except Exception as e:
            return False, str(e)

# --- Flask API Routes ---
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "node": "Finux-Main",
        "protocol": "Deep Freeze",
        "state": "Active"
    })

def main():
    node = FrostNode()
    
    # Run a quick self-test
    healthy, info = node.check_system_integrity()
    if healthy:
        print(f"✅ System Integrity Confirmed: {info}")
    else:
        print(f"🔥 Integrity Check Failed: {info}")

    # Launch Flask Server
    print("🚀 Launching Frost API on port 5000...")
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
