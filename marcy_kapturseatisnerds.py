import time
import os
import random
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.table import Table

console = Console()

# --- CAMPAIGN CONFIG ---
CANDIDATE = "JACOB FROST (MOGA/MCGA)"
OPPONENT = "THE INCUMBENT (40-Year Reign)"
DISTRICT = "OHIO 9TH (The Lakefront)"

def inject_campaign_assets():
    console.print(Panel(f"[bold white on red] 🗳️  INITIATING CAMPAIGN MODE: 9TH DISTRICT [/]", border_style="red"))
    time.sleep(1)

    updates = [
        ("[MAP]", "Downloading 'Gerrymander Gulch' (Lake Erie Coast)...", "✔ MAP SET"),
        ("[ENEMY]", "Reskinning 'Zombies' -> 'Lobbyists' & 'Super PACs'...", "✔ ENEMIES UPDATED"),
        ("[LOOT]", "Renaming 'Ammo Crates' -> 'Ballot Harvest Boxes'...", "✔ LOOT SECURED"),
        ("[OBJECTIVE]", "Mission: 'Drain the Swamp' (Toledo Sector)...", "✔ MISSION ACTIVE")
    ]

    for category, action, status in updates:
        console.log(f"[bold blue]{category}:[/] {action}")
        time.sleep(0.4)
        console.log(f"[bold green]{status}[/]")
        time.sleep(0.2)

    console.print("\n[bold red]🇺🇸 CAMPAIGN TRAIL LOADED. POLLS ARE OPEN.[/]")
    time.sleep(1)

def render_debate_stage():
    os.system('clear')
    
    # HUD: CAMPAIGN EDITION
    header = Panel(
        Align.center("[bold white on blue]★ VOTE FROST: 9TH DISTRICT ★[/]"), 
        style="red",
        subtitle="Current Polling: FROST (+45%) | KAPTUR (-12%)"
    )
    
    console.print(header)
    
    # THE SCENE
    console.print(Align.center("\n[bold red]>> FINAL DEBATE BOSS FIGHT <<[/]\n"))
    
    combat_log = [
        ("[MODERATOR]", "Mr. Frost, your rebuttal?"),
        ("[JACOB FROST]", "“We are building the Protocol. It’s huge. It’s digital. And the incumbent can’t even rotate a PDF.”"),
        ("[CROWD]", "CHEERS & APPLAUSE (+500 Votes)"),
        ("[GAMEPLAY]", "You activated Killstreak: [bold red]'FILIBUSTER'[/] (Unlimited Ammo)"),
        ("[COMBAT]", "Opponent Stunned! 'Fact Check' failed."),
        ("[SYSTEM]", "District Flipped! 9th District is now [red]RED[/].")
    ]
    
    for actor, line in combat_log:
        color = "white"
        if actor == "[JACOB FROST]": color = "cyan"
        if actor == "[SYSTEM]": color = "green blink"
        
        console.print(f"[{color}]{actor}:[/] {line}")
        time.sleep(1.5)

def election_night_victory():
    print("\n")
    console.print(Panel(f"""
[bold red]🇺🇸 ELECTION RESULTS 🇺🇸[/]
-------------------------
[white]Winner:[/white]    JACOB FROST (MOGA Party)
[white]District:[/white]  OH-09 (Toledo to Cleveland)
[white]Votes:[/white]     74,000,000 (Record High)
[white]Status:[/white]    [bold green]CONGRESSMAN-ELECT[/]

[dim]New Perk Unlocked: 'Congressional Immunity'[/dim]
    """, border_style="red"))

if __name__ == "__main__":
    inject_campaign_assets()
    render_debate_stage()
    election_night_victory()
