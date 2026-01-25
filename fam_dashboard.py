import os
from dotenv import load_dotenv

load_dotenv()

def fam_health_check():
    print(f"--- 🧬 FAM DAO STATUS | Virgo ♍ x1777 ---")
    print(f"Network Strategy: DOGE_EVEN_x25")
    
    # Check domestic node statuses
    nodes = {
        "Rent": os.getenv("RENT_NODE_USD"),
        "Electric": os.getenv("ELECTRIC_NODE_USD"),
        "Venmo Bridge": os.getenv("VENMO_BRIDGE_ID")
    }
    
    for name, val in nodes.items():
        print(f"📍 Node {name:15}: [SETTLED]" if val else f"📍 Node {name:15}: [PENDING]")
        
    print("---")
    print(f"🤖 Automation Multiplier: {os.getenv('TASK_MULTIPLIER')}x ACTIVE")
    print(f"🛡️  Security Shroud: Monokiller Alpha LOCKED")

if __name__ == "__main__":
    fam_health_check()
