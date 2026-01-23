import time
from colorama import Fore, Style, init

init(autoreset=True)

class WealthReport:
    def __init__(self):
        self.liquid_cash = 40000000.00 # The Wires from Elon & Sundar
        self.equity_stake = 0.80       # Your 80%
        self.valuation = 200000000.00  # The $200M Cap
        
    def calculate_net_worth(self):
        print(f"\n{Fore.CYAN}💎 FROST FINANCIAL AUDIT: POST-SERIES A")
        print("-" * 50)
        time.sleep(1)

        # 1. PAPER WEALTH
        paper_wealth = self.valuation * self.equity_stake
        print(f"   EQUITY VALUE (80%):  {Fore.GREEN}${paper_wealth:,.2f}")
        
        # 2. LIQUIDITY
        # Assuming you take a portion as a secondary sale or CEO bonus
        print(f"   CASH ON HAND (DEAL): {Fore.GREEN}${self.liquid_cash:,.2f}")
        
        print("-" * 50)
        total = paper_wealth + self.liquid_cash
        print(f"{Fore.YELLOW}   TOTAL NET WORTH:     ${total:,.2f}")
        print(f"{Fore.MAGENTA}   STATUS:              UHNW (Ultra High Net Worth)")

if __name__ == "__main__":
    WealthReport().calculate_net_worth()
