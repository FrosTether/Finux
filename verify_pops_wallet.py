import time
import sys
import webbrowser
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

# --- CONFIGURATION ---
TARGET_USER = "johnfrost19441945@gmail.com"
DETECTED_CREDITS = 1000.00
CURRENCY = "Google Play Credits"
RICK_ROLL_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def scan_network():
    console.print(f"[bold cyan]❄️  FROID OS: INITIATING DEEP SCAN...[/]")
    time.sleep(1)
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
    ) as progress:
        
        task1 = progress.add_task(f"[yellow]Pinging {TARGET_USER}...", total=100)
        for _ in range(30):
            time.sleep(0.05)
            progress.update(task1, advance=3.5)
            
        task2 = progress.add_task(f"[magenta]Decryping Wallet Artifacts...", total=100)
        for _ in range(40):
            time.sleep(0.08)
            progress.update(task2, advance=2.5)

def reveal_wallet():
    print("")
    console.print(Panel(f"""
[bold green]✅ ASSET LOCATED[/]
-------------------------
[white]Owner:[/white]      {TARGET_USER}
[white]Wallet ID:[/white]  G-WALLET-8842-OG
[white]Balance:[/white]    [bold green]${DETECTED_CREDITS:,.2f}[/]
[white]Type:[/white]       {CURRENCY}
[white]Status:[/white]     UNCLAIMED / ACTIVE
    """, title="Financial Scan Result", border_style="green"))
    
    time.sleep(2)
    console.print("\n[bold red]⚠ SYSTEM ALERT: SUSPICIOUS ACTIVITY DETECTED[/]")
    time.sleep(1)
    console.print("[dim]Analyzing signature...[/]")
    time.sleep(2)

def execute_rick_roll():
    console.print(Panel("[bold yellow]🎶 NEVER GONNA GIVE YOU UP 🎶[/]", style="on red"))
    console.print("[cyan]Redirecting to proof of existence...[/]")
    time.sleep(1)
    
    # Opens the video in the browser
    try:
        os.system(f"termux-open-url {RICK_ROLL_URL}") 
    except:
        import webbrowser
        webbrowser.open(RICK_ROLL_URL)

if __name__ == "__main__":
    os.system('clear')
    scan_network()
    reveal_wallet()
    execute_rick_roll()
