import os
import sys
import time
import threading
import hashlib
import struct
import subprocess
import json
import multiprocessing as mp
import sqlite3

# --- COLOR PALETTE ---
C_CYAN = "\033[38;5;51m"
C_PURPLE = "\033[38;5;135m"
C_GREEN = "\033[38;5;46m"
C_RED = "\033[38;5;196m"
C_GREY = "\033[38;5;240m"
RESET = "\033[0m"
CLEAR = "\033[H\033[J"

# === Minimal FrostChainDB ===
class FrostChainDB:
    def __init__(self, db_path="$HOME/finux/core/frostchain.db"):
        self.db_path = os.path.expanduser(db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS chain
                            (height INTEGER PRIMARY KEY, timestamp REAL, node_id TEXT, hash TEXT, type TEXT)''')
        self.conn.commit()

    def get_height(self):
        self.cur.execute("SELECT MAX(height) FROM chain")
        row = self.cur.fetchone()
        return row[0] if row[0] else 0

    def get_last_hash(self):
        self.cur.execute("SELECT hash FROM chain ORDER BY height DESC LIMIT 1")
        row = self.cur.fetchone()
        return row[0] if row else "GENESIS"

    def add_block(self, height, timestamp, node_id, hash_, type_):
        self.cur.execute("INSERT INTO chain (height, timestamp, node_id, hash, type) VALUES (?, ?, ?, ?, ?)",
                         (height, timestamp, node_id, hash_, type_))
        self.conn.commit()

class DeviceProfile:
    def __init__(self):
        self.cores = mp.cpu_count()
        self.total_mem = self._get_ram()
        self.tier = "UNKNOWN"
        self._classify()

    def _get_ram(self):
        try:
            with open('/proc/meminfo', 'r') as f:
                line = f.readline()
                kb = int(line.split()[1])
                return kb / 1024 / 1024
        except:
            return 2.0

    def _classify(self):
        if self.cores >= 8 and self.total_mem > 6.0:
            self.tier = "APEX (High-Perf)"
            self.ui_refresh = 0.2
        elif self.cores >= 4:
            self.tier = "CORE (Standard)"
            self.ui_refresh = 0.5
        else:
            self.tier = "LITE (Survival)"
            self.ui_refresh = 1.0

class FrostNode:
    def __init__(self):
        self.profile = DeviceProfile()
        self.db = FrostChainDB()
        self.id = "1337G_" + hashlib.sha256(os.urandom(16)).hexdigest()[:6].upper()
        
        self.mining = True
        self.mode = "BOOTING..."
        self.batt_temp = 25.0
        self.batt_level = 100
        
        self.counter = mp.Value('l', 0)  # signed long for big numbers
        self.running = mp.Value('b', True)
        self.processes = []
        
        self.chain_height = self.db.get_height()
        self.last_hash = self.db.get_last_hash()
        self.last_persisted = 0
        
        self.current_rate = 0.0
        self.last_rate_time = time.time()
        self.last_rate_hashes = 0
        
        # Initial environment check for starting workers
        self.target_workers = self.check_environment()  # sets mode + returns workers
        self.start_workers(self.target_workers)

    def worker(self, counter, running):
        while running.value:
            entropy = struct.pack(">Q", time.time_ns())
            hashlib.sha256(entropy).digest()
            with counter.get_lock():
                counter.value += 1

    def start_workers(self, num):
        for _ in range(num):
            p = mp.Process(target=self.worker, args=(self.counter, self.running))
            p.daemon = True
            p.start()
            self.processes.append(p)

    def adjust_workers(self, target):
        current = len(self.processes)
        if target > current:
            self.start_workers(target - current)
        elif target < current:
            for _ in range(current - target):
                p = self.processes.pop()
                p.terminate()
                p.join(timeout=3)

    def check_environment(self):
        try:
            cmd = subprocess.check_output(["termux-battery-status"], stderr=subprocess.DEVNULL)
            data = json.loads(cmd)
            self.batt_temp = data.get('temperature', 25.0) / 10.0  # Termux gives x10
            self.batt_level = data.get('percentage', 100)
            
            if self.batt_temp < 5.0:
                self.mode = "❄️ BLIZZARD (Protect)"
                return 1
            elif self.batt_temp > 42.0:
                self.mode = "🔥 OVERHEAT (Cooling)"
                return max(1, self.profile.cores // 4)
            elif self.batt_level < 15:
                self.mode = "🔋 LOW POWER (Eco)"
                return self.profile.cores // 2
            else:
                self.mode = "31337 G MODE ●"
                return self.profile.cores
        except:
            self.mode = "SENSOR ERROR (Safe)"
            return max(1, self.profile.cores // 2)

    def update_rate(self):
        now = time.time()
        hashes = self.counter.value
        delta_t = now - self.last_rate_time
        if delta_t >= 1.0:
            self.current_rate = (hashes - self.last_rate_hashes) / delta_t
            self.last_rate_time = now
            self.last_rate_hashes = hashes

    def format_rate(self, rate):
        if rate > 1_000_000:
            return f"{rate/1_000_000:.2f} MH/s"
        elif rate > 1_000:
            return f"{rate/1_000:.2f} kH/s"
        else:
            return f"{rate:.2f} Hz"

def monitor_thread(node):
    while node.mining:
        time.sleep(30)  # Check every 30s
        if node.mining:
            target = node.check_environment()
            node.adjust_workers(target)

def render_ui(node):
    # Occasional fresh hash for display
    hash_counter = 0
    
    while node.mining:
        try:
            node.update_rate()
            
            current_hashes = node.counter.value
            current_workers = len(node.processes)
            rate_str = node.format_rate(node.current_rate)
            elite = " (3L1T3)" if node.current_rate > 31337 else ""
            
            # Fresh hash every ~10 updates
            hash_counter += 1
            if hash_counter % 10 == 0:
                entropy = struct.pack(">Q", time.time_ns())
                node.last_hash = hashlib.sha256(entropy).hexdigest()
            
            # Persistence
            if current_hashes // 500_000 > node.last_persisted:
                node.chain_height += 1
                node.db.add_block(node.chain_height, time.time(), node.id, node.last_hash, "ELITE")
                node.last_persisted = current_hashes // 500_000
            
            sys.stdout.write(CLEAR)
            sys.stdout.write(f"{C_PURPLE}╔══════════════════════════════════════════════╗{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {C_CYAN}31337 G PROTOCOL {C_GREY}v13.37{elite}{C_PURPLE}            ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╠══════════════════════════════════════════════╣{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}OPERATOR: {C_GREEN}JACOB FROST [3L1T3]{C_PURPLE}                ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}HARDWARE: {C_GREEN}{node.profile.tier:<26}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}STATUS  : {C_CYAN}{node.mode:<26}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╠══════════════════════════════════════════════╣{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}WORKERS : {C_GREEN}{current_workers}/{node.profile.cores}<{' ' * 23}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}SPEED   : {C_RED}{rate_str:<26}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}HASHES  : {C_GREEN}{current_hashes}{C_PURPLE} {' ' * (26 - len(str(current_hashes))) } ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}HEIGHT  : {C_GREEN}{node.chain_height} Blocks{C_PURPLE}                   ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╠══════════════════════════════════════════════╣{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}LATEST HASH:{C_PURPLE}                                 ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {C_GREY}{node.last_hash[:40]}...{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╚══════════════════════════════════════════════╝{RESET}\n")
            sys.stdout.write(f"\n{C_GREY}>> Godspeed active. [CTRL+C] to Halt.{RESET}\n")
            
            sys.stdout.flush()
            time.sleep(node.profile.ui_refresh)
            
        except KeyboardInterrupt:
            node.mining = False
            break

if __name__ == "__main__":
    node = FrostNode()
    
    # Start monitor thread for dynamic adaptation
    monitor = threading.Thread(target=monitor_thread, args=(node,), daemon=True)
    monitor.start()
    
    try:
        render_ui(node)
    finally:
        # Cleanup
        node.running.value = False
        for p in node.processes[:]:
            p.join(timeout=5)
            if p.is_alive():
                p.terminate()
        print(f"\n{C_RED}>> 31337 G PROTOCOL HALTED. Stay elite.{RESET}")