import time
from colorama import Fore, init

init(autoreset=True)

class SporeVault:
    def __init__(self):
        self.vault_id = "FROST-BIO-VAULT-01"
        self.temp_k = 77.15  # -196 Celsius in Kelvin
        self.nitrogen_level = 98.5  # Percentage
        self.inventory = {
            "Frost-Omega-01": 500, # Viable Spore Prints
            "Frost-Omega-4HO-MET": 250, # Precursor-Optimized
            "Frost-Omega-4AcO": 100 # High-Yield Variant
        }

    def check_vault_integrity(self):
        print(f"\n{Fore.CYAN}❄️  ACCESSING SPORE VAULT: {self.vault_id}")
        
        checks = [
            ("Cryo-Temp Stability", f"{self.temp_k}K", Fore.GREEN),
            ("LN2 Reserve Levels", f"{self.nitrogen_level}%", Fore.GREEN),
            ("Vacuum Seal Status", "NOMINAL", Fore.CYAN),
            ("Biometric Log", "CLEARED - ARCHITECT ONLY", Fore.MAGENTA)
        ]

        for label, val, color in checks:
            time.sleep(0.5)
            print(f"   [CHECK] {label:<20} : {color}{val}")

        print(f"\n{Fore.WHITE}✅ GENETIC HERITAGE SECURED. Inventory verified against Black Box.")

if __name__ == "__main__":
    SporeVault().check_vault_integrity()
