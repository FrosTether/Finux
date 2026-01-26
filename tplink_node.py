cat << 'EOF' > tplink_node.py
import asyncio
import os
from kasa import Discover

# --- VIRGO ♍ x1777: ELECTRIC ORACLE ---
# Scans for TP-Link Hardware to audit the $90.88 Bill

async def scan_grid():
    print(f"📡 Scanning Local Grid for TP-Link Nodes...")
    devices = await Discover.discover()
    
    found = False
    for ip, dev in devices.items():
        found = True
        await dev.update()
        print(f"\n🔌 [NODE FOUND]: {dev.alias}")
        print(f"   IP: {ip}")
        print(f"   State: {'🟢 ON' if dev.is_on else '🔴 OFF'}")
        
        # Check for Energy Monitoring (HS110 / KP115 models)
        if dev.has_emeter:
            print(f"   ⚡ Real-Time Load: {dev.emeter_realtime.power:.2f} W")
            print(f"   📊 Monthly Total: {dev.emeter_today:.2f} kWh")
        else:
            print(f"   ⚠️ No Energy Chip (Standard Relay)")

    if not found:
        print("❌ No TP-Link devices found. Ensure they are on the SAME WiFi.")

if __name__ == "__main__":
    asyncio.run(scan_grid())
EOF
