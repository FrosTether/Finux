import time
import sys
import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from rich.align import Align
from rich.text import Text

console = Console()

def boot_sequence():
    # 1. BIOS / KERNEL INIT
    os.system('clear')
    console.print("[bold white on black] FROID BI0S v4.0.1 | MEM: 64GB | GPU: ADRENO-X [/]")
    time.sleep(0.5)
    
    logs = [
        "[KERNEL] Initializing Frost-Vulkan Driver...",
        "[MEMORY] Allocating 12GB for Shader Cache...",
        "[NETWORK] Pinging Centinet Node (192.168.1.105)... [OK]",
        "[CRYPTO] Syncing Wager Pool (0xWARFARE...888)... [SYNCED]",
        "[SECURITY] Loading FSP-v9 Ghost Anti-Cheat... [ACTIVE]"
    ]
    
    for log in logs:
        console.print(f"[dim green]{log}[/dim]")
        time.sleep(0.3)
    
    time.sleep(1)
    
    # 2. THE SPLASH SCREEN
    os.system('clear')
    
    banner = """
    █████▒██████  ▒█████   ██████ ▄▄▄█████▓█████▓█████▄ 
  ▓██   ▒▓██   ▒ ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▓█   ▀▒██▀ ██▌
  ▒████ ░▒████ ░ ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒▒███  ░██   █▌
  ░▓█▒  ░░▓█▒  ░ ▒██   ██░  ▒   ██▒░ ▓██▓ ░▒▓█  ▄░▓█▄   ▌
  ░▒█░   ░▒█░    ░ ████▓▒░▒██████▒▒  ▒██▒ ░░▒████▒░▒████▓ 
   ▒ ░    ▒ ░    ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░  ░░ ▒░ ░ ▒▒▓  ▒ 
   ░      ░        ░ ▒ ▒░ ░ ░▒  ░ ░    ░    ░ ░  ░ ░ ▒  ▒ 
   ░ ░    ░      ░ ░ ░ ▒  ░  ░  ░    ░        ░    ░ ░  ░ 
                   ░ ░          ░             ░  ░   ░    
                                                   ░      
    """
    console.print(Align.center(Text(banner, style="bold cyan")))
    console.print(Align.center("[ W A R F A R E :   Z E R O   H O U R ]", style="bold white")))
    console.print(Align.center("[ PRESS ANY KEY TO BREACH ]", style="blink yellow"))
    
    # Simulate loading bar
    with console.status("[bold red]Loading Map: THE CITADEL...[/]", spinner="dots"):
        time.sleep(3)

def lobby_screen():
    os.system('clear')
    
    # Header
    console.print(Panel(
        Align.center("[bold red]💀 LOBBY - MATCHMAKING ACTIVE[/]"), 
        style="red",
        subtitle="Server: US-EAST-MANSFIELD"
    ))
    
    # Player Stats
    stats_table = Table(show_header=True, header_style="bold magenta", expand=True)
    stats_table.add_column("OPERATOR", style="cyan")
    stats_table.add_column("RANK", style="yellow")
    stats_table.add_column("K/D", style="green")
    stats_table.add_column("WALLET", style="bold white")
    
    stats_table.add_row("JACOB_FROST [DEV]", "ELITE (Top 1%)", "42.0", "558.65 BTC")
    stats_table.add_row("xX_NoobSlayer_Xx", "Silver IV", "1.2", "0.005 BTC")
    stats_table.add_row("Satoshi_Ghost", "Gold I", "2.8", "1.200 BTC")
    
    console.print(stats_table)
    
    # Match Found Alert
    print("\n")
    console.print("[dim]Searching for opponents...[/dim]")
    time.sleep(2)
    console.print("[bold green]✔ MATCH FOUND![/]")
    console.print("[white]Map:[/white] [red]THE CITADEL (Night Mode)[/]")
    console.print("[white]Wager:[/white] [yellow]0.001 BTC ($89.50)[/]")
    
    print("\n")
    console.print("[bold white on red] >> DEPLOYING IN 3... << [/]")
    time.sleep(1)
    console.print("[bold white on red] >> DEPLOYING IN 2... << [/]")
    time.sleep(1)
    console.print("[bold white on red] >> DEPLOYING IN 1... << [/]")
    time.sleep(1)

if __name__ == "__main__":
    boot_sequence()
    lobby_screen()
