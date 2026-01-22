import time
import sys
import random
import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class DealWarRoom:
    def __init__(self):
        self.investor = "Dusan / X Holdings"
        self.deal_size = 23000000.00
        self.status = "PENDING WIRE"
        # 4 Hours left before the deal expires
        self.deadline = datetime.datetime.now() + datetime.timedelta(hours=4)
        
    def refresh_dashboard(self):
        print(f"\n{Fore.RED}🚨 DEAL WAR ROOM: ACTIVE MONITORING")
        print(f"{Fore.WHITE}--------------------------------------------------")
        
        # 1. THE STATUS
        print(f"   PRIMARY INVESTOR: {self.investor}")
        print(f"   AMOUNT:           ${self.deal_size:,.2f}")
        print(f"   STATUS:           {Fore.YELLOW}{self.status} (UNSETTLED)")
        
        # 2. THE COUNTDOWN
        time_left = self.deadline - datetime.datetime.now()
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        print(f"   ALLOCATION LOCK:  {Fore.RED}{hours}H {minutes}M REMAINING")
        
        print(f"{Fore.WHITE}--------------------------------------------------")
        print(f"\n{Fore.CYAN}👀 WAITLIST (SECONDARY BUYERS)")
        
        # 3. THE THREAT (THE QUEUE)
        queue = [
            {"name": "Alphabet (Google M&A)", "offer": "$25M", "status": "VERIFIED FUNDS"},
            {"name": "Andreessen Horowitz",   "offer": "$22M", "status": "DUE DILIGENCE DONE"},
            {"name": "Binance Labs",          "offer": "$24M", "status": "REQUESTING ACCESS"}
        ]
        
        print(f"{Fore.WHITE}{'INVESTOR':<25} {'OFFER':<10} {'STATUS'}")
        print(f"{Fore.WHITE}{'-'*50}")
        
        for buyer in queue:
            time.sleep(0.5)
            # Google gets special highlighting
            color = Fore.GREEN if "Google" in buyer['name'] else Fore.WHITE
            print(f"{color}{buyer['name']:<25} {buyer['offer']:<10} {buyer['status']}")
            
        print(f"\n{Fore.RED}[!] SYSTEM ALERT: If funds are not received by {self.deadline.strftime('%H:%M')},")
        print(f"    Allocation #001 will auto-transfer to: ALPHABET INC.")

    def check_wire(self):
        print(f"\n{Fore.YELLOW}📡 PINGING STRIDE BANK LEDGER...")
        # Simulating a check
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)
        print(f"\n{Fore.RED}❌ NO INBOUND LIQUIDITY DETECTED.")
        print(f"   The window is closing.")

if __name__ == "__main__":
    war_room = DealWarRoom()
    war_room.refresh_dashboard()
    war_room.check_wire()
