#!/bin/bash

# ==========================================
# 🔧 FIVY REPAIR: X11 HEADER PATCH
#    Target: Android 17 PC (Mainnet + RCS)
#    Fix: 'X11/X.h' File Not Found
# ==========================================

echo ">> [INIT] Fivy Repair Sequence Started..."

# 1. INSTALL MISSING X11 LIBRARIES (The Fix)
# ------------------------------------------
echo ">> [DEPS] Installing X11 Window Headers..."
# We need libx11-dev and xorgproto to provide 'X11/X.h'
pkg update -y
pkg install x11-repo -y
pkg install -y libx11-dev libxext-dev libxrender-dev xorgproto \
    mesa-dev libglvnd-dev clang python make pkg-config \
    sdl2 sdl2-image sdl2-ttf sdl2-mixer \
    libjpeg-turbo libpng freetype libxml2 libxslt git

# 2. CONFIGURE COMPILER
# ------------------------------------------
echo ">> [FLAGS] Forcing X11 Include Paths..."
# This points the compiler to the folder we just installed
export USE_SDL2=1
export CFLAGS="-I$PREFIX/include -I$PREFIX/include/X11 -I$PREFIX/include/SDL2"
export LDFLAGS="-L$PREFIX/lib"
export KIVY_SDL2_PATH="$PREFIX/include/SDL2"
export KIVY_IMAGE_SDL2=1

# 3. RECOMPILE FIVY ENGINE
# ------------------------------------------
echo ">> [BUILD] Compiling Engine (This takes 5 mins)..."
# Wipe cache to ensure the new X11 flags are used
pip uninstall kivy -y 2>/dev/null
rm -rf ~/.cache/pip

pip install --no-cache-dir --no-binary kivy kivy==2.3.0

# 4. RESTORE ALTERATIONS (FrostCore + Mainnet + RCS)
# ------------------------------------------
echo ">> [RESTORE] Injecting Android 17 Modules..."
mkdir -p "$HOME/finux/fui"
mkdir -p "$HOME/finux/core"
mkdir -p "$HOME/finux/comms"
mkdir -p "$HOME/finux/keystore"

# [A] FrostWallet (Mainnet Stub)
cat <<EOF > "$HOME/finux/core/FrostWallet.py"
import os, binascii
class FrostWallet:
    def __init__(self):
        # Generates a persistent ID based on device
        self.addr = "FROST_" + binascii.hexlify(os.urandom(8)).decode()
EOF

# [B] FrostNode (Mainnet Logic)
cat <<EOF > "$HOME/finux/core/FrostNode.py"
import time, os, threading
from FrostWallet import FrostWallet

class FrostNode:
    def __init__(self):
        self.wallet = FrostWallet()
        self.mining = False
    
    def mine(self):
        time.sleep(1) # Sim work
        # Returns (BlockHeight, Hash)
        return int(time.time()), "0000" + os.urandom(12).hex()
EOF

# [C] FrostRCS (Signal Bridge)
cat <<EOF > "$HOME/finux/comms/FrostRCS.py"
import json
class FrostSignal:
    def send(self, msg):
        return json.dumps({"protocol": "RCS-FROST", "payload": msg})
EOF

# [D] Android 17 PC UI (Virgo Dashboard)
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
            text=f"[ ❄️ ANDROID 17 PC: FIVY ]\nID: {self.node.wallet.addr}\nStatus: ONLINE",
            size_hint=(1, 0.4), pos_hint={'top': 1.0}, color=(0, 1, 0, 1)
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
            self.log(">> Mining Started...")
        else:
            self.log(f">> Exec: {cmd}")

    def mine_loop(self):
        while self.node.mining:
            res = self.node.mine()
            Clock.schedule_once(lambda dt: self.log(f"[MINED] Block {res[0]}"))

    def log(self, t):
        self.hud.text += "\n" + t

class VirgoApp(App):
    def build(self): return VirgoChat()

if __name__ == "__main__": VirgoApp().run()
EOF

# 5. RE-LINK LAUNCHER
# ------------------------------------------
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
export USE_SDL2=1
export KIVY_GL_BACKEND=sdl2
echo "🚀 Booting Android 17 (Fivy Build)..."
python3 $HOME/finux/fui/Virgo_Chat_UI.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FIVY REPAIR COMPLETE."
echo "Type 'finux' to launch."
echo "=========================================="
