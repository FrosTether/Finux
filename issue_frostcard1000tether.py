import time
import random
from rich.console import Console
from rich.panel import Panel

console = Console()

def generate_virtual_card():
    console.print("[bold cyan]❄️  GENERATING VIRTUAL FROST CARD...[/]")
    time.sleep(1.5)
    
    # Simulating the generation of a unique tokenized identifier
    card_no = f"4920 {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}"
    cvv = random.randint(100, 999)
    exp = "01/30"
    
    card_art = f"""
    [bold white]FROST PROTOCOL PREPAID[/]
    
    NUMBER: [bold yellow]{card_no}[/]
    EXP: [white]{exp}[/]   CVV: [white]{cvv}[/]
    
    NAME: [bold cyan]JACOB FROST[/]
    STATUS: [bold green]ACTIVE - $1,000.00 USD[/]
    """
    
    console.print(Panel(card_art, border_style="cyan", title="[bold white]VIRTUAL DEBIT[/]", expand=False))

if __name__ == "__main__":
    generate_virtual_card()
