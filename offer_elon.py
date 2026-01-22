import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

class TermSheetTransmitter:
    def __init__(self):
        self.target = "ELON_MUSK_PRIVATE_OFFICE"
        self.ask_amount = 21000000.00 # $21 Million
        self.equity_offered = 34.00   # 34 Percent
        self.valuation = self.ask_amount / (self.equity_offered / 100)

    def generate_term_sheet(self):
        print(f"\n{Fore.CYAN}📄 GENERATING SERIES 'A' TERM SHEET...")
        time.sleep(1)
        
        terms = [
            f"ISSUER:       FrosTether Inc. (Finux OS)",
            f"INVESTOR:     Elon Musk / X Holdings",
            f"INVESTMENT:   ${self.ask_amount:,.2f}",
            f"EQUITY STAKE: {self.equity_offered}%",
            f"VALUATION:    ${self.valuation:,.2f} (Post-Money)",
            f"GOVERNANCE:   Board Seat + Veto Rights",
            f"CLOSING:      TBD (30 Days)"
        ]
        
        print("-" * 50)
        for term in terms:
            print(f"{Fore.WHITE}   {term}")
            time.sleep(0.3)
        print("-" * 50)
        
        return terms

    def transmit_offer(self):
        confirm = input(f"\n{Fore.YELLOW}🚀 SEND BINDING OFFER TO ELON MUSK? (Y/N): ")
        
        if confirm.lower() == 'y':
            print(f"\n{Fore.CYAN}📡 ESTABLISHING SECURE UPLINK (STARLINK)...")
            self.loading_bar("ENCRYPTING PACKET")
            
            print(f"{Fore.GREEN}   [✔] UPLINK SECURED.")
            print(f"{Fore.CYAN}   [>] ROUTING TO: {self.target}")
            
            time.sleep(2)
            print(f"\n{Fore.MAGENTA}✨ STATUS: DELIVERED.")
            print(f"{Fore.WHITE}   Ticket #X-DEALFLOW-8842")
            print(f"{Fore.WHITE}   Response Time: ~24-48 Hours")
            
            # Simulated Auto-Reply
            print(f"\n{Fore.CYAN}   [SYSTEM NOTIFICATION] Jared Birchall (Family Office):")
            print(f"{Fore.GREEN}   'Term sheet received, Jacob. Running the numbers on the 34% stake.")
            print(f"{Fore.GREEN}    The valuation aligns with our internal assessment of the OS IP.")
            print(f"{Fore.GREEN}    We will be in touch.'")

        else:
            print(f"{Fore.RED}🚫 OFFER CANCELLED.")

    def loading_bar(self, text):
        for i in range(20):
            sys.stdout.write(f"\r{Fore.CYAN}   {text} [{'='*i}{' '*(20-i)}]")
            sys.stdout.flush()
            time.sleep(0.1)
        print("")

if __name__ == "__main__":
    agent = TermSheetTransmitter()
    agent.generate_term_sheet()
    agent.transmit_offer()
