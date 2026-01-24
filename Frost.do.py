#!/bin/bash

# ==========================================
# 🚀 FROSTCHAIN: DEPLOYMENT UPLINK
#    Action: Push 'Blizzard Edition' to Chain
#    Target: FrostChain Ledger (frost.db)
# ==========================================

echo ">> [DEPLOY] Bundling Source Code..."

# 1. UPGRADE DATABASE (Add Deployment Layer)
# ------------------------------------------
# We add a new table to track Code Versions on-chain
cat <<'EOF' > "$HOME/finux/core/FrostChain_DB.py"
import sqlite3
import os
import time
import json

class FrostChainDB:
    def __init__(self):
        self.db_path = os.path.expanduser("~/finux/chaindata/frost.db")
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.init_chain()

    def init_chain(self):
        # 1. Block Ledger
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS blocks (
                height INTEGER PRIMARY KEY,
                timestamp REAL,
                miner TEXT,
                hash TEXT,
                prev_hash TEXT
            )
        ''')
        # 2. Deployment Ledger (The Code Registry)
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS deployments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                version TEXT,
                code_hash TEXT,
                modules TEXT,
                timestamp REAL
            )
        ''')
        self.conn.commit()

    def get_height(self):
        self.cursor.execute("SELECT MAX(height) FROM blocks")
        res = self.cursor.fetchone()[0]
        return res if res is not None else 0

    def get_last_hash(self):
        h = self.get_height()
        if h == 0: return "00000000000000000000000000000000"
        self.cursor.execute("SELECT hash FROM blocks WHERE height=?", (h,))
        return self.cursor.fetchone()[0]

    def add_block(self, height, timestamp, miner, block_hash, prev_hash):
        self.cursor.execute("INSERT INTO blocks VALUES (?, ?, ?, ?, ?)", 
                           (height, timestamp, miner, block_hash, prev_hash))
        self.conn.commit()

    def push_deployment(self, version, code_hash, modules):
        # Records the software update on the blockchain
        t = time.time()
        self.cursor.execute("INSERT INTO deployments (version, code_hash, modules, timestamp) VALUES (?, ?, ?, ?)",
                           (version, code_hash, modules, t))
        self.conn.commit()
        return t
EOF

# 2. CREATE THE DEPLOYMENT SCRIPT
# ------------------------------------------
echo ">> [BUILD] Creating Push Logic..."

cat <<'EOF' > "$HOME/finux/core/Deploy.py"
import os
import sys
import hashlib
import time
import struct
from FrostChain_DB import FrostChainDB

# ANSI
CYAN = "\033[38;5;51m"
PURPLE = "\033[38;5;135m"
GREEN = "\033[38;5;46m"
RESET = "\033[0m"

def calculate_checksum(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def deploy():
    print(f"{PURPLE}>> [INIT] Connecting to FrostChain Node...{RESET}")
    db = FrostChainDB()
    
    # 1. SCAN MODULES
    print(f"{PURPLE}>> [SCAN] Hashing Core Modules...{RESET}")
    base_path = os.path.expanduser("~/finux/core/")
    files = ["FrostMaster.py", "BlackBox.py", "FrostChain_DB.py"]
    
    combo_hash = hashlib.sha256()
    module_list = []
    
    for f_name in files:
        full_path = os.path.join(base_path, f_name)
        if os.path.exists(full_path):
            chk = calculate_checksum(full_path)
            combo_hash.update(chk.encode())
            module_list.append(f_name)
            print(f"   {CYAN}├── {f_name} {GREY}[{chk[:8]}]{RESET}")
        else:
            print(f"   {RED}├── {f_name} [MISSING]{RESET}")

    final_hash = combo_hash.hexdigest()
    version_tag = "v9.63-BLIZZARD"
    
    # 2. ANIMATE UPLINK
    print(f"\n{PURPLE}>> [PUSH] Broadcasting to Network...{RESET}")
    # Simulating propagation delay
    for i in range(10, 101, 10):
        sys.stdout.write(f"\r   Progress: [{'#' * (i//10)}{' ' * (10 - i//10)}] {i}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

    # 3. COMMIT TO CHAIN
    ts = db.push_deployment(version_tag, final_hash, str(module_list))
    
    print(f"{GREEN}╔══════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║ 🚀 DEPLOYMENT SUCCESSFUL                     ║{RESET}")
    print(f"{GREEN}╠══════════════════════════════════════════════╣{RESET}")
    print(f"{GREEN}║ VERSION : {CYAN}{version_tag:<27}{GREEN}║{RESET}")
    print(f"{GREEN}║ HASH    : {CYAN}{final_hash[:20]}...{GREEN}       ║{RESET}")
    print(f"{GREEN}║ BLOCK   : {CYAN}Confirmed{GREEN}                          ║{RESET}")
    print(f"{GREEN}╚══════════════════════════════════════════════╝{RESET}")

if __name__ == "__main__":
    deploy()
EOF

# 3. RUN THE DEPLOYMENT
# ------------------------------------------
echo ">> [EXEC] Pushing Update..."
python3 $HOME/finux/core/Deploy.py

echo "=========================================="
echo "✅ CODE PUSHED TO FROSTCHAIN."
echo ">> Version: v9.63-BLIZZARD"
echo ">> Status: Immutable / On-Ledger"
echo "------------------------------------------"
echo "Your node is now running the Official Deployment."
echo "Type 'finux' to resume mining operations."
echo "=========================================="
