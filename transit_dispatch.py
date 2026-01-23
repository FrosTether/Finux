import time
from colorama import Fore, init

init(autoreset=True)

class FreetownTransit:
    def __init__(self):
        self.nodes = ["Monroeville", "Sandusky", "Bellevue", "Norwalk"]
        self.fleet_size = 10

    def request_ride(self, citizen_id, pickup, dropoff):
        print(f"\n{Fore.CYAN}🚖 FREETOWN TRANSIT: RIDE REQUEST")
        print(f"   [AUTH] Verifying Citizenship NFT: {citizen_id[:10]}...")
        time.sleep(0.5)
        
        if pickup in self.nodes and dropoff in self.nodes:
            print(f"   [ROUTE] {pickup} -> {dropoff}")
            print(f"   [STATUS] Dispatching Finux-Drive Unit #04... {Fore.GREEN}[EN ROUTE]")
        else:
            print(f"{Fore.RED}   [ERROR] Destination outside the Diamond Perimeter.")

if __name__ == "__main__":
    FreetownTransit().request_ride("FTZN-JACOB-001", "Monroeville", "Norwalk")
