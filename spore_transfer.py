import time
from colorama import Fore, init

init(autoreset=True)

def execute_secure_transfer():
    print(f"\n{Fore.MAGENTA}🚚 INITIATING SECURE BIO-TRANSFER: MONROEVILLE -> SANDUSKY")
    
    steps = [
        "Cryo-Case Initialization (Temp: -196C)",
        "Spore Retrieval: Frost-Omega-01 (Batch Alpha)",
        "Escort Assigned: Cybertruck-Guard-01 & 02",
        "Nightwatch Perimeter Clearance: [CLEARED]",
        "GPS Routing: Ghost-State Encrypted Path"
    ]

    for step in steps:
        time.sleep(1)
        print(f"   [>] {step}... {Fore.GREEN}[OK]")

    print(f"\n{Fore.CYAN}✅ TRANSFER IN PROGRESS. Estimated Arrival at Sandusky Node: 22:00 HRS.")

if __name__ == "__main__":
    execute_secure_transfer()
