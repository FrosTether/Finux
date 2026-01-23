import time
import random
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

# --- GAME CONFIGURATION ---
GAME_TITLE = "FROSTED WARFARE: ZERO HOUR"
GENRE = "Tactical FPS / Crypto-Wager"
SERVER_REGIONS = ["NA-East (Mansfield)", "EU-West (London)", "Asia-Pacific (Tokyo)"]
WAGER_POOL_ADDRESS = "0xWARFARE777...888"

def initialize_deployment():
    console.print(Panel(f"[bold red]☢️  INITIATING DEPLOYMENT: {GAME_TITLE}[/]", border_style="red"))
    time.sleep(1)

    with Progress(
        SpinnerColumn("dots", style="red"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(style="red"),
        TextColumn("{task.percentage:>3.0f}%"),
    ) as progress:
        
        # 1. Asset Compilation
        t1 = progress.add_task("[yellow]Compiling Shaders & Textures...", total=100)
        for _ in range(20):
            time.sleep(0.05)
            progress.update(t1, advance=5)
            
        # 2. Smart Contract Deployment
        t2 = progress.add_task("[cyan]Deploying 'Kill-to-Earn' Contracts...", total=100)
        for _ in range(15):
            time.sleep(0.08)
            progress.update(t2, advance=7)
            
        # 3. Server Spin-up
        t3 = progress.add_task("[green]Booting Dedicated Servers...", total=100)
        for region in SERVER_REGIONS:
            progress.console.log(f"[dim]>> {region} Online[/dim]")
            progress.update(t3, advance=33)
            time.sleep(0.3)

def activate_anti_cheat():
    print("")
    console.print("[bold red]🛡️  ACTIVATING FROST-GUARD ANTI-CHEAT[/]")
    console.print("[dim]Policy: ZERO TOLERANCE.[/dim]")
    console.print("[dim]Penalty: Instant Wallet Liquidation.[/dim]")
    time.sleep(1)
    console.print("[green]✔ PROTECTED[/]")

def public_release():
    print("")
    console.print(Panel(f"""
[bold red]🚀 FROSTED WARFARE IS LIVE[/]
-----------------------------
[white]Version:[/white]    1.0 (Alpha)
[white]Map:[/white]        "The Citadel"
[white]Mode:[/white]       High-Stakes Battle Royale
[white]Entry:[/white]      0.001 BTC / Match

[bold yellow]The Lobby is Open.[/bold yellow]
    """, border_style="red"))

if __name__ == "__main__":
    initialize_deployment()
    activate_anti_cheat()
    public_release()
