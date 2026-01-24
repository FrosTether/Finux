#!/bin/bash

# ==========================================
# ❄️ FROSTINSTALLER 2.0: MAINNET INTEGRATION
#    Target: Android 17 PC (Pumpkin Cheesecake)
#    Fix: 'GL/gl.h' Missing Header + Core Install
# ==========================================

echo ">> [INIT] Starting Frostinstaller 2.0..."

# 1. FIX THE MISSING HEADER (The "GL/gl.h" Error)
# ------------------------------------------
echo ">> [DEPS] Installing Mesa OpenGL Headers..."
# We need 'mesa-dev' to fix the error in your screenshot
pkg update -y
pkg install x11-repo -y
pkg install -y mesa-dev libglvnd-dev clang python make pkg-config \
    sdl2 sdl2-image sdl2-ttf sdl2-mixer \
    libjpeg-turbo libpng freetype libxml2 libxslt git

# 2. INSTALL CRYPTO & NETWORK UTILS
# ------------------------------------------
echo ">> [CORE] Installing FrostCore Dependencies..."
pip install ecdsa requests

# 3. CONFIGURE & COMPILE ENGINE
# ------------------------------------------
echo ">> [BUILD] Wiping old cache & Recompiling..."
pip uninstall kivy -y 2>/dev/null
rm -rf ~/.cache/pip

# Force Kivy to find the new X11 headers
export USE_SDL2=1
export CFLAGS="-I$PREFIX/include/SDL2 -I$PREFIX/include"
export LDFLAGS="-L$PREFIX/lib"
export KIVY_SDL2_PATH="$PREFIX/include/SDL2"
export KIVY_IMAGE_SDL2=1

# Compile (This fixes the 'wheel' error)
pip install --no-cache-dir --no-binary kivy kivy==2.3.0

# 4. DEPLOY FROSTCORE MAINNET (Wallet & Node)
# ------------------------------------------
echo ">> [DEPLOY] Injecting Mainnet Source Code..."
mkdir -p "$HOME/finux/core"
mkdir -p "$HOME/finux/keystore"

# [A] FrostWallet.py
cat <<EOF > "$HOME/finux/core/FrostWallet.py"
import os
import ecdsa
import binascii

class FrostWallet:
    def __init__(self):
        self.path = os.environ['HOME'] + "/finux/keystore/node_wallet.pem"
        self.load_or_create()

    def load_or_create(self):
        if os.path.exists(self.path):
            with open(self.path, "rb") as f:
                self.sk = ecdsa.SigningKey.from_pem(f.read())
        else:
            self.sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
            with open(self.path, "wb") as f:
                f.write(self.sk.to_pem())
        self.addr = "FROST" + binascii.hexlify(self.sk.verifying_key.to_string()).decode()[:32]

    def sign(self, msg):
        return binascii.hexlify(self.sk.sign(msg.encode())).decode()
EOF

# [B] FrostNode.py
cat <<EOF > "$HOME/finux/core/FrostNode.py"
import socket, threading, json, time, sqlite3, hashlib
from FrostWallet import FrostWallet

class FrostNode:
    def __init__(self):
        self.wallet = FrostWallet()
        self.db = "frost_mainnet.db"
        self.mining = False
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS chain (idx INT, hash TEXT, prev TEXT, data TEXT, nonce INT)')
        if c.execute('SELECT count(*) FROM chain').fetchone()[0] == 0:
            c.execute("INSERT INTO chain VALUES (?,?,?,?,?)", (1, "0"*64, "0", "GENESIS", 0))
        conn.commit()
        conn.close()

    def mine(self):
        conn = sqlite3.connect(self.db)
        c = conn.cursor()
        last = c.execute("SELECT * FROM chain ORDER BY idx DESC LIMIT 1").fetchone()
        conn.close()
        
        idx, prev = last[0] + 1, last[1]
        data = json.dumps({"reward": 50, "miner": self.wallet.addr})
        nonce = 0
        
        while self.mining:
            block_hash = hashlib.sha256(f"{idx}{prev}{data}{nonce}".encode()).hexdigest()
            if block_hash.startswith("0000"): # Difficulty
                conn = sqlite3.connect(self.db)
                c = conn.cursor()
                c.execute("INSERT INTO chain VALUES (?,?,?,?,?)", (idx, block_hash, prev, data, nonce))
                conn.commit()
                conn.close()
                return idx, block_hash
            nonce += 1
            if nonce % 2000 == 0: time.sleep(0.01)
EOF

# 5. DEPLOY UI (Android 17 PC Dashboard)
# ------------------------------------------
echo ">> [UI] Deploying Virgo Dashboard..."
mkdir -p "$HOME/finux/fui"

cat <<EOF > "$HOME/finux/fui/Virgo_Chat_UI.py"
import os, sys, threading
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

class VirgoChat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.node = FrostNode()
        
        self.hud = Label(
            text=f"[ ❄️ ANDROID 17 PC: MAINNET ]\nWallet: {self.node.wallet.addr[:12]}...\nStatus: READY",
            size_hint=(1, 0.4), pos_hint={'top': 1.0}, color=(0, 1, 0, 1), halign="left"
        )
        self.add_widget(self.hud)

        self.input = TextInput(size_hint=(0.9, 0.08), pos_hint={'center_x': 0.5, 'y': 0.05})
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)

    def on_enter(self, instance):
        cmd = self.input.text
        self.input.text = ""
        if cmd == "/start":
            self.node.mining = True
            threading.Thread(target=self.mine_loop, daemon=True).start()
            self.log(">> Miner Started (Mainnet)")
        elif cmd == "/stop":
            self.node.mining = False
            self.log(">> Miner Stopped")
        else:
            self.log(f">> Unknown: {cmd}")

    def mine_loop(self):
        while self.node.mining:
            res = self.node.mine()
            if res: Clock.schedule_once(lambda dt: self.log(f"[MINED] Block {res[0]}"))

    def log(self, t):
        self.hud.text += "\n" + t

class VirgoApp(App):
    def build(self): return VirgoChat()

if __name__ == "__main__": VirgoApp().run()
EOF

# 6. LAUNCHER
# ------------------------------------------
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
export USE_SDL2=1
export KIVY_GL_BACKEND=sdl2
echo "🚀 Booting Android 17 PC (Mainnet)..."
python3 $HOME/finux/fui/Virgo_Chat_UI.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FROSTINSTALLER 2.0 COMPLETE."
echo "Type 'finux' to launch Mainnet."
echo "=========================================="
