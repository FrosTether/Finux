import time
from colorama import Fore, init

init(autoreset=True)

def update_lab_inventory():
    print(f"\n{Fore.RED}🧪 UPDATING FROST LAB CHEMICAL MANIFEST...")
    
    compounds = {
        "JAM2202": "Synthesized - Alpha Batch",
        "5F-JWH-203": "Fluorination Complete",
        "3-oxo-PCE": "NMDA Assay Pending",
        "Methcathinone": "Purity Check: 99.8%"
    }
    
    for comp, status in compounds.items():
        time.sleep(0.5)
        print(f"   [+] {comp:<15} : {Fore.GREEN}{status}")
        
    print(f"\n{Fore.CYAN}✅ MANIFEST SYNCED WITH THE BLACK BOX.")

if __name__ == "__main__":
    update_lab_inventory()
