#!/bin/bash

# ==========================================
# 🦕 INSTANT RESTORE: T-REX MINER
#    Target: Fix 'No such file' Error
#    Action: Point Launcher to Existing File
# ==========================================

echo ">> [RESTORE] Relinking Mining Engine..."

# 1. UPDATE LAUNCHER TO USE THE EXISTING FILE
# ------------------------------------------
# Your screenshot shows FUI_TRex.py exists, so we use that.
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
echo "🦕 Booting T-Rex Miner (963 Hz)..."
python3 $HOME/finux/fui/FUI_TRex.py
EOF

# 2. MAKE EXECUTABLE
# ------------------------------------------
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ LINK RESTORED."
echo ">> The launcher is now fixed."
echo ">> Type 'finux' to start mining."
echo "=========================================="
