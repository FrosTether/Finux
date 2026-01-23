import time
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.text import Text

console = Console()

def play_audio_segment(lyrics, duration):
    """Simulates the audio track playing."""
    console.print(f"[bold cyan]🎵 AUDIO:[/bold cyan] [italic]\"{lyrics}\"[/italic]")
    time.sleep(duration)

def render_scene(visual_art, caption, color="green"):
    os.system('clear')
    frame = Panel(
        Align.center(visual_art, vertical="middle"),
        title=f"[bold {color}]{caption}[/]",
        border_style=color,
        height=16,
        style="on black"
    )
    console.print(frame)

def campaign_remix_sequence():
    # --- INTRO: THE HOOK ---
    # Audio: "Well it was just a dream... Just a moment ago..."
    
    scene_1 = """
       [bold blue]
          O
         /|\\   <-- [JACOB FROST]
         / \\
       [/]
       
       [bold yellow]★ SHOOTING FOR STARS ★[/]
    """
    render_scene(scene_1, "THE 9TH DISTRICT DREAM", "white")
    play_audio_segment("Well it was just a dream... Just a moment ago...", 2.5)
    
    # --- VERSE 1: THE STRUGGLE ---
    # Audio: "I was up so high... Lookin' down at the sky..."
    
    scene_2 = """
    [bold blue]
          O
         /|\\
         / \\
    [/]
    
    [dim]
    -----------------------------
    [ THE POLITICAL SWAMP ]
    -----------------------------
    [/dim]
    """
    render_scene(scene_2, "LOOKING DOWN ON THE ESTABLISHMENT", "cyan")
    play_audio_segment("I was up so high... Lookin' down at the sky...", 2.5)

    # --- THE PIVOT: QUITTING THE GAME ---
    # Audio: "I'm gonna quit this crazy scene..."
    
    scene_3 = """
    [bold red]
      O      O      O   <-- [THE INCUMBENTS]
     /|\\    /|\\    /|\\
     / \\    / \\    / \\
    [/]
    
        [bold blue]
           O   <-- [WALKING AWAY]
          /|\\
          / \\
        [/]
    """
    render_scene(scene_3, "QUIT THE CRAZY SCENE (WASHINGTON DC)", "red")
    play_audio_segment("But I'm gonna quit this crazy scene...", 3.0)

    # --- CHORUS: THE MOVEMENT ---
    # Audio: "Don't let me fall... They say what goes up..."
    
    scene_4 = """
       [bold blue]
          O
         /|\\
         / \\
       [/]
       
      [bold green] [ B.o.B ] [/]
      (Ballots over Bureaucracy)
      
      [bold yellow] ❂ LIFE  ❂ LIBERTY  ❂ PROPERTY [/]
    """
    render_scene(scene_4, "DON'T LET THE 9TH DISTRICT FALL", "green")
    play_audio_segment("Don't let me fall... Don't let me fall...", 3.0)

    # --- OUTRO: THE SEAL ---
    final_logo = """
    [bold white]
       _______
      |       |
      | FROST |
      | 2026  |
      |_______|
    [/]
    
    [bold cyan]MOGA. MCGA. B.o.B.[/]
    """
    render_scene(final_logo, "VOTE FROST", "white blink")
    play_audio_segment("They say what goes up... must come down.", 2.0)

def viral_blast():
    print("\n")
    console.print(Panel("""
[bold green]🚀 CAMPAIGN AD RENDERED[/]
----------------------------
[white]Track:[/white]   B.o.B - "Don't Let Me Fall" (Remix)
[white]Visual:[/white]  Philosophy of Liberty (Classic)
[white]Status:[/white]  [bold red]UPLOADED TO TIKTOK / SHORTS[/]

[dim]Targeting Demographics: 18-35 (The "Dreamer" Vote)[/dim]
    """, border_style="green"))

if __name__ == "__main__":
    campaign_remix_sequence()
    viral_blast()
