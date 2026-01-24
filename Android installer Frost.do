#!/bin/bash

# ==========================================
# 📱 FROST.DO: NATIVE ANDROID INSTALLER
#    Target: Any Android Device (via Termux)
#    Engine: FUI T-Rex (963 Hz)
#    Features: Background Mining + WakeLock
# ==========================================

echo ">> [ANDROID] Initializing Native Installer..."

# 1. SYSTEM PREP (The Foundation)
# ------------------------------------------
echo ">> [1/4] Updating Android Environment..."
# Stop any existing miners
pkill -f python3
# Update repos and install Python
pkg update -y
pkg install python termux-api -y

# 2. INSTALL MINING KERNEL (The T-Rex Engine)
# ------------------------------------------
echo ">> [2/4] Injecting 963 Hz Kernel..."
mkdir -p "$HOME/finux/fui"
mkdir -p "$HOME/finux/core"

cat <<'EOF' > "$HOME/finux/fui/Native_Miner.py"
import os, sys, time, hashlib, struct, threading

# --- 963 Hz CONFIG ---
FREQ = 963.0
CYCLE = 1.0 / FREQ

# --- ANDROID COLORS ---
CYAN = "\033[38;5;51m"
PURPLE = "\033[38;5;135m"
GREEN = "\033[38;5;46m"
RESET = "\033[0m"
CLEAR = "\033[H\033[J"

class FrostNode:
    def __init__(self):
        # Generate ID from Android Entropy
        self.id = "DROID_" + hashlib.sha256(os.urandom(32)).hexdigest()[:8].upper()
        self.mining = True
        self.hashes = 0
        self.start_t = time.time()

    def mine(self):
        while self.mining:
            # 1. Frequency Wait
            time.sleep(CYCLE)
            
            # 2. Hash
            entropy = struct.pack(">Q", int(time.time_ns()) & 0xFFFFFFFFFFFFFFFF)
            _ = hashlib.sha256(entropy).hexdigest()
            self.hashes += 1

def draw_ui(node):
    while node.mining:
        try:
            uptime = int(time.time() - node.start_t)
            hr = node.hashes / (uptime if uptime > 0 else 1)
            
            sys.stdout.write(CLEAR)
            sys.stdout.write(f"{PURPLE}╔══════════════════════════════════════╗{RESET}\n")
            sys.stdout.write(f"{PURPLE}║ {CYAN}📱 FROST NATIVE MOBILE {PURPLE}            ║{RESET}\n")
            sys.stdout.write(f"{PURPLE}╠══════════════════════════════════════╣{RESET}\n")
            sys.stdout.write(f"{PURPLE}║ {RESET}KERNEL : {GREEN}963 Hz (Optimized){PURPLE}        ║{RESET}\n")
            sys.stdout.write(f"{PURPLE}║ {RESET}ID     : {CYAN}{node.id}{PURPLE}               ║{RESET}\n")
            sys.stdout.write(f"{PURPLE}║ {RESET}SPEED  : {GREEN}{hr:.2f} H/s{PURPLE}                  ║{RESET}\n")
            sys.stdout.write(f"{PURPLE}║ {RESET}UPTIME : {CYAN}{uptime}s{PURPLE}                        ║{RESET}\n")
            sys.stdout.write(f"{PURPLE}╚══════════════════════════════════════╝{RESET}\n")
            sys.stdout.write(f"\n{PURPLE}>> {RESET}System running in background.\n")
            sys.stdout.write(f"{PURPLE}>> {RESET}Press [CTRL+C] to exit.\n")
            sys.stdout.flush()
            time.sleep(0.5)
        except KeyboardInterrupt:
            node.mining = False
            sys.exit()

if __name__ == "__main__":
    node = FrostNode()
    t = threading.Thread(target=node.mine, daemon=True)
    t.start()
    draw_ui(node)
EOF

# 3. CREATE NATIVE LAUNCHER (With WakeLock)
# ------------------------------------------
echo ">> [3/4] Creating 'finux' Command..."

cat <<EOF > "$PREFIX/bin/finux"
#!/bin/bash
# 1. Acquire WakeLock (Keeps CPU running when screen is off)
echo ">> Acquiring Android WakeLock..."
termux-wake-lock

# 2. Launch Miner
python3 $HOME/finux/fui/Native_Miner.py

# 3. Release WakeLock on exit
termux-wake-unlock
echo ">> WakeLock Released."
EOF

# Make it runnable
chmod +x "$PREFIX/bin/finux"

# 4. FINAL CLEANUP & LAUNCH
# ------------------------------------------
echo ">> [4/4] Installation Complete."
echo ""
echo "=========================================="
echo "✅ FROST INSTALLED ON ANDROID."
echo "------------------------------------------"
echo "features:"
echo "  [⚡] WakeLock Active (Mines with screen off)"
echo "  [📱] Native T-Rex Dashboard"
echo "  [❄️] 963 Hz Frequency Kernel"
echo "------------------------------------------"
echo "Type 'finux' to launch now."
echo "=========================================="
