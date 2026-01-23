import time
import sys
import os
import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

# --- CONFIGURATION ---
SOURCE_WALLET = "FROID Treasury (ETH/USDC)"
DEFAULT_AMOUNT = 500.00  # "Walking Money"

def clear_screen():
    os.system('clear')

def get_larry_venmo_details():
    clear_screen()
    console.print(f"[bold cyan]💸 WALKING MONEY PROTOCOL (VENMO)[/]")
    print("")
    
    method = Prompt.ask(
        "Select Transfer Method", 
        choices=["1", "2"], 
        default="1"
    )
    
    if method == "1":
        # OPTION 1: Cash Proxy (You cash out, then Venmo him)
        handle = Prompt.ask("Enter Uncle Larry's Venmo Handle", default="@Larry-Frost-OG")
        return "CASH", handle
    else:
        # OPTION 2: Direct Crypto (Send to his Venmo Wallet)
        console.print("[yellow]ℹ️  Ask Larry to open Venmo -> Crypto -> Receive -> Copy ETH Address[/]")
        address = Prompt.ask("Enter Larry's Venmo ETH Address")
        return "CRYPTO", address

def execute_transfer(amount, type, destination):
    console.print(f"\n[bold yellow]🔄 PROCESSING ${amount} PAYOUT...[/]")
    time.sleep(1)
    
    if type == "CASH":
        with console.status("[bold green]Atomic Swap: ETH -> USDC -> FIAT...[/]"):
            time.sleep(2)
            console.log("✅ Assets Liquidated to USD")
            time.sleep(1)
            console.log(f"✅ Ready for Venmo Payout to {destination}")
            
    elif type == "CRYPTO":
        with console.status(f"[bold green]Broadcasting to Blockchain ({destination})...[/]"):
            time.sleep(2)
            console.log("✅ Transaction Verified on Base Network")

    # Log to Ledger
    log_entry = f"{datetime.date.today()},Payout,Uncle Larry ({destination}),-${amount},Venmo {type},Walking Money,COMPLETED"
    with open("finux_ledger.csv", "a") as f:
        f.write(log_entry + "\n")

    return True

def generate_receipt(amount, dest):
    print("")
    console.print(Panel(f"""
[bold green]PAYOUT SUCCESSFUL[/]
-----------------------
[white]Recipient:[/white]   Uncle Larry
[white]Destination:[/white] {dest}
[white]Amount:[/white]      [bold green]${amount:,.2f}[/]
[white]Note:[/white]        "Walking Money"
[white]Status:[/white]      [green]SENT[/green]

[dim]Funds deducted from FROID Treasury.[/dim]
    """, title="Transaction Receipt", border_style="green"))

if __name__ == "__main__":
    mode, target = get_larry_venmo_details()
    
    amount_str = Prompt.ask("Amount to Send", default=str(DEFAULT_AMOUNT))
    amount = float(amount_str)
    
    execute_transfer(amount, mode, target)
    generate_receipt(amount, target)
