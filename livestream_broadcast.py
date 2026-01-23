import time
import random
import threading
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.live import Live
from rich.table import Table
from rich.align import Align

console = Console()

# --- STREAM CONFIG ---
STREAM_TITLE = "⛽ MAKING WARFARE GREAT AGAIN | $50M GIVEAWAY? | 🇺🇸"
VIEWER_COUNT = 125_482

def generate_chat_reaction():
    """Simulates the chaotic energy of a live chat."""
    users = ["xX_Elon_Xx", "CryptoKing", "LarryTheCableGuy", "MAGA_Tron", "FrostFan1", "DogeCoiner"]
    msgs = [
        "🔥🔥🔥 GAS",
        "🇺🇸 USA USA USA 🇺🇸",
        "IS THAT TRUMP ANNOUNCER?? LMAOO",
        "Wait, is he using the Diamond Deagle?",
        "FROST PROTOCOL ON TOP",
        "SHEEEEESH 🥶",
        "BIGLY WINNING",
        "W STREAM",
        "🚀 TO THE MOON"
    ]
    return f"[bold cyan]{random.choice(users)}:[/bold cyan] {random.choice(msgs)}"

def render_stream_layout(viewers, chat_log, game_event):
    # 1. VIDEO FEED (THE GAME)
    game_screen = Panel(
        Align.center(f"\n\n{game_event}\n\n[bold red]🔴 LIVE[/]  |  [bold white]CAM: JACOB FROST[/]", vertical="middle"),
        title=f"[bold white]{STREAM_TITLE}[/]",
        border_style="red",
        height=12
    )
    
    # 2. CHAT BOX (THE HYPE)
    chat_text = "\n".join(chat_log[-8:])
    chat_panel = Panel(chat_text, title="🔥 SUPER CHAT", border_style="yellow", height=12)
    
    # 3. STATS
    stats = f"[bold red]👁️ {viewers:,}[/] watching  |  [green]💰 Donations: {random.randint(10, 500)} FC[/]"
    
    layout = Layout()
    layout.split_row(
        Layout(game_screen, ratio=3),
        Layout(chat_panel, ratio=1)
    )
    
    return layout, stats

def go_live():
    viewers = VIEWER_COUNT
    chat_log = ["[SYSTEM] STREAM STARTING..."]
    game_events = [
        "DROPPING IN: CRYPTO FARM",
        "LOOTING: TRUMP TOWER",
        "ENGAGING: SQUAD DELTA",
        "WEAPON: THE PATRIOT (GOLD)",
        "KILLSTREAK: ORBITAL STRIKE 🚀",
        "VICTORY ROYALE 🏆"
    ]
    
    console.print(Panel("[bold white on red] 🎥 GOING LIVE IN 3... 2... 1... [/]", border_style="red"))
    time.sleep(1)

    with Live(refresh_per_second=4, screen=True) as live:
        for event in game_events:
            # Simulate Chat Speed
            for _ in range(8):
                chat_log.append(generate_chat_reaction())
                viewers += random.randint(100, 1500)
                
                layout, stats = render_stream_layout(viewers, chat_log, f"[bold white]{event}[/]")
                
                # Combine Layout + Footer Stats
                full_display = Table.grid(expand=True)
                full_display.add_row(layout)
                full_display.add_row(Panel(stats, style="dim"))
                
                live.update(full_display)
                time.sleep(0.3)
            
            # Big Event Pause
            if "VICTORY" in event:
                chat_log.append("[bold red]SYSTEM:[/bold red] 🚨 HYPE TRAIN LEVEL 5 UNLOCKED 🚨")
                time.sleep(2)

if __name__ == "__main__":
    go_live()
