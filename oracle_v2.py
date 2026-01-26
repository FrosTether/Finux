cat << 'EOF' > oracle_v2.py
import asyncio
import csv
from kasa import Discover
from datetime import datetime

# --- VIRGO ♍ x1777: OPTIMIZED ENERGY LOG ---
async def log_grid():
    print("🧹 [VIRGO MOON] Optimizing Energy Data...")
    devices = await Discover.discover()
    
    with open('energy_audit.csv', 'a') as f:
        writer = csv.writer(f)
        for ip, dev in devices.items():
            await dev.update()
            if dev.has_emeter:
                # Optimized extraction for the $90.88 budget
                power = dev.emeter_realtime.power
                voltage = dev.emeter_realtime.voltage
                writer.writerow([datetime.now(), dev.alias, f"{power}W", f"{voltage}V"])
                print(f"📊 [LOGGED] {dev.alias}: {power}W cached to audit.")

if __name__ == "__main__":
    asyncio.run(log_grid())
EOF
