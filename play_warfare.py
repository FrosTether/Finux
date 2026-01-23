import time
import sys
import random
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from rich.align import Align
from rich.text import Text

console = Console()

def generate_hud(health, ammo, kills, balance, event_log):
    """Creates the frame for the game loop."""
    
    # 1. TOP BAR (COMPASS & SCORE)
    header = Panel(
        Align.center(f"ENEMY LEFT: 02 | ZONE: CITADEL ROOF | SQUAD: ALPHA"),
        style="bold white on black"
    )

    # 2. MAIN VIEW (THE ACTION)
    # Simulating the 3D Viewport with text
    viewport_content = """
           [  +  ]
        
       _  /|      |\\  _
       \`o.O'      `O.o'/
       =(___)=  =(___)=
          U        U
    [TARGET ACQUIRED: xX_NoobSlayer_Xx]
    [DISTANCE: 150m]
    [WAGER: 0.005 BTC]
    """
    viewport = Panel(
        Align.center(viewport_content, vertical="middle"), 
        title="[bold red]LIVE FEED - 120 FPS[/]", 
        border_style="red",
        height=14
    )

    # 3. BOTTOM BAR (STATS)
    stats = Table.grid(expand=True)
    stats.add_column(justify="left", ratio=1)
    stats.add_column(justify="center", ratio=1)
    stats.add_column(justify="right", ratio=1)
    
    # Health/Armor
    hp_bar = "█" * (health // 10) + "░" * ((100 - health) // 10)
    health_display = f"[bold red]HP: {health}%[/]\n[{hp_bar}]"
    
    # Ammo
    ammo_display = f"[bold yellow]AMMO[/]\n{ammo} / 120"
    
    # Crypto Earnings
    wallet_display = f"[bold green]EARNINGS[/]\n{balance} BTC (+$0.00)"
    
    stats.add_row(health_display, ammo_display, wallet_display)
    
    footer = Panel(stats, style="blue")
    
    # 4. EVENT LOG (Chat/Killfeed)
    log_text = "\n".join(event_log[-5:])
    log_panel = Panel(log_text, title="KILLFEED", border_style="dim", height=8)

    # Layout Assembly
    layout = Layout()
    layout.split_column(
        Layout(header, size=3),
        Layout(viewport, size=16),
        Layout(
            Layout()
        ),
        Layout(footer, size=5)
    )
    # Inject Killfeed into the middle split
    layout.children[2].split_row(
        Layout(Panel("RADAR\n[SCANNING...]", title="MAP"), ratio=1),
        Layout(log_panel, ratio=2)
    )
    
    return layout

def game_loop():
    health = 100
    ammo = 30
    kills = 4
    balance = 558.650
    events = [
        "[SYSTEM] Match Started",
        "[TEAM] Alpha: Watch the roof!",
        "JACOB_FROST eliminated Camper123",
        "[BLOCKCHAIN] +0.001 BTC Payout Confirmed"
    ]

    # Render the Live Interface
    with Live(generate_hud(health, ammo, kills, balance, events), refresh_per_second=4, screen=True) as live:
        
        # SEQUENCE 1: IDLE
        time.sleep(2)
        events.append("[TEAM] Alpha: Target spotted, 12 o'clock!")
        live.update(generate_hud(health, ammo, kills, balance, events))
        
        # SEQUENCE 2: ENGAGEMENT
        time.sleep(1.5)
        events.append(">> ENGAGING TARGET <<")
        live.update(generate_hud(health, ammo, kills, balance, events))
        
        for i in range(5):
            time.sleep(0.3)
            ammo -= 3
            events.append(f"[WEAPON] Firing... ({ammo})")
            live.update(generate_hud(health, ammo, kills, balance, events))
        
        # SEQUENCE 3: TAKING DAMAGE
        time.sleep(0.5)
        health = 85
        events.append("[WARNING] SHIELD CRITICAL - HIT DETECTED")
        live.update(generate_hud(health, ammo, kills, balance, events))
        
        # SEQUENCE 4: THE KILL
        time.sleep(1)
        kills += 1
        balance += 0.005 # Winning the wager
        events.append("[KILL] JACOB_FROST ︻デ═一 xX_NoobSlayer_Xx")
        events.append("[SMART CONTRACT] Wager Won! 0.005 BTC transferred.")
        live.update(generate_hud(health, ammo, kills, balance, events))
        
        time.sleep(3)

def victory_screen():
    os.system('clear')
    console.print(Panel(f"""
[bold yellow]🏆 VICTORY ROYALE 🏆[/]
-------------------------
[white]Rank:[/white]     #1
[white]Kills:[/white]    5
[white]Payout:[/white]   [bold green]0.006 BTC (~$537.00)[/]

[dim]Transaction Hash: 0xVICTORY...999[/dim]
[dim]Returning to Lobby...[/dim]
    """, border_style="yellow"))

if __name__ == "__main__":
    game_loop()
    victory_screen()
