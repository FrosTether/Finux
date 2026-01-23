import time
from colorama import Fore, init

init(autoreset=True)

class ProtegeProtocol:
    def __init__(self, name):
        self.protege_name = name
        self.access_level = "Epsilon (Observation Only)"
        
    def initialize_training_node(self):
        print(f"\n{Fore.CYAN}🛡️  INITIALIZING PROTEGE PROTOCOL: {self.protege_name}")
        print(f"   ROLE: Future Architect of the Frost Empire")
        
        modules = [
            "Network Sovereignty 101",
            "FRP Settlement Architecture",
            "Orbital Command Telemetry",
            "AI-Executive Communications"
        ]
        
        for module in modules:
            time.sleep(0.5)
            print(f"   [+] Granting Read-Access to: {module}... {Fore.GREEN}SUCCESS")
            
        print(f"\n{Fore.MAGENTA}✅ DEACON ISIAH FROST IS NOW SYNCED TO THE CITADEL.")

if __name__ == "__main__":
    ProtegeProtocol("Deacon Isiah Frost").initialize_training_node()
