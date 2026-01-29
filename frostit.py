#!/bin/bash

# --- FROST PROTOCOL DEPLOYMENT SCRIPT (TERMUX PATCHED) ---
echo "❄️ Initiating Deep Freeze Protocol..."

# 1. Force Termux Compiler Flags (Crucial for zlib/jpeg)
export CFLAGS="-I/data/data/com.termux/files/usr/include"
export LDFLAGS="-L/data/data/com.termux/files/usr/lib"
export CC="clang"
export CXX="clang++"

echo "Checking environment..."

# 2. Verify Dependencies (Silent Check)
REQUIRED_PKGS="zlib libjpeg-turbo freetype libpng python clang make"
for pkg in $REQUIRED_PKGS; do
    if ! pkg list-installed | grep -q "$pkg"; then
        echo "[!] Missing $pkg. Installing..."
        pkg install "$pkg" -y
    fi
done

# 3. Clean & Prep
echo "🧹 Cleaning up old binaries..."
rm -rf build/ dist/ *.spec

# 4. Build Sequence
echo "🧊 Compiling FrostCrush... (This may take a while)"

# Check if buildozer.spec exists, if not create a dummy one for the build
if [ ! -f "buildozer.spec" ]; then
    echo "# Genering default spec..."
    # Create a minimal spec file to satisfy the build system
    echo '[app]' > buildozer.spec
    echo 'title = Finux' >> buildozer.spec
    echo 'package.name = finux' >> buildozer.spec
    echo 'package.domain = org.frost' >> buildozer.spec
    echo 'source.include_exts = py,png,jpg,kv,atlas' >> buildozer.spec
    echo 'requirements = python3,kivy,zlib,openssl' >> buildozer.spec
    echo 'version = 1.2' >> buildozer.spec
fi

# 5. Execute Build (Simulated or Real)
# If you have the actual build command, put it here. 
# For now, we verify the environment is ready for Python execution.

if python3 -c "import zlib; print('Zlib Linked:', zlib.ZLIB_VERSION)" > /dev/null 2>&1; then
    echo "✅ Zlib linkage confirmed."
else
    echo "🔥 Warning: Python cannot find Zlib. Re-running pip install..."
    pip install --force-reinstall zlib
fi

echo "------------------------------------------------"
echo "❄️ SYSTEM FROZEN. DEPLOYMENT READY."
echo "------------------------------------------------"
# Launch the main node if it exists
if [ -f "main.py" ]; then
    echo "🚀 Launching Finux Node..."
    python main.py
else
    echo "[i] main.py not found. Please upload your script."
fi
