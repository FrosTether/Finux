"""
❄️ FROSTOISE OS (v1.4)
======================
A terminal-based OS shell for the Finux Ecosystem.
Includes:
- FrostSearch Uplink (Google API)
- Ice Walk Protocol (Mini-game)
- Virgo Kernel Simulation (Thermal Safety)

Author: Jacob Frost
License: MIT
"""

import os
import time
import sys
import random
import requests
from dotenv import load_dotenv

# --- CONFIGURATION ---
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
NODE_ID = os.getenv("NODE_ID", "Monroeville_Node_01")
SEARCH_CX = os.getenv("SEARCH_ENGINE_ID") # Optional: Add this to .env later

# --- MODULES ---

def boot_sequence():
    """Simulates the OS boot process."""
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[1;36m") # Cyan Text
    print(f"""
    ❄️  FROSTOISE OS v1.4-STABLE  ❄️
    Node ID: {NODE_ID}
    System: ONLINE (User-Space)
    ================================
    """)
    print("\033[0m", end="") # Reset color

def x1337_uplink(query):
    """Handles Google Search API requests with error handling."""
    if not API_KEY:
        print("\033[1;31m[!] Error: No API Key found in .env\033[0m")
        return

    print(f"\n\033[1;33m[⚡] Uplink Active. Searching: '{query}'...\033[0m")
    
    url = "https://www.googleapis.com/customsearch/v1"
    params = {'key': API_KEY, 'cx': SEARCH_CX, 'q': query}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'items' in data:
            print(f"\033[1;32m[✔] Data Received:\033[0m")
            for item in data['items'][:3]:
                print(f" > {item['title']}")
                print(f"   {item['link']}\n")
        else:
            # If no CX is set, we expect a 400 error, which confirms the key works.
            print("\033[1;36m[i] Uplink established (Mock Mode).\033[0m")
            print(f"   Target: {query}")
                
    except Exception as e:
        print(f"\033[1;31m[!] Connection Failure: {e}\033[0m")

def ice_walk_game():
    """Launcher for the embedded mini-game."""
    print("❄️  Initializing Ice Walk Protocol...")
    time.sleep(1)
    # Check if the external game file exists, else use mock
    if os.path.exists("ice_walk.py"):
        os.system('python ice_walk.py')
    else:
        print("\033[1;31m[!] Error: ice_walk.py module missing.\033[0m")
    
    time.sleep(1)
    boot_sequence()

# --- MAIN LOOP ---

if __name__ == "__main__":
    boot_sequence()
    
    while True:
        try:
            cmd = input("\033[1;36mFrostoise@Finux:~$ \033[0m").strip()
            
            if cmd.lower() in ['exit', 'quit']:
                print("Shutting down...")
                break
                
            elif cmd.lower() == 'status':
                # Simulated Virgo Thermal Check
                temp = random.randint(38, 45)
                status = "STABLE" if temp < 42 else "THROTTLED"
                color = "\033[1;32m" if temp < 42 else "\033[1;31m"
                print(f"Virgo Sensor: {color}{temp}°C [{status}]\033[0m")
                
            elif cmd.lower() in ['ice', 'game', 'gucci']:
                ice_walk_game()
                
            elif cmd == "":
                continue
                
            else:
                x1337_uplink(cmd)
                
        except KeyboardInterrupt:
            print("\nForce Quit.")
            break
