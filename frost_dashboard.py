import time
import os
import random
from colorama import Fore, Style, init

init(autoreset=True)

class FrostCommandDeck:
    def __init__(self):
        self.version = "1.0.0-GOLD"
        self.user = "Jacob Frost"
        self.bank_balance = 40000000.00
        self.fszt_price = 1.24
        
    def render_header(self):
        os.system('clear')
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}❄️  FROST COMMAND DECK | {self.version} | SECURITY: OMEGA")
        print(f"{Fore.CYAN}{'='*60}")
        print(f"{Fore.WHITE}Welcome, {self.user}. System time: {time.strftime('%H:%M:%S')}")

    def get_subsystem_status(self):
        print(f"\n{Fore.YELLOW}[ SUBSYSTEM STATUS ]")
        systems = [
            ("FINUX KERNEL", "v1.3-STABLE", Fore.GREEN),
            ("GHOST LAYER", "TOR/I2P ACTIVE", Fore.GREEN),
            ("CITADEL MESH", "PORT 7444 OPEN", Fore.GREEN),
            ("STARLINK UPLINK", "ORBITAL-6 CONNECTED", Fore.CYAN),
            ("SOVEREIGNTY LOCK", "NO BACKDOORS", Fore.GREEN),
            ("AI EXECUTIVE", "MONITORING TRAFFIC", Fore.MAGENTA)
        ]
        for name, status, color in systems:
            print(f"   {name:<20} : {color}{status}")
            time.sleep(0.1)

    def get_financial_summary(self):
        print(f"\n{Fore.YELLOW}[ FINANCIAL INTELLIGENCE ]")
        print(f"   STRIDE BANK LEDGER : {Fore.GREEN}${self.bank_balance:,.2f} USD")
        print(f"   FSZT MARKET PRICE  : {Fore.CYAN}${self.fszt_price} (+4.2%)")
        print(f"   APP STORE ROYALTY  : {Fore.GREEN}+$32,410.12 (Today)")

    def get_ai_alerts(self):
        print(f"\n{Fore.RED}[ AI EXECUTIVE ALERTS ]")
        alerts = [
            "Verified: $20M wire from X Holdings.",
            "Verified: $20M wire from Alphabet Inc.",
            "Blocked: 420 unauthorized pings from Langley, VA.",
            "Optimization: Starlink switching to Laser-Link 04."
        ]
        for alert in alerts:
            print(f"   {Fore.WHITE}!» {alert}")
            time.sleep(0.1)

    def run(self):
        while True:
            self.render_header()
            self.get_subsystem_status()
            self.get_financial_summary()
            self.get_ai_alerts()
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"{Fore.WHITE}Refreshing in 10s... (Ctrl+C to Exit)")
            time.sleep(10)

if __name__ == "__main__":
    deck = FrostCommandDeck()
    deck.run()
