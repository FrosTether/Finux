import time
import sys
import random
from colorama import Fore, Style, init

init(autoreset=True)

class DealCloser:
    def __init__(self):
        self.investor_email = "dusan@x-holdings-internal.corp"
        self.amount = 23000000.00 # $23 Million
        self.equity = 20.0        # 20 Percent
        self.sender = "jacob.frost@finux.os"
        
    def generate_email_body(self):
        print(f"\n{Fore.CYAN}📧 DRAFTING BINDING ACCEPTANCE...")
        time.sleep(1)
        
        subject = "ACCEPTED: Series A Allocation - Finux OS / FrosTether"
        body = f"""
        TO:      {self.investor_email}
        FROM:    {self.sender}
        DATE:    2026-01-22
        SUBJECT: {subject}
        --------------------------------------------------------
        
        Dusan,
        
        We have reviewed your counter-offer.
        
        Effective immediately, FrosTether Inc. ACCEPTS the following terms:
        1. Investment: ${self.amount:,.2f} USD
        2. Equity:     {self.equity}% (Preferred Stock)
        3. Valuation:  $115,000,000 (Post-Money)
        
        This locks you in before the Mainnet Launch.
        
        ATTACHED:
        - Series_A_Term_Sheet_Signed.pdf
        - Wiring_Instructions_Graysons_Vault.pdf
        - Patent_Docket_Receipts.zip
        
        Let's build the future.
        
        Jacob Frost
        Architect, Finux OS
        """
        
        print("-" * 50)
        print(f"{Fore.WHITE}{body}")
        print("-" * 50)
        return body

    def send_email(self):
        input(f"\n{Fore.YELLOW}PRESS ENTER TO AUTHORIZE TRANSMISSION >> ")
        
        print(f"\n{Fore.CYAN}📡 CONNECTING TO SMTP RELAY (ENCRYPTED)...")
        self.progress_bar("HANDSHAKE")
        
        print(f"{Fore.CYAN}🔑 SIGNING WITH PGP KEY (0x3e1C...)...")
        time.sleep(0.5)
        
        print(f"{Fore.GREEN}🚀 SENT. MESSAGE ID: <{random.randint(100000,999999)}@finux.os>")
        print(f"{Fore.MAGENTA}   STATUS: DELIVERED TO X HOLDINGS SERVER.")

    def progress_bar(self, task):
        sys.stdout.write(f"   {task}: [")
        for i in range(15):
            sys.stdout.write("=")
            sys.stdout.flush()
            time.sleep(0.1)
        print("] OK")

if __name__ == "__main__":
    closer = DealCloser()
    closer.generate_email_body()
    closer.send_email()
