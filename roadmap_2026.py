import time
from colorama import Fore, init

init(autoreset=True)

class FinuxRoadmap:
    def __init__(self):
        self.budget = 5000000.00
        self.timeline = {
            "Day 1-30":   "Hardware Prototypes & AMD Vangogh APU Licensing",
            "Day 31-60":  "Deep-Level Kernel Audit & Fed-Backdoor Stress Test",
            "Day 61-90":  "Manufacturing 'Batch Zero' (10,000 Units)",
            "Day 91-100": "Global Launch: finux.tech Genesis Event"
        }

    def print_roadmap(self):
        print(f"\n{Fore.CYAN}🗺️  FINUX GENESIS ROADMAP: THE FIRST $5M")
        print(f"{Fore.WHITE}--------------------------------------------------")
        
        for period, goal in self.timeline.items():
            time.sleep(0.5)
            print(f"{Fore.YELLOW}{period:<12} {Fore.WHITE}{goal}")
            
        print("-" * 50)
        print(f"{Fore.GREEN}✅ ALLOCATION: $5,000,000 LIQUIDITY ASSIGNED.")

if __name__ == "__main__":
    FinuxRoadmap().print_roadmap()
