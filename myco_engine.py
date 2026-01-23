import time
from colorama import Fore, init

init(autoreset=True)

class MycoEngine:
    def __init__(self):
        self.strain = "Frost-Omega-01"
        self.precursor_level = 85.0 # Percentage of target saturation
        self.temp_c = 24.2

    def monitor_growth(self):
        print(f"\n{Fore.GREEN}🍄 INITIALIZING MYCO-ENGINE: {self.strain}")
        
        stages = [
            "Sterilizing Substrate with UV-C (Freetown Standard)",
            "Injecting 4-Substituted Indole Precursors",
            "Adjusting Mycelium CO2 levels for Fruiting",
            "Sensing Alkaloid Synthesis via Biosensors"
        ]

        for stage in stages:
            time.sleep(0.8)
            print(f"   [>] {stage}... {Fore.CYAN}[ACTIVE]")

        if self.precursor_level > 80:
            print(f"\n{Fore.WHITE}✨ BIO-SYNTHESIS OPTIMAL: 4-Substituted Alkaloids detected in tissue.")
            print(f"   [STATUS] Harvest estimated in 72 hours.")

if __name__ == "__main__":
    MycoEngine().monitor_growth()
