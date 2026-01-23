import time
from colorama import Fore, init

init(autoreset=True)

class TheSwitzerlandDeal:
    def __init__(self):
        self.valuation = 200000000.00 # $200 Million
        self.total_raise = 40000000.00
        
    def render_allocation(self):
        print(f"\n{Fore.CYAN}⚖️  STRUCTURING 'SWITZERLAND' ROUND (SERIES A)")
        print(f"{Fore.WHITE}   VALUATION: ${self.valuation:,.0f} (Post-Money)")
        print("-" * 60)
        
        allocations = [
            {
                "Investor": "X HOLDINGS (Elon Musk)",
                "Investment": "$20,000,000",
                "Equity": "10.0%",
                "Role": "Hardware Partner (Phone)"
            },
            {
                "Investor": "ALPHABET INC. (Sundar Pichai)",
                "Investment": "$20,000,000",
                "Equity": "10.0%",
                "Role": "Search/AI Partner"
            },
            {
                "Investor": "JACOB FROST (Founder)",
                "Investment": "Intellectual Property",
                "Equity": "80.0%",
                "Role": "Controlling Vote (Super-Shares)"
            }
        ]
        
        print(f"{Fore.YELLOW}{'ENTITY':<30} {'STAKE':<10} {'INVESTMENT':<15}")
        print("-" * 60)
        
        for row in allocations:
            print(f"{Fore.WHITE}{row['Investor']:<30} {row['Equity']:<10} {row['Investment']:<15}")
            time.sleep(0.5)
            
        print("-" * 60)
        print(f"\n{Fore.GREEN}✅ DEAL LOGIC:")
        print(f"   1. X Corp ensures hardware distribution.")
        print(f"   2. Google ensures app compatibility.")
        print(f"   3. FROST retains 80% Control & Audit Rights.")
        print(f"   4. NO SINGLE ENTITY can force a backdoor.")

if __name__ == "__main__":
    deal = TheSwitzerlandDeal()
    deal.render_allocation()
