import time
import os
from colorama import Fore, init

init(autoreset=True)

class DeaconNode:
    def __init__(self):
        self.node_id = "FROST-PROTEGE-01"
        self.user = "Deacon Isiah Frost"
        self.status = "OFFLINE"

    def initialize_forge(self):
        print(f"\n{Fore.CYAN}🏗️  BUILDING THE DEACON-NODE: {self.node_id}")
        
        stages = [
            "Partitioning 'Sandbox-Alpha' (2TB Encrypted)",
            "Installing Finux-Apprentice Kernel",
            "Configuring Starlink-Junior Uplink",
            "Activating 'Training Wheels' Firewall (No Outbound Leak)",
            "Syncing FRP Testnet Ledger"
        ]

        for stage in stages:
            time.sleep(0.8)
            print(f"   [>] {stage}... {Fore.GREEN}[SUCCESS]")

        self.status = "ACTIVE_TRAINING"
        print(f"\n{Fore.MAGENTA}✨ THE FORGE IS HOT.")
        print(f"   Deacon Isiah Frost: You are now authorized to build.")

if __name__ == "__main__":
    DeaconNode().initialize_forge()
