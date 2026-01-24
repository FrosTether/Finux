#!/bin/bash

# ==========================================
# ❄️ FINUX 2026: OPTIMIZATION SUITE
#    Target: FrostCore (Persist & Async)
# ==========================================

echo ">> [OPT] Initializing 2026 Core Protocols..."

# 1. THE DATABASE-BACKED CORE (FrostChain v2)
# ------------------------------------------
# Upgrading from RAM lists to SQLite3 for permanent storage
cat <<EOF > "$HOME/finux/core/FrostChain.py"
import hashlib
import json
import sqlite3
import time
from threading import Thread

class FrostChain:
    # 2026 OPTIMIZATION: Use __slots__ to reduce RAM usage per object
    __slots__ = ['db_path', 'current_transactions', 'mining_active', 'node_id']

    def __init__(self, node_id="Jacob_Frost_Node"):
        self.db_path = "frost.db"
        self.node_id = node_id
        self.current_transactions = []
        self.mining_active = False
        self._init_db()

    def _init_db(self):
        """ Initialize SQLite3 (Persistent Storage) """
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS chain 
                     (index_num INTEGER PRIMARY KEY, timestamp REAL, 
                      transactions TEXT, proof INTEGER, previous_hash TEXT)''')
        # Check if Genesis exists
        c.execute('SELECT count(*) FROM chain')
        if c.fetchone()[0] == 0:
            self._save_block(1, time.time(), [], 100, "1") # Genesis
        conn.commit()
        conn.close()

    def _save_block(self, idx, ts, txs, proof, prev_hash):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("INSERT INTO chain VALUES (?,?,?,?,?)", 
                  (idx, ts, json.dumps(txs), proof, prev_hash))
        conn.commit()
        conn.close()

    def get_last_block(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM chain ORDER BY index_num DESC LIMIT 1")
        row = c.fetchone()
        conn.close()
        return {
            'index': row[0], 'timestamp': row[1], 
            'transactions': json.loads(row[2]), 
            'proof': row[3], 'previous_hash': row[4]
        }

    def proof_of_work(self, last_proof):
        """ 2026 OPTIMIZATION: Battery Saver Algorithm """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
            # CRITICAL: Sleep to prevent CPU overheating
            if proof % 1000 == 0:
                time.sleep(0.01) 
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def mine_daemon(self, callback):
        self.mining_active = True
        callback("[SYSTEM]: Node Validator Started (Low Power Mode)")
        
        while self.mining_active:
            last_block = self.get_last_block()
            proof = self.proof_of_work(last_block['proof'])

            # Reward
            self.current_transactions.append({
                'sender': "0", 'recipient': self.node_id, 'amount': 12.5
            })

            # Save Block to DB
            new_idx = last_block['index'] + 1
            self._save_block(new_idx, time.time(), self.current_transactions, 
                             proof, self.hash(last_block))
            
            self.current_transactions = [] # Reset Mempool
            
            callback(f"[❄️ MINTED]: Block {new_idx} Saved to DB.")
            time.sleep(1) # Pause between blocks (Traffic Control)

    @staticmethod
    def hash(block):
        # Helper to hash a block dictionary
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
EOF

# 2. THE DASHBOARD UPDATE (Visualizing Persistence)
# ------------------------------------------
cat <<EOF > "$HOME/finux/fui/Virgo_Chat_UI.py"
import os
import sys
import threading
from kivy.config import Config

# 2026 OPTIMIZATION: Cap FPS to 30 for battery life
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
from FrostChain import FrostChain

Window.clearcolor = (0.05, 0.05, 0.08, 1) # Void

class VirgoChat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chain = FrostChain()
        
        # HEAD UP DISPLAY
        self.hud = Label(
            text="[ ❄️ FINUX 2026: PERSISTENT NODE ]\nInitializing Database...",
            size_hint=(1, 0.4), pos_hint={'top': 1.0},
            color=(0, 1, 0.8, 1), halign="left", valign="top"
        )
        self.hud.bind(size=self.hud.setter('text_size'))
        self.add_widget(self.hud)

        # INPUT
        self.input = TextInput(
            size_hint=(0.9, 0.08), pos_hint={'center_x': 0.5, 'y': 0.05},
            multiline=False, background_color=(0.1, 0.1, 0.15, 1), 
            foreground_color=(1, 1, 1, 1)
        )
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)
        
        # Load initial state
        self.refresh_status()

    def on_enter(self, instance):
        cmd = self.input.text
        self.input.text = ""
        
        if cmd == "/start":
            t = threading.Thread(target=self.chain.mine_daemon, args=(self.log_thread,))
            t.daemon = True
            t.start()
        elif cmd == "/status":
            self.refresh_status()
        elif cmd == "/stop":
            self.chain.mining_active = False
            self.log("[SYSTEM]: Validator Paused.")
        else:
            self.log(f"> Unknown: {cmd}")

    def refresh_status(self):
        last = self.chain.get_last_block()
        supply = last['index'] * 12.5
        self.log(f"[DB STATUS]: Height {last['index']} | Holdings: {supply} FTC")

    def log_thread(self, text):
        Clock.schedule_once(lambda dt: self.log(text))

    def log(self, text):
        lines = self.hud.text.split("\n")
        lines.append(text)
        self.hud.text = "\n".join(lines[-14:])

class VirgoApp(App):
    def build(self):
        return VirgoChat()

if __name__ == "__main__":
    VirgoApp().run()
EOF

# 3. REBOOT
# ------------------------------------------
echo ">> [SUCCESS] Database Integrated."
echo ">> [SUCCESS] Battery Optimization Applied."
echo ">> Rebooting Finux 2026..."
python3 $HOME/finux/fui/Virgo_Chat_UI.py
