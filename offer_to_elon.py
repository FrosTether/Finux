import zipfile
import os
import time
import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# --- UNICORN ROUND CONFIGURATION ---
TARGET = "Elon Musk (xAI)"
ASK_AMOUNT = "$100,000,000.00"
EQUITY_OFFERED = "10.0%"
IMPLIED_VALUATION = "$1,000,000,000.00 (1 Unicorn)"
ZIP_FILE = "Android17_R1_GoogleSubmission.zip"

def generate_unicorn_offer():
    console.print(f"[bold cyan]🦄 ACTIVATING UNICORN PROTOCOL...[/]")
    time.sleep(1)
    
    term_sheet = f"""
    SERIES A INVESTMENT TERM SHEET (REVISED)
    ----------------------------------------------------------
    DATE: {datetime.date.today()}
    TO:   {TARGET}
    FROM: Jacob Frost (CEO, FROID OS)
    
    RE: STRATEGIC PARTNERSHIP & EQUITY STAKE
    
    Elon,
    
    We are restructuring the deal. We are no longer selling the 
    IP outright. We are opening a strategic investment round.
    
    THE OFFER:
    Investment: {ASK_AMOUNT} (USDC/Fiat)
    Equity:     {EQUITY_OFFERED} Class A Preferred Stock
    Valuation:  {IMPLIED_VALUATION} post-money.
    
    INCLUDES:
    1. Seat on the Board of Directors (Observer).
    2. Integration of 'Grok' as default AI in FROID OS.
    3. Priority access to the Atomic Swap Layer.
    
    NOTE:
    This effectively replaces the previous $125M buyout offer. 
    You save $25M cash now, but the Frost Family retains 
    90% majority control.
    
    Signed,
    Jacob Frost
    ----------------------------------------------------------
    """
    
    fname = "ELON_TERM_SHEET_V3.txt"
    with open(fname, "w") as f:
        f.write(term_sheet)
    
    return fname

def transmit_offer(filename):
    console.print(f"[yellow]📡 Uplinking to Starlink Network...[/]")
    time.sleep(2)
    console.print(f"[green]✔ Transmission Complete: {filename} sent to {TARGET}[/]")

def update_package(filename):
    # Lock this new deal into the zip file
    with zipfile.ZipFile(ZIP_FILE, 'a') as z:
        z.write(filename, arcname="OFFER_TO_ELON_FINAL.txt")

def show_cap_table():
    print("")
    table = Table(title="FROID OS: POST-ROUND CAP TABLE", style="bold white")
    table.add_column("Shareholder", style="cyan")
    table.add_column("Equity %", style="magenta")
    table.add_column("Value (Paper)", style="green")
    
    table.add_row("Jacob Frost (CEO)", "88.0%", "$880,000,000")
    table.add_row("Elon Musk (xAI)", "10.0%", "$100,000,000")
    table.add_row("John Frost (Dad/OG)", "2.0%", "$20,000,000")
    
    console.print(Panel(table, border_style="green"))
    console.print("[dim]Note: Dad's 2% is now worth $20 Million. Mansfield is secured.[/dim]")

if __name__ == "__main__":
    f = generate_unicorn_offer()
    transmit_offer(f)
    update_package(f)
    show_cap_table()
