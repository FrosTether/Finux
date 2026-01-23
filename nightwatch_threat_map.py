import time

def scan_perimeter():
    print("🛰️  NIGHTWATCH: SYNCING DEFENSE ASSETS...")
    
    nodes = ["Drone-Sentinel-01", "Cybertruck-Guard-03", "Mesh-Gateway-07"]
    
    for node in nodes:
        print(f"   [+] Handshake with {node}... {Fore.GREEN}ENCRYPTED")
        time.sleep(0.4)
    
    print("\n🕵️  THREAT SCANNING ACTIVE (360° RADAR)")
    # Simulation: Detecting an unauthorized vehicle near the 7-Eleven
    threat_detected = False
    
    if threat_detected:
        print(f"{Fore.RED}🚨 ALERT: UNAUTHORIZED SIGNAL DETECTED AT SECTOR 4.")
        print("   [ACTION] Dispatching Drone-Sentinel-01 for ID.")
    else:
        print(f"{Fore.GREEN}✅ STATUS: FREETOWN PERIMETER CLEAR.")

if __name__ == "__main__":
    scan_perimeter()
