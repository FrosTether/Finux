#!/bin/bash

# ==========================================
# ♍ FPU4EVA REPAIR PROTOCOL
#    Target: Termux Native Compilation
#    Fix: Package Naming Convention
# ==========================================

echo ">> [INIT] Developer FPU Override Engaged..."

# 1. CLEANUP (Wipe the failed attempts)
# ------------------------------------------
echo ">> [PURGE] Wiping corrupted build cache..."
pip uninstall kivy -y 2>/dev/null
rm -rf ~/.cache/pip
rm -rf "$HOME/finux/build_logs"

# 2. INSTALL CORRECT TERMUX PACKAGES
# ------------------------------------------
echo ">> [DEPS] Installing Native Headers..."
# ENABLE REPO
pkg install x11-repo -y
pkg update -y

# CRITICAL FIX: Using Termux names (No '-dev' suffix)
# 'xorgproto' provides the X11/X.h header you were missing
pkg install -y \
    libx11 libxext libxrender xorgproto \
    mesa libglvnd clang python make pkg-config \
    sdl2 sdl2-image sdl2-ttf sdl2-mixer \
    libjpeg-turbo libpng freetype libxml2 libxslt git

# 3. CONFIGURE COMPILER FLAGS
# ------------------------------------------
echo ">> [FLAGS] Pointing Compiler to Termux Paths..."
# We explicitly tell Clang to look in the Termux include folder
export USE_SDL2=1
export CFLAGS="-I$PREFIX/include -I$PREFIX/include/X11 -I$PREFIX/include/SDL2"
export LDFLAGS="-L$PREFIX/lib"
# Kivy Specifics
export KIVY_SDL2_PATH="$PREFIX/include/SDL2"
export KIVY_IMAGE_SDL2=1
export KIVY_AUDIO_SDL2=1

# 4. COMPILE ENGINE (The Moment of Truth)
# ------------------------------------------
echo ">> [BUILD] Compiling Kivy Engine..."
echo ">> NOTE: This takes 5-10 minutes. Screen may freeze. DO NOT QUIT."

pip install --upgrade pip wheel setuptools
pip install "cython<3.0.0"

# Force source build with new flags
pip install --no-cache-dir --no-binary kivy kivy==2.3.0

# 5. RESTORE UI & LAUNCHER
# ------------------------------------------
echo ">> [DEPLOY] Restoring Finux Interface..."
mkdir -p "$HOME/finux/fui"
mkdir -p "$HOME/finux/core"

# Stub Wallet
cat <<EOF > "$HOME/finux/core/FrostWallet.py"
import os, binascii
class FrostWallet:
    def __init__(self): self.addr = "FPU_" + binascii.hexlify(os.urandom(4)).decode()
EOF

# Stub Node
cat <<EOF > "$HOME/finux/core/FrostNode.py"
from FrostWallet import FrostWallet
class FrostNode:
    def __init__(self): self.wallet = FrostWallet(); self.mining = False
    def mine(self): return 1, "0000DEADBEEF"
EOF

# UI
cat <<EOF > "$HOME/finux/fui/Virgo_Chat_UI.py"
import os, sys
from kivy.config import Config
Config.set('graphics', 'maxfps', '30') 
os.environ['KIVY_GL_BACKEND'] = 'sdl2'
os.environ['KIVY_WINDOW'] = 'sdl2'

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

sys.path.append(os.environ['HOME'] + "/finux/core")
from FrostNode import FrostNode

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class VirgoChat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.node = FrostNode()
        self.hud = Label(
            text=f"[ ♍ FPU4EVA BUILD: SUCCESS ]\nKernel: Termux Native\nWallet: {self.node.wallet.addr}",
            size_hint=(1, 0.4), pos_hint={'top': 1.0}, color=(0, 1, 0, 1)
        )
        self.add_widget(self.hud)
        self.input = TextInput(size_hint=(0.9, 0.08), pos_hint={'center_x': 0.5, 'y': 0.05})
        self.add_widget(self.input)

class VirgoApp(App):
    def build(self): return VirgoChat()

if __name__ == "__main__": VirgoApp().run()
EOF

# Launcher
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
export USE_SDL2=1
export KIVY_GL_BACKEND=sdl2
# PASTE NEW API KEY HERE IF NEEDED
export GEMINI_API_KEY=""
echo "♍ Booting FPU4EVA Build..."
python3 $HOME/finux/fui/Virgo_Chat_UI.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FPU REPAIR COMPLETE."
echo "Type 'finux' to launch."
echo "=========================================="
