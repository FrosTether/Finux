import time
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.text import Text

console = Console()

def update_enemy_metadata():
    console.print(Panel(f"[bold white on red] 🎯 TARGET LOCKED: THE PELOSI CLONE [/]", border_style="red"))
    time.sleep(1)
    
    updates = [
        ("[GAME DATA]", "Renaming 'Boss_Kaptur' -> 'The_Nancy_of_Ohio'...", "✔ ASSET RENAMED"),
        ("[NARRATIVE]", "Syncing Voting Record (100% Pelosi Alignment)...", "✔ DATA MERGED"),
        ("[AUDIO]", "Injecting Soundbite: 'We have to pass the bill to find out...'", "✔ AUDIO LOOPED")
    ]
    
    for category, action, status in updates:
        console.log(f"[bold blue]{category}:[/] {action}")
        time.sleep(0.4)
        console.log(f"[bold green]{status}[/]")

def render_attack_ad():
    os.system('clear')
    
    # SCENE 1: THE COMPARISON
    # Philosophy of Liberty Style
    
    comparison_frame = """
    [bold red]
       O               O
      /|\\             /|\\
      / \\             / \\
    [/]
    
    [bold white]   DC NANCY      OHIO NANCY   [/]
    [dim]   (Original)      (The Clone)   [/dim]
    """
    
    console.print(Panel(
        Align.center(comparison_frame, vertical="middle"),
        title="[bold red]SPOT THE DIFFERENCE?[/]",
        border_style="red",
        height=14,
        style="on black"
    ))
    
    time.sleep(2.5)
    
    # SCENE 2: THE VOTING RECORD (The "100%" Stamp)
    console.print(Align.center("\n[bold yellow]>> ANALYZING VOTING RECORD <<[/]\n"))
    time.sleep(1)
    
    stamp = """
    [bold red]
      _____________
     |             |
     |  100% SAME  |
     |_____________|
    [/]
    """
    
    console.print(Panel(
        Align.center(stamp, vertical="middle"),
        title="[bold white]THE TRUTH[/]",
        subtitle="She isn't representing Toledo. She's representing San Francisco.",
        border_style="yellow",
        style="on black"
    ))
    
    time.sleep(2.5)
    
    # SCENE 3: THE SOLUTION (FROST)
    os.system('clear')
    
    solution_frame = """
       [bold blue]
          O
         /|\\  <-- [JACOB FROST]
         / \\
       [/]
       
    [bold green]OHIO FIRST. NOT PELOSI FIRST.[/]
    """
    
    console.print(Panel(
        Align.center(solution_frame, vertical="middle"),
        title="[bold blue]THE MOGA CHOICE[/]",
        border_style="blue",
        height=12,
        style="on black"
    ))

def broadcast_to_9th_district():
    print("\n")
    console.print(Panel("""
[bold red]📢 ALERT: OPPOSITION RESEARCH DROP[/]
-------------------------------------
[white]Headline:[/white]  "Meet the Nancy Pelosi of Ohio."
[white]Reach:[/white]     Targeting every TV screen in Sandusky & Toledo.
[white]Game:[/white]      New Boss Fight: "The Gavel Snatcher."

[dim]Status: TRENDING #1 in Ohio[/dim]
    """, border_style="red"))

if __name__ == "__main__":
    update_enemy_metadata()
    render_attack_ad()
    broadcast_to_9th_district()
