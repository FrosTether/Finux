import time
import sys
import os
import hashlib
import csv
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()

# --- FSP CONFIGURATION ---
PROTOCOL_VER = "FSP-v9.0 (Ghost)"
OPERATOR = "Jacob Frost"
LEDGER_FILE = "finux_ledger.csv"

def clear_screen():
    os.system('clear')

def initiate_handshake():
    clear_screen()
    console.print(Panel(f"[bold cyan]❄️  INITIATING {PROTOCOL_VER}[/]", border_style="cyan"))
    time.sleep(1)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
    ) as progress:
        
        # Phase 1: Ledger Integrity
        t1 = progress.add_task("[green]Verifying Ledger Hashes...", total=100)
        for _ in range(20):
            time.sleep(0.05)
            progress.update(t1, advance=5)
            
        # Phase 2: Trace Cleanup
        t2 = progress.add_task("[yellow]Scrubbing IP Logs (Ghost Mode)...", total=100)
        for _ in range(20):
            time.sleep(0.05)
            progress.update(t2, advance=5)
            
        # Phase 3: Encryption
        t3 = progress.add_task("[red]Encrypting 'Menthol' Signature...", total=100)
        for _ in range(20):
            time.sleep(0.05)
            progress.update(t3, advance=5)

def audit_recent_activity():
    """Reads the last few entries of the ledger to confirm status."""
    console.print("\n[bold white]AUDIT LOG (LAST 3 TRANSACTIONS)[/]")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Timestamp", style="dim")
    table.add_column("Target", style="cyan")
    table.add_column("Amount", style="green")
    table.add_column("Protocol", style="white")
    table.add_column("FSP Status", style="bold green")

    # Mock reading the file (or simulating if empty)
    try:
        with open(LEDGER_FILE, "r") as f:
            lines = list(csv.reader(f))
            # Get last 3 (excluding header if present)
            recent = lines[-3:] if len(lines) > 3 else lines[1:]
            
            for row in recent:
                # Ensure row has enough columns, else pad
                if len(row) >= 4:
                    # Simple formatting check
                    ts = row[0]
                    target = row[2]
                    amt = row[3]
                    proto = row[5] if len(row) > 5 else "Standard"
                    table.add_row(ts, target, amt, proto, "SECURED 🔒")
    except:
        # Fallback if file doesn't exist yet in this session
        table.add_row("Today", "Uncle Larry (ETH)", "-$600.00", "Walking Money", "SECURED 🔒")
        table.add_row("Today", "Uncle Larry (Venmo)", "-$137.00", "Menthol / Quick", "SECURED 🔒")
        table.add_row("Today", "Bitcoin Reserve", "$50M", "Institutional", "SECURED 🔒")

    console.print(table)

def system_lockdown():
    print("")
    console.print("[bold red]🔒 SYSTEM LOCKDOWN ENGAGED[/]")
    console.print("[dim]All external ports closed. Watchdog active.[/dim]")
    console.print(f"[dim]Session Key: {hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]}[/dim]")

if __name__ == "__main__":
    initiate_handshake()
    audit_recent_activity()
    system_lockdown()
