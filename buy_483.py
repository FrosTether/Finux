import time
import os
import sys
import webbrowser
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# --- MISSION CONFIGURATION ---
BUYER_NAME = "John Frost"
BUYER_TITLE = "Private Investor / OG"
LOCATION = "Bellevue, Ohio"
FUNDING_SOURCE = "FROID Asset Liquidity Layer (Verified)"

# --- REAL ESTATE INTEL (Bellevue - Monroe St Sector) ---
#
BEL_LISTINGS = [
    {"addr": "846 Monroe St, Bellevue, OH", "price": "164,000", "desc": "3 Bed / 2 Bath - Updated Roof (Turnkey)"},
    {"addr": "307 Monroe St, Bellevue, OH", "price": "99,800", "desc": "Fixer-Upper Potential (Estimated Value)"},
    {"addr": "613 Monroe St, Bellevue, OH", "price": "135,900", "desc": "3 Bed / 1 Bath - Old Style"},
    {"addr": "805 Monroe St, Bellevue, OH", "price": "101,400", "desc": "Smaller footprint, affordable cash buy"},
]

def clear_screen():
    os.system('clear')

def select_property():
    console.print(f"[bold cyan]❄️  FROID REAL ESTATE: BELLEVUE SECTOR[/]")
    time.sleep(1)
    
    table = Table(title="TARGETS NEAR MONROE ST", style="white")
    table.add_column("Opt", style="cyan", justify="center")
    table.add_column("Address", style="white")
    table.add_column("Est. Price", style="green")
    table.add_column("Intel", style="yellow")
    
    for i, house in enumerate(BEL_LISTINGS):
        table.add_row(str(i+1), house["addr"], f"${house['price']}", house["desc"])
        
    console.print(table)
    console.print("[dim]Option 0: Enter 'Joey Mira's House' manually if known.[/dim]")
    
    choice = Prompt.ask("SELECT TARGET", choices=["0", "1", "2", "3", "4"], default="0")
    
    if choice == "0":
        addr = Prompt.ask("Enter Street Address", default="Unknown (Joey Mira's House)")
        price = Prompt.ask("Enter Cash Offer", default="85000")
        return addr, price
    else:
        sel = BEL_LISTINGS[int(choice)-1]
        return sel["addr"], sel["price"].replace(",", "")

def generate_proof_of_funds(buyer, amount):
    """Generates a verifiable Proof of Funds document."""
    console.print("[yellow]⚡ Generating FROID Liquidity Certificate...[/]")
    time.sleep(1.5)
    
    html_content = f"""
    <html>
    <body style="font-family: monospace; padding: 40px; border: 2px solid #333;">
        <h1 style="color: #0044cc;">FROID ASSET MANAGEMENT</h1>
        <hr>
        <h3>PROOF OF FUNDS VERIFICATION</h3>
        <p><strong>Date:</strong> {time.strftime("%Y-%m-%d")}</p>
        <p><strong>Account Holder:</strong> {buyer}</p>
        <p><strong>Account Type:</strong> Institutional Crypto-Liquidity (USDC/ETH)</p>
        <br>
        <table style="width: 100%; text-align: left;">
            <tr><th>ASSET CLASS</th><th>BALANCE</th><th>USD VALUE</th></tr>
            <tr><td>USDC (Stablecoin)</td><td>85,400.00</td><td>$85,400.00</td></tr>
            <tr><td>Ethereum (ETH)</td><td>18.45 ETH</td><td>$
