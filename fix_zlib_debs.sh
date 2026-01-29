#!/bin/bash

echo "[❄️] Fixing zlib dependencies for Termux..."

# 1. Install the correct Termux package
# In Termux, 'zlib' includes the headers (what -dev usually has)
pkg update -y
pkg install zlib pkg-config -y

# 2. Force the compiler to find the headers
# This fixes the "headers must be installed" error by explicitly pointing to them
export CFLAGS="-I$PREFIX/include"
export LDFLAGS="-L$PREFIX/lib"
export CPPFLAGS="-I$PREFIX/include"

echo "[✅] zlib installed and linked."

# 3. Check if Cython is actually installed (Double check)
if ! command -v cython &> /dev/null
then
    echo "[...] Cython not found. Installing..."
    pip install cython
fi

echo "------------------------------------------------"
echo "Dependency fix complete."
echo "Please run: ./frostit.sh"
echo "------------------------------------------------"
