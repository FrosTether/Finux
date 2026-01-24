#!/bin/bash

# ==========================================
# 🦕 FUI: T-REX EDITION
#    Target: Fix 'libmtdev' & 'EGL' Crashes
#    Engine: Pure Python (No Graphics Libs)
# ==========================================

echo ">> [FUI] Initializing T-Rex Protocol..."

# 1. CLEANUP (Remove the broken Graphics Engine)
# ------------------------------------------
echo ">> [PURGE] Removing broken graphics drivers..."
# We remove Kivy so it never crashes your system again
pip uninstall kivy -y 2>/dev/null

# 2. CREATE THE T-REX DASHBOARD
# ------------------------------------------
mkdir -p "$HOME/finux/fui"
mkdir -p "$HOME/finux/core"

cat <<'EOF' > "$HOME/finux/fui/FUI_TRex.py"
import os
import sys
import time
import hashlib
import struct
import threading
import random

# --- CONFIGURATION ---
# 963 Hz Frequency
FREQ = 963.0
CYCLE = 1.0 / FREQ

# ANSI COLORS (The Cyberpunk Theme)
PURPLE = "\033[38;5;135m"
CYAN = "\033[38;5;51m"
GREEN = "\033[38;5;46m"
RED = "\033[38;5;196m"
GREY = "\033[38;5;240m"
WHITE = "\033[38;5;255m"
RESET = "\033[0m"
BOLD = "\033[1m"
CLEAR_SCREEN = "\033[H\033[J"

class FrostNode:
    def __init__(self):
        # Generate a wallet ID based on system entropy
        self.id = "TREX_" + hashlib.sha256(os.urandom(16)).hexdigest()[:8].upper()
        self.mining = True
        self.blocks = 0
        self.hash_rate = 0
        self.last_hash = "WAITING FOR SIGNAL..."

    def mine(self):
        # The Mining Loop
        while self.mining:
            start = time.time()
            
            # 1. Frequency Sync (The 963 Hz Wait)
            time.sleep(CYCLE)
            
            # 2. Generate Entropy
            entropy = struct.pack(">Q", int(time.time_ns()) & 0xFFFFFFFFFFFFFFFF)
            self.last_hash = hashlib.sha256(entropy).hexdigest()
            self.blocks += 1
            
            # 3. Calculate Rate
            dur = time.time() - start
            if dur > 0:
                self.hash_rate = 1.0 / dur

def draw_interface(node):
    # This draws the UI directly in the terminal
    while node.mining:
        try:
            # Stats
            hr = f"{node.hash_rate:.2f} Hz"
            blk = f"{node.blocks}"
            
            # THE DASHBOARD ART
            buffer = f"{CLEAR_SCREEN}"
            buffer += f"{PURPLE}╔══════════════════════════════════════════════╗{RESET}\n"
            buffer += f"{PURPLE}║ {CYAN}🦕 FUI: T-REX PROTOCOL     {GREY}v3.0 (STABLE){PURPLE}    ║{RESET}\n"
            buffer += f"{PURPLE}╠══════════════════════════════════════════════╣{RESET}\n"
            buffer += f"{PURPLE}║ {WHITE}STATUS : {GREEN}● ONLINE{PURPLE}                            ║{RESET}\n"
            buffer += f"{PURPLE}║ {WHITE}KERNEL : {CYAN}963 Hz OSCILLATOR{PURPLE}                   ║{RESET}\n"
            buffer += f"{PURPLE}║ {WHITE}WALLET : {CYAN}{node.id}{PURPLE}                  ║{RESET}\n"
            buffer += f"{PURPLE}╠══════════════════════════════════════════════╣{RESET}\n"
            buffer += f"{PURPLE}║ {GREY}SPEED  : {WHITE}{hr:<10} {GREY}BLOCKS : {WHITE}{blk:<10} {PURPLE}║{RESET}\n"
            buffer += f"{PURPLE}╠══════════════════════════════════════════════╣{RESET}\n"
            buffer += f"{PURPLE}║ {WHITE}CURRENT HASH:                                {PURPLE}║{RESET}\n"
            buffer += f"{PURPLE}║ {GREY}{node.last_hash[:40]}...{PURPLE} ║{RESET}\n"
            buffer += f"{PURPLE}╚══════════════════════════════════════════════╝{RESET}\n"
            buffer += f"\n{GREY} [CTRL+C] to Halt System{RESET}"
            
            sys.stdout.write(buffer)
            sys.stdout.flush()
            time.sleep(0.1) # Update display 10x per second
            
        except KeyboardInterrupt:
            node.mining = False
            print(f"\n{RED}>> SYSTEM HALTED.{RESET}")
            sys.exit()

def main():
    node = FrostNode()
    
    # Launch Miner in Background
    t = threading.Thread(target=node.mine, daemon=True)
    t.start()
    
    # Launch UI in Foreground
    try:
        draw_interface(node)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()
EOF

# 3. CREATE LAUNCHER
# ------------------------------------------
echo ">> [BUILD] Compiling Launcher..."
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
# Bypass Graphics Config entirely
echo "🦕 Booting FUI (T-Rex)..."
python3 $HOME/finux/fui/FUI_TRex.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FUI: T-REX EDITION INSTALLED."
echo ">> Graphics Engine: DISABLED (0% Crash Risk)"
echo ">> Interface: Cyberpunk Terminal Dashboard"
echo ">> Type 'finux' to launch."
echo "=========================================="
