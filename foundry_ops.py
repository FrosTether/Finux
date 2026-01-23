import time
from colorama import Fore, init

init(autoreset=True)

class FrostFoundry:
    def __init__(self):
        self.materials = {"Titanium_Powder": 500, "Carbon_Fiber": 200, "Polymer": 1000}
        self.status = "IDLE"

    def fabricate_part(self, part_name, material):
        print(f"\n{Fore.YELLOW}🛠️  INITIATING FOUNDRY FABRICATION: {part_name}")
        
        if self.materials.get(material, 0) > 0:
            steps = [
                "Loading CAD Blueprint from Black Box",
                f"Calibrating Laser for {material} Sintering",
                "Executing Precision Fabrication",
                "Post-Processing & Heat Treatment"
            ]
            for step in steps:
                time.sleep(1)
                print(f"   [>] {step}... {Fore.GREEN}[COMPLETE]")
            
            self.materials[material] -= 10
            print(f"\n{Fore.CYAN}✅ PART COMPLETED: {part_name} is ready for assembly.")
        else:
            print(f"{Fore.RED}❌ ERROR: Insufficient {material} inventory.")

if __name__ == "__main__":
    FrostFoundry().fabricate_part("Cybertruck_Armor_V2", "Titanium_Powder")
