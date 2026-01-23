import time
from colorama import Fore, init

init(autoreset=True)

class FrostGarden:
    def __init__(self):
        self.crop_yield = 5000 # Lbs per month
        self.ph_level = 6.0
        self.status = "STABLE"

    def optimize_environment(self):
        print(f"\n{Fore.GREEN}🥬 INITIALIZING THE GARDEN: VERTICAL FARMING OS")
        
        stages = [
            "Adjusting LED Spectrum for Growth Phase",
            "Balancing Nutrient Solution (Nitrogen/Phosphorus)",
            "Checking Air Exchange via Freetown Mesh Sensors",
            "Activating Automated Harvest Robotic Arms"
        ]

        for stage in stages:
            time.sleep(0.7)
            print(f"   [>] {stage}... {Fore.CYAN}[OPTIMIZED]")

        print(f"\n{Fore.WHITE}✨ HARVEST READY: Estimated {self.crop_yield} lbs of Frost Greens.")
        print("   Freetown Food Security: 100%")

if __name__ == "__main__":
    FrostGarden().optimize_environment()
