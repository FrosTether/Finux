#!/bin/bash

# ==========================================
# ❄️ FROSTCORE MAINNET: DEPLOYMENT SUITE
#    Network ID: 9921 (Frost Mainnet)
# ==========================================

echo ">> [MAINNET] Initiating Launch Sequence..."

# 1. INSTALL CRYPTO DEPENDENCIES
# ------------------------------------------
echo ">> [DEPS] Installing Elliptic Curve Libraries..."
pip install ecdsa requests

# 2. THE SECURE WALLET (Key Generation)
# ------------------------------------------
mkdir -p "$HOME/finux/keystore"
mkdir -p "$HOME/finux/core"

cat <<EOF > "$HOME/finux/core/FrostWallet.py"
import os
import ecdsa
import binascii

class FrostWallet:
    def __init__(self):
        self.keystore_path = os.environ['HOME'] + "/finux/keystore/node_wallet.pem"
        self.private_key = None
        self.public_address = None
        self.load_or_create()

    def load_or_create(self):
        # If key exists, load it. If not, generate new Mainnet Key.
        if os.path.exists(self.keystore_path):
            with open(self.keystore_path, "rb") as f:
                self.private_key = ecdsa.SigningKey.from_pem(f.read())
        else:
            self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
            with open(self.keystore_path, "wb") as f:
                f.write(self.private_key.to_pem())
        
        # Derive Public Key (Address)
        vk = self.private_key.verifying_key
        self.public_address = "FROST" + binascii.hexlify(vk.to_string()).decode()[:32]

    def sign(self, message):
        return binascii.hexlify(self.private_key.sign(message.encode())).decode()
EOF

# 3. THE MAINNET NODE (Networking + Consensus)
# ------------------------------------------
cat <<EOF > "$HOME/finux/core/FrostNode.py"
import socket
import threading
import json
import time
import sqlite3
import hashlib
from FrostWallet import FrostWallet

class FrostNode:
    def __init__(self):
        self.wallet = FrostWallet()
        self.host = '0.0.0.0'
        self.port = 9921
        self.db_path = "frost_mainnet.db"
        self.peers = set()
        self.mining = False
        
        self._init_db()
        self._start_server()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS chain 
                     (idx INTEGER PRIMARY KEY, hash TEXT, prev_hash TEXT, 
                      data TEXT, nonce INTEGER, timestamp REAL)''')
        # MAINNET GENESIS BLOCK
        c.execute('SELECT count(*) FROM chain')
        if c.fetchone()[0] == 0:
            genesis_data = json.dumps({"msg": "Frost Mainnet Launch 2026"})
            c.execute("INSERT INTO chain VALUES (?,?,?,?,?,?)", 
                      (1, "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f", 
                       "0", genesis_data, 2083236893, time.time()))
        conn.commit()
        conn.close()

    def _start_server(self):
        # P2P Listener
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"[NET] Listening on Port {self.port}")
        
        t = threading.Thread(target=self._accept_peers)
        t.daemon = True
        t.start()

    def _accept_peers(self):
        while True:
            client, addr = self.server.accept()
            # In a full implementation, we would handshake here
            self.peers.add(addr[0])

    def get_last_block(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM chain ORDER BY idx DESC LIMIT 1")
        row = c.fetchone()
        conn.close()
        return row

    def mine_block(self):
        # Mainnet Difficulty
        last = self.get_last_block()
        idx = last[0] + 1
        prev_hash = last[1]
        
        # Coinbase Transaction (Reward to YOUR Wallet)
        data = json.dumps({
            "reward": 50,
            "to": self.wallet.public_address,
            "signature": self.wallet.sign(f"Block {idx}")
        })
        
        nonce = 0
        while True:
            if not self.mining: return None
            
            block_str = f"{idx}{prev_hash}{data}{nonce}".encode()
            block_hash = hashlib.sha256(block_str).hexdigest()
            
            # Difficulty: Starts with "0000"
            if block_hash.startswith("0000"):
                conn = sqlite3.connect(self.db_path)
                c = conn.cursor()
                c.execute("INSERT INTO chain VALUES (?,?,?,?,?,?)", 
                          (idx, block_hash, prev_hash, data, nonce, time.time()))
                conn.commit()
                conn.close()
                return idx, block_hash
            
            nonce += 1
            if nonce % 5000 == 0: time.sleep(0.01) # Heat management
EOF

# 4. THE MAINNET UI
# ------------------------------------------
cat <<EOF > "$HOME/finux/fui/Virgo_Chat_UI.py"
import os
import sys
import threading
from kivy.config import Config

Config.set('graphics', 'maxfps', '30') 
os.environ['KIVY_GL_BACKEND'] = 'sdl2' 
os.environ['KIVY_WINDOW'] = 'sdl2'

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.window import Window

sys.path.append(os.environ['HOME'] + "/finux/core")
from FrostNode import FrostNode

Window.clearcolor = (0.05, 0.05, 0.08, 1)

class MainnetUI(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.node = FrostNode()
        
        # DASHBOARD
        addr_short = self.node.wallet.public_address[:16] + "..."
        self.hud = Label(
            text=f"[ ❄️ FROST MAINNET: LIVE ]\nNode: Active (Port 9921)\nWallet: {addr_short}\nStatus: Idle",
            size_hint=(1, 0.4), pos_hint={'top': 1.0},
            color=(0,
