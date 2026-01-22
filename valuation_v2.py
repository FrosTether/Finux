import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

class SeriesA_Update:
    def __init__(self):
        self.company = "FROSTETHER INC."
        self.round = "SERIES A (EXPANSION)"
        
        # SOTP MODEL (Comparables: Playtron, Canonical, DePIN)
        self.divisions = {
            "CORE IP (Finux Kernel v1.3)":          25000000,  # Base OS
            "GAMING (FrostDeck / Steam Fork)":      30000000,  # Comp: Playtron ($50M+)
            "ENTERPRISE (Chimera Hybrid OS)":       25000000,  # Comp: Red Hat / Kali
            "NETWORK (DePIN ARM Nodes)":            15000000,  # Comp: Helium / Render
            "TOKEN TREASURY (25M FSZT @ $1.20)":    30000000   # Liquid Assets
        }

    def present_valuation(self):
        print(f"\n{Fore.CYAN}📈 UPDATING VALUATION MODEL... [v2.0]")
        print(f"{Fore.WHITE}   TARGET: Dusan / X Holdings")
        print("-" * 60)
        time.sleep(1)

        total_val = 0
        
        for sector, value in self.divisions.items():
            # Animated Calculation
            sys.stdout.write(f"   > AUDITING: {sector:<35}")
            time.sleep(0.4)
            print(f"{Fore.GREEN} ${value:,.0f}")
            total_val += value
            time.sleep(0.2)

        print("-" * 60)
        print(f"{Fore.YELLOW}   💰 POST-MONEY VALUATION: ${total_val:,.0f}")
        print(f"{Fore.CYAN}   🚀 MULTIPLIER: 2.4x (Since Seed)")
        
        self.term_sheet_update(total_val)

    def term_sheet_update(self, val):
        # Updating the Ask based on new Valuation
        equity_ask = 20 # Lowering equity ask because value is higher
        investment = val * (equity_ask / 100)
        
        print(f"\n{Fore.WHITE}   [REVISED TERM SHEET]")
        print(f"   ASK:        ${investment:,.0f}")
        print(f"   EQUITY:     {equity_ask}%")
        print(f"   IMPLIED VAL: ${val:,.0f}")

if __name__ == "__main__":
    audit = SeriesA_Update()
    audit.present_valuation()
