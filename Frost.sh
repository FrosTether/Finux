#!/bin/bash

# ==========================================
# ❄️ FROSTINSTALLER 1: RECOMPILE SEQUENCE
#    Target: Android 17 (Pumpkin Cheesecake)
#    Fix: X11 Repo Injection
# ==========================================

echo ">> [FROSTINSTALLER1] Initiating System Repair..."

# 1. CRITICAL REPO FIX (The Missing Link)
# ------------------------------------------
echo ">> [REPO] Enabling X11 Repository..."
# This command fixes the 'sdl2 not found' error
pkg install x11-repo -y
pkg update -y

# 2. PURGE BROKEN CACHE
# ------------------------------------------
echo ">> [CLEAN] Wiping corrupted build files..."
pip uninstall kivy -y 2>/dev/null
rm -rf ~/.cache/pip

# 3. INSTALL GRAPHICS ENGINE (SDL2)
# ------------------------------------------
echo ">> [SD12] Installing Graphics Headers..."
# Now that X11 repo is active, these will succeed
pkg install -y clang python make pkg-config \
    sdl2 sdl2-image sdl2-ttf sdl2-mixer \
    libjpeg-turbo libpng freetype libxml2 libxslt git

# 4. CONFIGURE COMPILER (The "Fivy" Flags)
# ------------------------------------------
echo ">> [FLAGS] Injecting FD1337 Compiler Headers..."
export USE_SDL2=1
export CFLAGS="-I$PREFIX/include/SDL2"
export LDFLAGS="-L$PREFIX/lib"
export KIVY_SDL2_PATH="$PREFIX/include/SDL2"
export KIVY_IMAGE_SDL2=1
export KIVY_AUDIO_SDL2=1

# 5. EXECUTE RECOMPILE
# ------------------------------------------
echo ">> [BUILD] Compiling Engine from Source (Wait 5 mins)..."
pip install --upgrade pip wheel setuptools "cython<3.0.0"

# Force build from source
pip install --no-cache-dir --no-binary kivy kivy==2.3.0

# 6. DEPLOY ANDROID 17 UI
# ------------------------------------------
echo ">> [DEPLOY] Restoring Pumpkin Cheesecake UI..."
mkdir -p "$HOME/finux/fui"

cat <<EOF > "$HOME/finux/fui/Virgo_Chat_UI.py"
import os
import sys

# Termux Graphics Optimization
os.environ['KIVY_GL_BACKEND'] = 'sdl2' 
os.environ['KIVY_WINDOW'] = 'sdl2'

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.08, 1)

class VirgoChat(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(
            text="[ 🎃 Android 17: Frostinstaller1 Build ]\nSystem Online.",
            size_hint=(1, 0.3), pos_hint={'top': 1.0}, color=(1, 0.6, 0, 1)
        ))
        self.input = TextInput(size_hint=(0.9, 0.08), pos_hint={'center_x': 0.5, 'y': 0.05})
        self.add_widget(self.input)

class VirgoApp(App):
    def build(self):
        return VirgoChat()

if __name__ == "__main__":
    VirgoApp().run()
EOF

# 7. UPDATE LAUNCHER
# ------------------------------------------
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
export GEMINI_API_KEY="AIzaSyArl_oHSoUH6DAttIyyFrQulbrmS_umMWM"
export USE_SDL2=1
echo "🚀 Booting Frostinstaller1 Build..."
python3 $HOME/finux/fui/Virgo_Chat_UI.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FROSTINSTALLER1 COMPLETE."
echo "Type 'finux' to launch."
echo "=========================================="
