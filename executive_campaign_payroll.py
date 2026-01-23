import time
from rich.console import Console
from rich.table import Table

console = Console()

def process_payroll():
    console.print("[bold red]🗳️  AUTHORIZING CAMPAIGN PAYROLL...[/]")
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Leader", style="white")
    table.add_column("County", style="cyan")
    table.add_column("Status", style="green")
    
    payees = [
        ("Meech", "HQ / Ops", "TRANSFERRED 💸"),
        ("Troy Brown", "Lucas", "TRANSFERRED 💸"),
        ("Kelsee", "Huron", "TRANSFERRED 💸"),
        ("Kyle", "Erie/Ottawa", "TRANSFERRED 💸")
    ]
    
    for name, county, status in payees:
        time.sleep(0.5)
        table.add_row(name, county, status)
        
    console.print(table)
    console.print("\n[bold green]✔ TOTAL ALLOCATION: $800,000 SECURED.[/]")

if __name__ == "__main__":
    process_payroll()
