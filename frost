# 1. Update Termux to the latest version
pkg update -y && pkg upgrade -y

# 2. Install Python and the core build tools (Compiler)
pkg install python git clang make binutils pkg-config -y

# 3. Install the graphics & compression libraries (The ones that were missing)
pkg install zlib libjpeg-turbo freetype libpng -y

# 4. Set the environment flags so the compiler finds those libraries
export CFLAGS="-I/data/data/com.termux/files/usr/include"
export LDFLAGS="-L/data/data/com.termux/files/usr/lib"

# 5. Install the Python build tools (Cython is critical)
pip install --upgrade pip
pip install cython wheel

echo "------------------------------------------------"
echo "✅ Environment Ready. You can now deploy Finux."
echo "------------------------------------------------"
