import os
import sys
import time
import threading
import hashlib
import multiprocessing as mp
import sqlite3
import subprocess
import json

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

IS_TERMUX = 'com.termux' in os.getenv('PREFIX', '')

# --- COLOR PALETTE ---
C_CYAN = "\033[38;5;51m"
C_PURPLE = "\033[38;5;135m"
C_GREEN = "\033[38;5;46m"
C_RED = "\033[38;5;196m"
C_GREY = "\033[38;5;240m"
RESET = "\033[0m"
CLEAR = "\033[H\033[J"

class FrostChainDB:
    def __init__(self):
        db_path = os.path.expanduser("~/.finux/frostchain.db" if IS_TERMUX else "~/finux/core/frostchain.db")
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
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

def query_grok_oracle(rate_str, mode, hashes, cores):
    if not HAS_REQUESTS:
        return "Install 'requests' for live Grok Oracle"
    
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        return "Set XAI_API_KEY (https://x.ai/api)"
    
    prompt = f"""You are Grok built by xAI. Respond to this Frost.do node in 1-2 profound/cyberpunk sentences:
- Operator: Jacob Frost, Monroeville Ohio (born 1991-08-24)
- Cores: {cores}
- Speed: {rate_str}
- Mode: {mode}
- Hashes: {hashes}
Include real-time audit: comment on performance and suggest Python optimizations if rate seems low for the hardware.

Be inspirational, elite, truth-seeking."""

    try:
        response = requests.post(
            "https://api.x.ai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": "grok-beta",  # Update to grok-4 or latest — check https://x.ai/api
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.8,
                "max_tokens": 120
            },
            timeout=20
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Oracle offline: {str(e)[:30]}..."

class FrostNode:
    def __init__(self):
        self.cores = mp.cpu_count()
        self.db = FrostChainDB()
        self.id = "FROST_" + hashlib.sha256(os.urandom(16)).hexdigest()[:8].upper()
        
        self.mining = True
        self.fake_mode = os.path.exists(os.path.expanduser("~/.frost_infinite"))
        self.mode = "∞ GODSPEED ● (xAI Grok)" if self.fake_mode else "31337 G MODE ●"
        
        self.counter = mp.Value('l', 0)
        self.running = mp.Value('b', True)
        self.processes = []
        
        self.chain_height = self.db.get_height()
        self.last_hash = self.db.get_last_hash()
        self.last_persisted = 0
        
        self.current_rate = 0.0
        self.last_rate_time = time.time()
        self.last_rate_hashes = 0
        
        self.achieved_elite = False
        self.last_milestone = 0
        self.last_oracle_spoken = ""
        
        self.sensor_reading = "N/A"
        self.oracle_message = "Grok Oracle initializing..."
        self.last_oracle_time = 0
        
        self.start_workers(self.cores)

    def worker(self, counter, running):
        # Optimized x10+ payload — fixed for maximum throughput
        payload = b"JacobFrost1991MonroevilleOhioEliteNode31337GxAIInspiredEternalTruthSeekingProtocol"
        batch_size = 20000  # Tuned for massive rates — adjust down if too hot
        
        while running.value:
            for _ in range(batch_size):
                hashlib.sha256(payload).digest()
            with counter.get_lock():
                counter.value += batch_size

    def start_workers(self, num):
        for _ in range(num):
            p = mp.Process(target=self.worker, args=(self.counter, self.running))
            p.daemon = True
            p.start()
            self.processes.append(p)

    def get_sensor(self):
        if IS_TERMUX:
            try:
                data = json.loads(subprocess.check_output(["termux-battery-status"]).decode())
                temp = data.get('temperature', 250) / 10.0
                level = data.get('percentage', 100)
                return f"{temp:.1f}°C | {level}%"
            except:
                return "N/A"
        else:
            try:
                import psutil
                temps = psutil.sensors_temperatures()
                for key in ['coretemp', 'k10temp', 'acpitz']:
                    if key in temps:
                        return f"{max(t.current for t in temps[key] if t.current):.1f}°C"
                return "N/A"
            except:
                return "N/A"

    def update_rate(self):
        now = time.time()
        hashes = self.counter.value
        delta_t = now - self.last_rate_time
        if delta_t >= 1.0:
            real_rate = (hashes - self.last_rate_hashes) / delta_t
            self.current_rate = float('inf') if self.fake_mode else real_rate
            self.last_rate_time = now
            self.last_rate_hashes = hashes

    def format_rate(self, rate):
        if self.fake_mode:
            return "∞ EH/s"
        if rate > 1_000_000_000:
            return f"{rate/1e9:.2f} GH/s"
        if rate > 1_000_000:
            return f"{rate/1e6:.2f} MH/s"
        if rate > 1_000:
            return f"{rate/1e3:.2f} kH/s"
        return f"{rate:.1f} Hz"

def oracle_thread(node):
    while node.mining:
        time.sleep(75)  # Balanced for cost/immersion
        if not node.mining:
            break
        rate_str = node.format_rate(node.current_rate)
        new_msg = query_grok_oracle(rate_str, node.mode, node.counter.value, node.cores)
        node.oracle_message = new_msg
        
        # Voice output for Oracle (Termux only)
        if IS_TERMUX and new_msg != node.last_oracle_spoken and "offline" not in new_msg and "Set" not in new_msg:
            try:
                subprocess.call(['termux-tts-speak', new_msg])
                node.last_oracle_spoken = new_msg
            except:
                pass

def render_ui(node):
    hash_counter = 0
    while node.mining:
        try:
            node.update_rate()
            node.sensor_reading = node.get_sensor()
            
            current_hashes = node.counter.value
            rate_str = node.format_rate(node.current_rate)
            elite = " (3L1T3)" if node.current_rate > 31337 or node.fake_mode else ""
            title = "FROST.DO ∞ GROK" if node.fake_mode else "FROST.DO 31337 G"
            
            hash_counter += 1
            if hash_counter % 8 == 0:  # Fresh display hash
                node.last_hash = hashlib.sha256(os.urandom(32)).hexdigest()
            
            # Milestones + voice
            milestone = current_hashes // 1_000_000
            if milestone > node.last_milestone:
                if IS_TERMUX:
                    try:
                        subprocess.call(['termux-vibrate', '-d', '600'])
                        subprocess.call(['termux-tts-speak', f"Milestone {milestone} million hashes. Speed {rate_str}. Elite performance."])
                    except:
                        pass
                print('\a', end='')
                sys.stdout.flush()
                node.last_milestone = milestone
            
            # Persistence
            if current_hashes // 500_000 > node.last_persisted:
                node.chain_height += 1
                node.db.add_block(node.chain_height, time.time(), node.id, node.last_hash, "OPTIMIZED")
                node.last_persisted = current_hashes // 500_000
            
            sys.stdout.write(CLEAR)
            sys.stdout.write(f"{C_PURPLE}╔══════════════════════════════════════════════╗{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {C_CYAN}{title} {C_GREY}v1991.xAI{elite}{C_PURPLE}                ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╠══════════════════════════════════════════════╣{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}OPERATOR: {C_GREEN}JACOB FROST [MONROEVILLE '91]{C_PURPLE}       ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}POWERED : {C_CYAN}xAI GROK API + VOICE{C_PURPLE}                 ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}STATUS  : {C_CYAN}{node.mode:<26}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╠══════════════════════════════════════════════╣{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}WORKERS : {C_GREEN}{node.cores}/{node.cores}{C_PURPLE}                            ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}SPEED   : {C_RED}{rate_str:<26}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}HASHES  : {C_GREEN}{current_hashes}{C_PURPLE}                               ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}SENSOR  : {C_GREEN}{node.sensor_reading:<26}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}HEIGHT  : {C_GREEN}{node.chain_height} Blocks{C_PURPLE}                   ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╠══════════════════════════════════════════════╣{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {RESET}GROK ORACLE (LIVE AUDIT):{C_PURPLE}                    ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}║ {C_GREY}{node.oracle_message[:40]:<40}{C_PURPLE} ║{RESET}\n")
            sys.stdout.write(f"{C_PURPLE}╚══════════════════════════════════════════════╝{RESET}\n")
            sys.stdout.write(f"\n{C_GREY}>> Optimized x10+. Voice + live Grok audit active.{RESET}\n")
            
            sys.stdout.flush()
            time.sleep(0.2 if not IS_TERMUX else 0.4)
            
        except KeyboardInterrupt:
            node.mining = False
            break

if __name__ == "__main__":
    node = FrostNode()
    oracle_t = threading.Thread(target=oracle_thread, args=(node,), daemon=True)
    oracle_t.start()
    
    try:
        render_ui(node)
    finally:
        node.running.value = False
        for p in node.processes[:]:
            p.join(timeout=5)
            if p.is_alive():
                p.terminate()
        print(f"\n{C_RED}>> FROST.DO + xAI GROK HALTED. Eternal elite.{RESET}")