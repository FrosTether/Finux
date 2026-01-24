#!/bin/bash

# ==========================================
# ❄️ FROST.DO: FIVY APP RELEASE
#    Ver: 1.0 (963 Hz Kernel)
#    Engine: Fivy (Custom X11/GL Build)
# ==========================================

echo ">> [FROST.DO] Packaging 'Fivy' Engine..."

# 1. INSTALL 'FIVY' DEPENDENCIES (The Custom Layer)
# ------------------------------------------
echo ">> [FIVY] Injecting Termux Native Headers..."
# This is the "Fivy" secret sauce: Using native names (xorgproto) instead of debian names
pkg install x11-repo -y
pkg update -y
pkg install -y \
    xorgproto libx11 libxext libxrender \
    mesa libglvnd clang python make pkg-config \
    sdl2 sdl2-image sdl2-ttf sdl2-mixer \
    libjpeg-turbo libpng freetype libxml2 libxslt git

# 2. COMPILE FIVY ENGINE (Force Rebuild)
# ------------------------------------------
echo ">> [BUILD] Compiling Fivy Graphics Core..."
echo ">> NOTE: This wipes the old broken cache. Wait 5 mins."

# Export flags so the compiler sees our 'Fivy' headers
export USE_SDL2=1
export CFLAGS="-I$PREFIX/include -I$PREFIX/include/X11 -I$PREFIX/include/SDL2"
export LDFLAGS="-L$PREFIX/lib"
export KIVY_SDL2_PATH="$PREFIX/include/SDL2"
export KIVY_IMAGE_SDL2=1

# Nuke old builds and force fresh install
pip uninstall kivy -y 2>/dev/null
rm -rf ~/.cache/pip
pip install --upgrade pip wheel setuptools "cython<3.0.0"
pip install --no-cache-dir --no-binary kivy kivy==2.3.0

# 3. DEPLOY APP: FROSTCORE 963 (The Code)
# ------------------------------------------
echo ">> [APP] Installing FrostCore 963 Hz..."
mkdir -p "$HOME/finux/fui"
mkdir -p "$HOME/finux/core"

# [A] 963 Hz NODE
cat <<EOF > "$HOME/finux/core/FrostNode.py"
import time, hashlib, socket, struct
class FrostWallet:
    def __init__(self): self.addr = "FIVY_REL_" + hashlib.sha256(str(time.time()).encode()).hexdigest()[:8]

class FrostNode:
    def __init__(self):
        self.wallet = FrostWallet()
        self.mining = False
        self.FREQUENCY = 963.0
        self.CYCLE = 1.0 / self.FREQUENCY # 0.001038s

    def mine(self):
        # 963 Hz Oscillator Logic
        time.sleep(self.CYCLE) 
        entropy = struct.pack(">Q", int(time.time_ns() * self.FREQUENCY) & 0xFFFFFFFFFFFFFFFF)
        hash_val = hashlib.sha256(entropy).hexdigest()
        return time.time(), hash_val
EOF

# [B] VIRGO INTERFACE (Fivy Branded)
cat <<EOF > "$HOME/finux/fui/Virgo_Chat_UI.py"
import os, sys, threading
from kivy.config import Config
# Fivy Optimization: Cap FPS for battery
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

# Fivy Brand Colors (Void Black & Neon Cyan)
Window.clearcolor = (0.02, 0.02, 0.05, 1)

class VirgoChat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.node = FrostNode()
        
        self.hud = Label(
            text=f"[ ❄️ APP: FROST FIVY ]\nEngine: Active (963 Hz)\nID: {self.node.wallet.addr}\nStatus: READY",
            size_hint=(1, 0.4), pos_hint={'top': 1.0}, color=(0, 1, 1, 1), bold=True
        )
        self.add_widget(self.hud)

        self.input = TextInput(
            size_hint=(0.9, 0.08), pos_hint={'center_x': 0.5, 'y': 0.05},
            background_color=(0.1, 0.1, 0.2, 1), foreground_color=(1,1,1,1)
        )
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)

    def on_enter(self, instance):
        cmd = self.input.text
        self.input.text = ""
        if cmd == "/start":
            self.node.mining = True
            threading.Thread(target=self.mine_loop, daemon=True).start()
            self.log(">> 963 Hz Oscillator: RUNNING")
        elif cmd == "/stop":
            self.node.mining = False
            self.log(">> Halted.")
        else:
            self.log(f">> Exec: {cmd}")

    def mine_loop(self):
        while self.node.mining:
            res = self.node.mine()
            if res: Clock.schedule_once(lambda dt: self.log(f"[963] SYNC: {res[1][:10]}..."))

    def log(self, t):
        self.hud.text += "\n" + t

class VirgoApp(App):
    def build(self): return VirgoChat()

if __name__ == "__main__": VirgoApp().run()
EOF

# 4. CREATE LAUNCHER (The "New App" feel)
# ------------------------------------------
echo ">> [RELEASE] Stamping 'finux' Command..."
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
export USE_SDL2=1
export KIVY_GL_BACKEND=sdl2
# ⚠️ If you have a key, export GEMINI_API_KEY="YOUR_KEY" here
echo "❄️ Booting FrostOS (Fivy Edition)..."
python3 $HOME/finux/fui/Virgo_Chat_UI.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FIVY APP RELEASED."
echo ">> Dependency Layer: Fivy (Native)"
echo ">> Core Frequency: 963 Hz"
echo ">> Launch Command: 'finux'"
echo "=========================================="
