import time
import requests
import sys
import datetime
from web3 import Web3
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- TARGET CONFIGURATION ---
LARRY_ADDRESS = "0x951E5F8be239449cE826815ABc7e9E3068996EbC"
SEND_AMOUNT_USD = 600.00

# --- YOUR WALLET (You must edit this part locally) ---
RPC_URL = "https://mainnet.base.org" # Or Ethereum Mainnet
MY_ADDRESS = "YOUR_WALLET_ADDRESS"   # <--- PASTE YOUR ADDRESS
PRIVATE_KEY = "YOUR_PRIVATE_KEY"     # <--- PASTE YOUR KEY

def get_eth_price():
    """Get live ETH price to calculate exactly $600."""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        data = requests.get(url).json()
        return data['ethereum']['usd']
    except:
        return 3200.00 # Fallback price

def execute_transaction():
    console.print(f"[bold cyan]💸 INITIATING PAYOUT: UNCLE LARRY[/]")
    console.print(f"[yellow]Target Address:[/yellow] {LARRY_ADDRESS}")
    
    # 1. Connect
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        console.print("[red]❌ Connection Failed. Check Internet.[/]")
        return

    # 2. Calculate Amount
    eth_price = get_eth_price()
    eth_amount = SEND_AMOUNT_USD / eth_price
    wei_amount = w3.to_wei(eth_amount, 'ether')
    
    console.print(f"[white]Rate:[/white] ${eth_price:,.2f}/ETH")
    console.print(f"[white]Sending:[/white] {eth_amount:.5f} ETH (= ${SEND_AMOUNT_USD})")
    
    # 3. Confirm
    confirm = input("\nConfirm Send? (y/n): ")
    if confirm.lower() != 'y':
        print("Cancelled.")
        return

    # 4. Build & Sign (The "Real" Part)
    nonce = w3.eth.get_transaction_count(MY_ADDRESS)
    tx = {
        'nonce': nonce,
        'to': LARRY_ADDRESS,
        'value': wei_amount,
        'gas': 21000,
        'gasPrice': w3.eth.gas_price,
        'chainId': 8453 # Base Chain ID (Change to 1 for Ethereum)
    }
    
    # Sign
    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    
    # Send
    console.print("[yellow]🚀 Broadcasting to Blockchain...[/]")
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    # 5. Success Output
    tx_hash_hex = w3.to_hex(tx_hash)
    console.print(Panel(f"""
[bold green]✅ TRANSFER SUCCESSFUL[/]
-----------------------
[white]To:[/white]     Uncle Larry
[white]Addr:[/white]   {LARRY_ADDRESS}
[white]Amt:[/white]    ${SEND_AMOUNT_USD:.2f} ({eth_amount:.4f} ETH)
[white]TX:[/white]     {tx_hash_hex}
    """, border_style="green"))
    
    # 6. Auto-Log to Finux Ledger
    with open("finux_ledger.csv", "a") as f:
        f.write(f"{datetime.date.today()},Payout,{LARRY_ADDRESS},-${SEND_AMOUNT_USD},ETH Transfer,Walking Money,CONFIRMED\n")

if __name__ == "__main__":
    execute_transaction()
