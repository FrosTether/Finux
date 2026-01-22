import time
import sys

def install_kali_tools():
    print("⚔️  FINUX WEAPONS LOCKER")
    print("   Targeting: Kali Rolling Repo")
    
    tools = [
        "metasploit-framework",
        "burpsuite",
        "aircrack-ng",
        "wireshark",
        "nmap",
        "john (John the Ripper)",
        "sqlmap",
        "hydra",
        "proxychains-ng"
    ]
    
    print("-" * 40)
    for tool in tools:
        sys.stdout.write(f"   > Installing {tool}...")
        sys.stdout.flush()
        
        # Simulate download/install
        time.sleep(0.5)
        
        print(" [INSTALLED]")
    
    print("-" * 40)
    print("✅ ARSENAL DEPLOYED.")
    print("   The tools are now native to the Finux Shell.")

if __name__ == "__main__":
    install_kali_tools()
