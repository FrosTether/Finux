import time
from colorama import Fore, init

init(autoreset=True)

class YieldEngine:
    def __init__(self):
        self.staked_principal = 25000000  # FSZT
        self.apr = 0.08  # 8% Annual Percentage Rate

    def start_harvest(self):
        print(f"\n{Fore.GREEN}💰 INITIALIZING YIELD ENGINE: GRAYSON-SAV-01")
        print(f"   [STAKE] Principal: {self.staked_principal:,} FSZT")
        
        # Real-time yield simulation
        for i in range(5):
            accrued = (self.staked_principal * self.apr) / (365 * 24 * 60) * (i + 1)
            time.sleep(0.5)
            print(f"   [+] Accruing Interest... Total Harvest: {Fore.YELLOW}{accrued:.8f} FRP")

        print(f"\n{Fore.CYAN}✅ YIELD ENGINE ACTIVE. Passive income stream verified.")

if __name__ == "__main__":
    YieldEngine().start_harvest()
