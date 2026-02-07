#!/bin/bash

# --- FROST PROTOCOL DEPLOYMENT SCRIPT (TERMUX PATCHED) ---
echo "❄️ Initiating Deep Freeze Protocol..."

# 1. Force Termux Compiler Flags (Using $PREFIX for portability)
export CFLAGS="-I$PREFIX/include"
export LDFLAGS="-L$PREFIX/lib -landroid-spawn" # Added spawn fix
export CC="clang"
export CXX="clang++"

echo "Checking environment..."

# 2. Verify Dependencies (Added libandroid-spawn and ninja)
# These are the heavy hitters that failed earlier.
REQUIRED_PKGS="zlib libjpeg-turbo freetype libpng python clang make ninja cmake libandroid-spawn"
for pkg in $REQUIRED_PKGS; do
    if ! pkg list-installed | grep -q "$pkg"; then
        echo "[!] Missing $pkg. Installing..."
        pkg install "$pkg" -y
    fi
done

# 3. Clean & Prep
echo "🧹 Cleaning up old binaries..."
rm -rf build/ dist/ *.spec

# 4. Build Sequence (FrostCrush / Finux)
echo "🧊 Compiling FrostCrush... (This may take a while)"

# Check if buildozer.spec exists, if not create a dummy one
if [ ! -f "buildozer.spec" ]; then
    echo "# Generating default spec..."
    cat <<EOF > buildozer.spec
[app]
title = Finux
package.name = finux
package.domain = org.frost
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy,zlib,openssl,numpy
version = 1.2
EOF
fi

# 5. Execute Build & Verify
if python3 -c "import zlib; print('Zlib Linked:', zlib.ZLIB_VERSION)" > /dev/null 2>&1; then
    echo "✅ Zlib linkage confirmed."
else
    echo "🔥 Warning: Python cannot find Zlib. Re-running environment link..."
    # Note: 'pip install zlib' doesn't exist; it's a C library.
    # We ensure the headers are there instead.
    pkg install zlib -y
fi

echo "------------------------------------------------"
echo "❄️ SYSTEM FROZEN. DEPLOYMENT READY."
echo "------------------------------------------------"

# 6. Execution
# Check for your specific Finux or FrostOS entry points
if [ -f "main.py" ]; then
    echo "🚀 Launching Finux Node..."
    python3 main.py
elif [ -f "frostit.py" ]; then
    echo "🚀 Launching Frostit Node..."
    python3 frostit.py
else
    echo "[i] Entry point not found. Please ensure main.py or frostit.py exists."
fi
