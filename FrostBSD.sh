#!/bin/bash

# ==========================================
# 🐡 FINUX BSD: TOTAL DEPENDENCY REBUILD
#    Target: FinuxBSD (RC1)
#    Fix: Correct Termux Package Names (No -dev)
# ==========================================

echo ">> [INIT] Starting FinuxBSD Rebuild..."

# 1. CLEANUP (Wipe broken installs)
# ------------------------------------------
echo ">> [PURGE] Wiping corrupted libraries..."
pip uninstall kivy -y 2>/dev/null
rm -rf ~/.cache/pip
rm -rf "$HOME/finux/build_logs"

# 2. INSTALL CORRECT TERMUX PACKAGES
# ------------------------------------------
echo ">> [DEPS] Installing X11 & Graphics Headers..."
# Enabling the X11 repository
pkg install x11-repo -y
pkg update -y

# NOTE: In Termux, packages don't use '-dev'. 
# We install the main packages which include headers.
pkg install -y \
    libx11 libxext libxrender xorgproto \
    mesa libglvnd clang python make pkg-config \
    sdl2 sdl2-image sdl2-ttf sdl2-mixer \
    libjpeg-turbo libpng freetype libxml2 libxslt git

# 3. SET COMPILER FLAGS (The "BSD" Config)
# ------------------------------------------
echo ">> [FLAGS] Exporting Include Paths..."
# We explicitly tell Clang where to find the X11 headers we just installed
export USE_SDL2=1
export CFLAGS="-I$PREFIX/include -I$PREFIX/include/X11 -I$PREFIX/include/SDL2"
export LDFLAGS="-L$PREFIX/lib"
# Kivy specific flags
export KIVY_SDL2_PATH="$PREFIX/include/SDL2"
export KIVY_IMAGE_SDL2=1
export KIVY_AUDIO_SDL2=1

# 4. COMPILE ENGINE (From Source)
# ------------------------------------------
echo ">> [BUILD] Compiling FinuxBSD Engine..."
echo ">> NOTE: This takes 5-10 mins. Screen might freeze slightly."
pip install --upgrade pip wheel setuptools
pip install "cython<3.0.0"

# Force source build to link against new X11 headers
pip install --no-cache-dir --no-binary kivy kivy==2.3.0

# 5. DEPLOY FINUX BSD BRANDING
# ------------------------------------------
echo ">> [DEPLOY] Injecting FinuxBSD Interface..."
mkdir -p "$HOME/finux/fui"
mkdir -p "$HOME/finux/core"

# [A] Dummy Core for UI
cat <<EOF > "$HOME/finux/core/FrostNode.py"
class FrostNode:
    def __init__(self): self.wallet = type('obj', (object,), {'addr': 'BSD_ROOT_USER'})
    def mine(self): return None
EOF

# [B] FinuxBSD UI
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

Window.clearcolor = (0.1, 0.1, 0.1, 1) # BSD Grey

class FinuxChat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hud = Label(
            text="[ 🐡 FinuxBSD: SYSTEM READY ]\nKernel: Stable\nX11 Headers: Linked",
            size_hint=(1, 0.4), pos_hint={'top': 1.0}, color=(1, 1, 0, 1)
        )
        self.add_widget(self.hud)

        self.input = TextInput(size_hint=(0.9, 0.08), pos_hint={'center_x': 0.5, 'y': 0.05})
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)

    def on_enter(self, instance):
        self.hud.text += "\n> " + self.input.text
        self.input.text = ""

class FinuxBSDApp(App):
    def build(self): return FinuxChat()

if __name__ == "__main__": FinuxBSDApp().run()
EOF

# 6. LAUNCHER
# ------------------------------------------
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
export USE_SDL2=1
export KIVY_GL_BACKEND=sdl2
echo "🐡 Booting FinuxBSD..."
python3 $HOME/finux/fui/Virgo_Chat_UI.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FINUX BSD REBUILD COMPLETE."
echo "Type 'finux' to launch."
echo "=========================================="
