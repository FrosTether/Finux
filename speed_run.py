import time
import threading
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.align import Align

console = Console()

def market_thread():
    """Thread 1: The Black Market Transaction"""
    time.sleep(0.5)
    console.log("[bold yellow]🛒 MARKET:[/bold yellow] Authorizing Purchase...")
    time.sleep(0.2)
    console.log("[bold yellow]🛒 MARKET:[/bold yellow] -5,000 FC (FrostCoin) Deducted.")
    console.log("[bold yellow]🛒 MARKET:[/bold yellow] Item Crafted: [bold cyan]DIAMOND DESERT EAGLE[/]")
    console.log("[bold yellow]🛒 MARKET:[/bold yellow] [green]✔ ADDED TO LOADOUT[/]")

def game_thread():
    """Thread 2: The Battle Royale Deployment"""
    time.sleep(0.8)
    console.log("[bold red]⚔️  WARFARE:[/bold red] Server Locked: Crypto Farm (NA-East)")
    time.sleep(0.2)
    console.log("[bold red]⚔️  WARFARE:[/bold red] Rendering Map...")
    console.log("[bold red]⚔️  WARFARE:[/bold red] [green]✔ DROPPING IN[/]")

def dual_execution():
    os.system('clear')
    console.print(Panel("[bold white on blue] 🕯️  EXECUTING AT CANDLE SPEED [/]", border_style="blue"))
    
    # Run threads concurrently
    t1 = threading.Thread(target=market_thread)
    t2 = threading.Thread(target=game_thread)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    time.sleep(1)
    
    # THE DROP SCENE
    os.system('clear')
    console.print(Align.center("\n\n"))
    console.print(Align.center("[bold white]DROPPING INTO AREA[/]", style="blink"))
    
    drop_scene = """
           \\
            \\   [ALTITUDE: 5,000 FT]
             \\
           .---.
         /       \\   <-- [PARACHUTE DEPLOYED]
        |    |    |
         \\   |   /
          \\  |  /
           \\ | /
            \\|/
             o
            /|\\   <-- [YOU]
           / | \\
          /  |  \\
             
      [HAND]: [bold cyan]♦️ DIAMOND DEAGLE ♦️[/] (Equipped)
    """
    
    console.print(Align.center(drop_scene, style="bold white"))
    console.print(Panel("[bold green]🔫 WEAPON READY | 💰 SKINS FLASHING | 🎯 TARGETS LIVE[/]", style="green"))

if __name__ == "__main__":
    import os
    dual_execution()
