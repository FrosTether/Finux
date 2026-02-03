#!/bin/sh
# ------------------------------------------------------------------
# FROST DEPLOYMENT PROTOCOL - SURGE.SH
# Domain: frosttest.surge.sh
# ------------------------------------------------------------------

PROJECT_DIR="./dist"  # Change this to your build folder (e.g., ./public or .)
DOMAIN="frosttest.surge.sh"

echo "[*] Initializing Frost Deployment Sequence..."

# 1. CHECK DEPENDENCIES (Node.js & NPM)
if ! command -v npm >/dev/null 2>&1; then
    echo "[!] NPM not detected. Installing via BSD Package Manager..."
    # Switch to root to install pkg
    su root -c "pkg install -y node npm"
else
    echo "[+] Node.js/NPM detected."
fi

# 2. INSTALL SURGE (Global)
if ! command -v surge >/dev/null 2>&1; then
    echo "[!] Surge CLI not found. Installing..."
    npm install --global surge
fi

# 3. BUILD PROJECT (Optional - uncomment if you have a build step)
# echo "[*] Building Project..."
# npm run build

# 4. DEPLOY TO FROSTTEST
echo "------------------------------------------------------------------"
echo "   TARGET: ${DOMAIN}"
echo "   SOURCE: ${PROJECT_DIR}"
echo "------------------------------------------------------------------"

# The generic command is 'surge <folder> <domain>'
# First run might require login credentials
surge ${PROJECT_DIR} ${DOMAIN}

echo "[SUCCESS] Deployed to https://${DOMAIN}"
