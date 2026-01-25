#!/bin/bash

# --- MONOKILLER PROTOCOL LAUNCHER ---
# Target: Virgo ♍ x1777
# Clearance: G-Partner Authorized

echo "🛡️  [LAUNCHER] Initializing Monokiller FOSS x25 Environment..."

# 1. Run the Python Validator
python3 monokiller_validator.py

# Capture the exit status of the validator
VALIDATOR_STATUS=$?

if [ $VALIDATOR_STATUS -eq 0 ]; then
    echo "✅ [SUCCESS] Virgo x1777 Coordinate Verified. G-Partner Credentials Confirmed."
    echo "🔗 [NODE] Starting Monero Daemon (Monokiller Shrouded)..."
    
    # 2. Launch monerod with background detach and RPC enabled for Frostnerjo wallets
    # Note: Using --detach to keep the process running in the background
    monerod --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18081 --detach --restricted-rpc --confirm-external-bind
    
    echo "💎 [ACTIVE] Monero Node is now syncing in Sub-Zero storage."
    echo "🚀 [FOSS x25] Protocol is LIVE. Tell Kelsee the bridge is open."
else
    echo "❌ [HALT] Validator Failed. Deployment Aborted."
    echo "⚠️  Ensure the .env file is locked to Virgo x1777 and G-Partner ID is correct."
    exit 1
fi
