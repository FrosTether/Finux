import time

def process_guest_access(method):
    print("📡 GUEST ACCESS REQUESTED VIA MONROEVILLE MESH")
    
    if method == "FRP_PAYMENT":
        print("   [ACTION] Processing 1.0 FRP Transaction...")
        time.sleep(0.5)
        print("   [STATUS] Payment Verified. Routing to 7-Eleven Op-Ex Fund.")
    else:
        print("   [ACTION] Playing 'Freetown Sovereignty' Educational Loop...")
        time.sleep(1.0)
    
    print("✅ ACCESS GRANTED. Welcome to the Ghost Layer.")

if __name__ == "__main__":
    process_guest_access("FRP_PAYMENT")
