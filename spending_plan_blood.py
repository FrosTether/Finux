import csv
import time
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()

# --- FINANCIAL INPUTS ---
TOTAL_LIQUIDITY = 100_000_000.00  # The Cash from Elon
VALUATION = 1_000_000_000.00      # The Company Value (Paper)
SIGNER = "Jacob Frost"

# --- ALLOCATION STRATEGY ---
ALLOCATIONS = [
    {"item": "Bitcoin Strategic Reserve", "amount": 50_000_000, "cat": "Treasury", "note": "Immutable Store of Value"},
    {"item": "FROID Dev / Server Farm",   "amount": 20_000_000, "cat": "OpEx",     "note": "Global Node Expansion"},
    {"item": "Mansfield Innovation Hub",  "amount": 10_000_000, "cat": "Real Est", "note": " revitalization project"},
    {"item": "John Frost (Dad) Cash-Out", "amount":  5_000_000, "cat": "Payout",   "note": "Early Liquidity + Pension"},
    {"item": "Joey Mira's House",         "amount":    150_000, "cat": "Asset",    "note": "Acquisition for Dad"},
    {"item": "Jacob Personal / Fun",      "amount": 14_850_000, "cat": "Personal", "note": "Lambo / Private Island"},
]

def generate_ledger():
    console.print(f"[bold red]🩸 INITIATING BLOOD COVENANT PROTOCOL...[/]")
    time.sleep(1)
    
    filename = "BLOOD_LEDGER_FINAL.csv"
    
    # 1. Create CSV
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Item", "Category", "Amount (USD)", "Notes"])
        
        for alloc in ALLOCATIONS:
            writer.writerow([alloc["item"], alloc["cat"], f"${alloc['amount']:,.2f}", alloc["note"]])
            
    return filename

def sign_in_blood():
    print("")
    console.print(Panel(f"""
[bold red]THE FROST PROTOCOL: SERIES A EXECUTION[/]
-----------------------------------------
[white]Total Cash:[/white]    [green]${TOTAL_LIQUIDITY:,.2f}[/]
[white]Valuation:[/white]     [green]${VALUATION:,.2f}[/]
[white]Investor:[/white]      [cyan]Elon Musk (xAI)[/]
    """, border_style="red"))
    
    time.sleep(1)
    
    # Display the Breakdown
    table = Table(title="ALLOCATION OF FUNDS", style="red")
    table.add_column("Destination", style="white")
    table.add_column("Amount", style="green", justify="right")
    table.add_column("Impact", style="dim")
    
    for alloc in ALLOCATIONS:
        table.add_row(alloc["item"], f"${alloc['amount']:,.0f}", alloc["note"])
        
    console.print(table)
    print("")
    
    # The Blood Signature
    console.print("[bold red]📝 SIGNING CONTRACT...[/]")
    time.sleep(2)
    
    signature = Text(f"x__ {SIGNER} ______", style="bold red on black")
    console.print(signature)
    console.print("[bold red]   (SIGNED IN BLOOD - IRREVOCABLE)[/]")
    
    # Generate Hash
    blood_hash = "0xBLOOD777d8a9c3f2b1e4d5c6f7a8b9c0d1e2f3a4b5"
    console.print(f"\n[dim red]Contract Hash: {blood_hash}[/]")

if __name__ == "__main__":
    generate_ledger()
    sign_in_blood()
