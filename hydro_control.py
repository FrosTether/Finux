import time
from colorama import Fore, init

init(autoreset=True)

class HydroPlant:
    def __init__(self):
        self.purity_level = 99.99
        self.tank_level = 100000 # Gallons
        self.status = "OFFLINE"

    def initiate_filtration(self):
        print(f"\n{Fore.CYAN}💧 INITIATING PROJECT HYDRO: WATER PURIFICATION")
        
        processes = [
            "Activating Aquifer Pumps",
            "Running Reverse Osmosis Cycle",
            "UV Sterilization Pass",
            "Checking Purity Index (Finux-Audit)"
        ]

        for p in processes:
            time.sleep(0.8)
            print(f"   [>] {p}... {Fore.GREEN}[OK]")

        self.status = "ACTIVE"
        print(f"\n{Fore.BLUE}✨ PURITY SECURED: {self.purity_level}%")
        print("   Freetown is now water-independent.")

if __name__ == "__main__":
    HydroPlant().initiate_filtration()
