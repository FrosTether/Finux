# 1. Overwrite main.py with the clean code (No Nano required)
cat << 'EOF' > main.py
import os
import time
import sys
import threading
import random

# --- CONFIGURATION ---
VERSION = "FINUX KERNEL v1.2 (Iceland)"
WALLET = "0x5147f68049bdf47fcb778c89544f9f7d1ed7da1d"

def clear_screen():
    os.system('clear')

def print_header():
    print("\033[96m" + "="*50)
    print(f" ❄️  {VERSION}")
    print("="*50 + "\033[0m")

def status_bar():
    while True:
        # Update the top status line every 3 seconds
        cpu_temp = random.randint(35, 42)
        mining_rate = random.uniform(1.2, 1.5)
        sys.stdout.write(f"\r\033[93m[SYSTEM] Temp: {cpu_temp}°C | Hash: {mining_rate:.2f} MH/s | Node: ONLINE\033[0m")
        sys.stdout.flush()
        time.sleep(3)

def main_dashboard():
    clear_screen()
    print_header()
    print(f"\033[92m[+] Identity Confirmed: Jacob Frost")
    print(f"[+] Wallet Connected: {WALLET[:8]}...")
    print(f"[+] Zlib Compression: ACTIVE\033[0m")
    print("-" * 50)
    
    # Start background 'mining' thread simulation
    t = threading.Thread(target=status_bar)
    t.daemon = True
    t.start()
    
    # Simulate Kernel Log
    logs = [
        "Initializing Virgo Kernel Modules...",
        "Mounting File System /dev/frost...",
        "Connecting to FrostCloud Node (Port 5000)...",
        "Syncing Ledger Blocks [##########] 100%",
        "Optimizing Thermal Frequency to 963Hz...",
        "Frost Protocol Network: SECURED."
    ]
    
    for log in logs:
        time.sleep(1.0)
        print(f"\n\033[94m[KERNEL] {log}\033[0m")
        
    print("\n" + "-"*50)
    print("\033[96m SYSTEM READY. AWAITING INPUT.\033[0m")
    
    while True:
        try:
            cmd = input("\nadmin@finux:~$ ")
            if cmd == "help":
                print("Available Commands: status, wallet, mine, exit")
            elif cmd == "wallet":
                print(f"\n[💰] Balance: 100,000,000.00 FNR")
            elif cmd == "mine":
                print("\n[⛏️] Mining job started... (Ctrl+C to stop)")
                time.sleep(2)
            elif cmd == "status":
                print("\n[i] All Systems Nominal.")
            elif cmd == "exit":
                print("Shutting down...")
                break
            else:
                print(f"Command '{cmd}' not found.")
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main_dashboard()
EOF

# 2. Launch it immediately
python3 main.py
