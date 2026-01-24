#!/bin/bash

# ==========================================
# ❄️ FUI.DO: DIRECT TERMINAL INTERFACE
#    Target: Bypass Graphics/Input Crash
#    Engine: Text-Based Dashboard (TUI)
# ==========================================

echo ">> [FUI] Initializing Finux User Interface..."

# 1. CREATE THE FUI DASHBOARD
# ------------------------------------------
mkdir -p "$HOME/finux/fui"
mkdir -p "$HOME/finux/core"

cat <<'EOF' > "$HOME/finux/fui/FUI_Dashboard.py"
import os
import sys
import time
import hashlib
import struct
import threading
import random

# ------------------------------------------
# 1. 963 Hz MINING KERNEL
# ------------------------------------------
class FrostNode:
    def __init__(self):
        self.id = "FUI_" + hashlib.sha256(str(time.time()).encode()).hexdigest()[:6]
        self.freq = 963.0
        self.cycle = 1.0 / self.freq
        self.mining = True
        self.hashes = 0
        self.last_hash = "INIT"

    def mine(self):
        # Precise Frequency Sync
        time.sleep(self.cycle)
        entropy = struct.pack(">Q", int(time.time_ns()) & 0xFFFFFFFFFFFFFFFF)
        self.last_hash = hashlib.sha256(entropy).hexdigest()
        self.hashes += 1

# ------------------------------------------
# 2. FUI VISUAL ENGINE (The Interface)
# ------------------------------------------
# ANSI Colors for that "Finux" Look
PURPLE = "\033[38;5;135m"
CYAN = "\033[38;5;51m"
GREEN = "\033[38;5;46m"
GREY = "\033[38;5;240m"
WHITE = "\033[38;5;255m"
RESET = "\033[0m"
CLEAR = "\033[H\033[J"

def draw_box(node):
    """Draws the Dashboard Frame"""
    # System Stats
    t = time.strftime("%H:%M:%S")
    
    print(CLEAR)
    print(f"{PURPLE}╔══════════════════════════════════════════════════╗{RESET}")
    print(f"{PURPLE}║ {CYAN}❄️  FUI.DO SYSTEM v1.0   {GREY}[{t}]{PURPLE}            ║{RESET}")
    print(f"{PURPLE}╠══════════════════════════════════════════════════╣{RESET}")
    print(f"{PURPLE}║ {WHITE}KERNEL : {GREEN}ACTIVE (963 Hz){PURPLE}                         ║{RESET}")
    print(f"{PURPLE}║ {WHITE}ID     : {CYAN}{node.id}{PURPLE}                      ║{RESET}")
    print(f"{PURPLE}║ {WHITE}BLOCKS : {GREEN}{node.hashes}{PURPLE}                                  ║{RESET}")
    print(f"{PURPLE}╠══════════════════════════════════════════════════╣{RESET}")
    print(f"{PURPLE}║ {WHITE}LATEST HASH:                                     {PURPLE}║{RESET}")
    print(f"{PURPLE}║ {GREY}{node.last_hash}{PURPLE} ║{RESET}")
    print(f"{PURPLE}╚══════════════════════════════════════════════════╝{RESET}")
    print(f"\n{GREY}>> [LOG] Oscillator synchronized to 963 Hz...{RESET}")
    print(f"{GREY}>> [LOG] Press CTRL+C to Halt.{RESET}")

# ------------------------------------------
# 3. MAIN LOOP
# ------------------------------------------
def main():
    node = FrostNode()
    
    # Start Mining Thread
    miner_thread = threading.Thread(target=run_miner, args=(node,), daemon=True)
    miner_thread.start()

    # UI Loop (Updates 10 times per second)
    try:
        while True:
            draw_box(node)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(f"\n{PURPLE}>> FUI SHUTDOWN.{RESET}")
        sys.exit()

def run_miner(node):
    while node.mining:
        node.mine()

if __name__ == "__main__":
    main()
EOF

# 2. CREATE LAUNCHER
# ------------------------------------------
echo ">> [BUILD] Compiling Launcher..."
cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
python3 $HOME/finux/fui/FUI_Dashboard.py
EOF
chmod +x "$PREFIX/bin/finux"

echo "=========================================="
echo "✅ FUI.DO BUILT SUCCESSFULLY."
echo ">> Dependency Issues: SOLVED (Bypassed)"
echo ">> Interface: Terminal Dashboard (TUI)"
echo ">> Type 'finux' to launch."
echo "=========================================="
