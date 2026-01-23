import time
import qrcode # Requires: pip install qrcode
from colorama import Fore, init

init(autoreset=True)

class FrpMerchantTerminal:
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id
        self.asset_code = "FRP"
        self.conversion_rate = 1.00 # 1 FRP = 1 USD (Anchored by Stride)

    def create_invoice(self, amount_usd):
        print(f"\n{Fore.CYAN}🛒 GENERATING INVOICE: {self.merchant_id}")
        print(f"{Fore.WHITE}   TOTAL: ${amount_usd:,.2f} USD ({amount_usd} {self.asset_code})")
        
        # Generate Stellar URI / QR Data
        # Format: stellar:pay?destination=MERCHANT_ADDRESS&amount=X&asset_code=FRP
        qr_data = f"stellar:pay?dest={self.merchant_id}&amt={amount_usd}&asset={self.asset_code}"
        
        print(f"   [QR] Generating Secure Payment Matrix...")
        # In a real GUI, this would display the QR on the Handheld screen
        time.sleep(1)
        print(f"{Fore.YELLOW}   [DISPLAY] QR CODE READY FOR SCAN.")
        
        self.await_settlement(amount_usd)

    def await_settlement(self, amount):
        print(f"\n{Fore.WHITE}   📡 MONITORING STELLAR LEDGER...")
        
        # Simulating the Stellar Horizon API Listener
        for i in range(5):
            time.sleep(1)
            sys.stdout.write(f"\r     Checking block visibility... [{'.' * (i+1)}]")
            sys.stdout.flush()
        
        print(f"\n{Fore.GREEN}   ✅ PAYMENT RECEIVED: {amount} {self.asset_code}")
        print(f"{Fore.MAGENTA}   🏦 TRIGGERING FIAT SETTLEMENT TO MERCHANT BANK...")
        time.sleep(0.8)
        print(f"{Fore.GREEN}   [STRIDE] $ {amount:,.2f} USD CLEARANCE SUCCESS.")

if __name__ == "__main__":
    import sys
    terminal = FrpMerchantTerminal("G-FROST-MERCHANT-XYZ-123")
    terminal.create_invoice(45.99) # Example: $45.99 sale
