#!/bin/bash

# --- MONOKILLER PROTOCOL LAUNCHER (DOGE-DISTRIBUTION) ---
# Target: Virgo ♍ x1777 | Supply: UNCAPPED
# Reward: 10,000 FNR Fixed

echo "🛡️  [LAUNCHER] Initializing Monokiller FOSS x25..."

# 1. Run the Python Validator
python3 monokiller_validator.py

if [ $? -eq 0 ]; then
    echo "✅ [SUCCESS] Virgo x1777 Verified."
    echo "🐕 [DOGE-LOGIC] Applying 10,000 FNR Fixed Reward..."
    
    # 2. Launch Monero Daemon with Doge-Logic override
    # Note: --fixed-block-reward is a custom flag for your FOSS build
    ./monerod --rpc-bind-ip 127.0.0.1 \
              --fixed-block-reward 10000 \
              --detach \
              --restricted-rpc
    
    echo "💎 [ACTIVE] Nodes are now minting even-distribution blocks."
    echo "🚀 [FOSS x25] Bridge Status: @drfrostwavhz is LIVE."
else
    echo "❌ [HALT] Validator Failed. Check .env for Virgo x1777."
    exit 1
fi
