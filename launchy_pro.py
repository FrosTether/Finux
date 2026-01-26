#!/bin/bash
# --- 🧬 NEWKIRK AUTHORIZED LAUNCH ---
# Target: Virgo ♍ x1777 | Checksum: 312
# Seed: 683050920

echo "🛡️  [NEWKIRK] Initializing Master Shroud..."

# Verify the environment dependencies (Rust/Python) are locked
if python3 -c "import kraken, dotenv" &> /dev/null; then
    echo "✅ [BRIDGE] AI Shop Dependencies Verified."
else
    echo "❌ [ERROR] Missing Build Stack. Run fix_deps.py first."
    exit 1
fi

# Launch the Daemon with Doge-Logic 10,000 FNR
./monerod --fixed-block-reward 10000 --detach

# Launch the FAM Dashboard
python3 kelsee_dashboard.py
