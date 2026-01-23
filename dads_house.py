import time
import os
import sys
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# --- MISSION DATA ---
BUYER_NAME = "John Frost"
BUYER_TITLE = "Private Investor / OG"
FUNDING_SOURCE = "FROID Asset Liquidity Layer (ETH/USDC)"

# --- ACTIVE MANSFIELD OPPORTUNITIES (Scouted Jan 2026) ---
#
ACTIVE_LISTINGS = [
    {"addr": "319 Prescott St, Mansfield, OH", "price": "19,900", "desc": "Fixer-upper near industrial zone"},
    {"addr": "368 W 6th St, Mansfield, OH", "price": "50,000", "desc": "3 Bed / 1 Bath - Old Style"},
    {"addr": "572 France St, Mansfield, OH", "price": "64,900", "desc": "2 Bed / 2 Bath - Move-in ready"},
    {"addr": "781 N McElroy Rd, Mansfield, OH", "price": "59,000", "desc": "3 Bed - Large Lot"},
]

def clear_screen():
    os.system('clear')

def select_target():
    console.print(f"[bold cyan]❄️  FROID REAL ESTATE: MANSFIELD SECTOR[/]")
    time.sleep(1)
    
    table = Table(title="DETECTED OPPORTUNITIES (Under $100k)")
    table.add_column("ID", style="cyan")
    table.add_column("Address", style="white")
    table.add_column("Price (USD)", style="green")
    table.add_column("Notes", style="yellow")
    
    for i, house in enumerate(ACTIVE_LISTINGS):
        table.add_row(str(i+1), house["addr"], f"${house['price']}", house["desc"])
        
    console.print(table)
    console.print("[dim]Or select Option 0 to enter Joey Mira's address manually.[/dim]")
    
    choice = Prompt.ask("SELECT TARGET", choices=["0", "1", "2", "3", "4"], default="0")
    
    if choice == "0":
        address = Prompt.ask("Enter Joey Mira's Address")
        price = Prompt.ask("Enter Offer Price", default="85000")
        return address, price
    else:
        selection = ACTIVE_LISTINGS[int(choice)-1]
        return selection["addr"], selection["price"].replace(",", "")

def generate_offer_packet(address, price):
    clear_screen()
    console.print(f"[bold white on blue] GENERATING CASH OFFER: {address} [/]")
    time.sleep(2)
    
    date_str = time.strftime("%B %d, %Y")
    
    # The Legal Text
    offer_letter = f"""
    LETTER OF INTENT TO PURCHASE
    ------------------------------------------------------------------
    DATE:    {date_str}
    TO:      Owner of Record
    RE:      {address}, Mansfield, OH
    
    BUYER:   {BUYER_NAME}
    OFFER:   ${int(price):,} USD (ALL CASH)
    
    To Whom It May Concern,
    
    I am submitting this formal offer to purchase the property located at 
    {address}.
    
    TERMS OF OFFER:
    1. PURCHASE PRICE: ${int(price):,}.
    2. FINANCING: None. This is a CASH OFFER backed by verified liquid assets.
    3. CLOSING: 14 Days or sooner.
    4. CONDITION: Buying "AS-IS". No repairs requested.
    
    PROOF OF FUNDS:
    Attached is verification of liquidity via FROID Asset Management.
    
    I am ready to sign a purchase agreement immediately.
    
    Respectfully,
    
    {BUYER_NAME}
    {BUYER_TITLE}
    ------------------------------------------------------------------
    """
    
    # Save to file
    filename = "CASH_OFFER_MANSFIELD.txt"
    with open(filename, "w") as f:
        f.write(offer_letter)
        
    return offer_letter, filename

def main():
    clear_screen()
    address, price = select_target()
    
    letter_content, fname = generate_offer_packet(address, price)
    
    console.print(Panel(letter_content, title="PREVIEW", border_style="green"))
    console.print(f"\n[bold yellow]🖨️  PACKET GENERATED: {fname}[/]")
    console.print("[white]INSTRUCTIONS:[/white]")
    console.print("1. Print this file.")
    console.print("2. Have Dad sign it.")
    console.print("3. Deliver to the property owner or listing agent.")

if __name__ == "__main__":
    main()
