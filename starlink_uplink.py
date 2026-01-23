import time
from colorama import Fore, init

init(autoreset=True)

class StarlinkUplink:
    def __init__(self):
        self.constellation = "Starlink-G4-2"
        self.encryption = "Laser-Link (Proprietary)"
        self.status = "DISCONNECTED"

    def connect_to_orbit(self):
        print(f"\n{Fore.CYAN}📡 INITIATING STARLINK UPLINK...")
        
        stages = [
            "Scanning for Phased Array Antenna",
            "Acquiring Satellite Handshake",
            "Negotiating Laser-Link Encryption",
            "Bypassing Ground-Based Gateways"
        ]

        for stage in stages:
            time.sleep(0.7)
            print(f"   [>] {stage}... {Fore.GREEN}[OK]")

        self.status = "ORBITAL_CONNECTED"
        print(f"\n{Fore.MAGENTA}🚀 FINUX IS NOW SPACE-BORN.")
        print(f"   LATENCY: 22ms | THROUGHPUT: 350Mbps")
        print(f"   {Fore.WHITE}STATUS: ISP Censorship is now impossible.")

if __name__ == "__main__":
    uplink = StarlinkUplink()
    uplink.connect_to_orbit()
