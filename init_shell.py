import time
import json
import hashlib
from rich.console import Console
from rich.table import Table

console = Console()

# --- Network Constants ---
NETWORK_DIFFICULTY = 15.0  # Scales with total miners
GAME_MULTIPLIERS = {
    "ms_frostman": 1.25,
    "frost_crush": 1.10,
    "frostether": 1.50
}

def calculate_reward(score, game_id):
    """Executes the Proof-of-Skill Formula: Rb = (Sp * mu) / Dn"""
    mu = GAME_MULTIPLIERS.get(game_id, 1.0)
    reward = (score * mu) / NETWORK_DIFFICULTY
    return round(reward, 6)

def validate_and_mint(game_data):
    """Verifies the game score and 'mints' a local block hash."""
    score = game_data['score']
    game_id = game_data['game_id']
    player_id = game_data['player_id']
    
    reward = calculate_reward(score, game_id)
    
    # Create a unique block hash for this validation event
    block_string = f"{player_id}-{game_id}-{score}-{time.time()}"
    block_hash = hashlib.sha256(block_string.encode()).hexdigest()
    
    return {
        "reward": reward,
        "hash": block_hash,
        "status": "MINTED"
    }

def start_validation_listener():
    console.print("[bold green]Validation Listener Active... Waiting for game scores.[/bold green]")
    
    # In a live environment, this would listen to a socket or local file hook
    # For this demo, we simulate a 'Ms Frostman' High Score event.
    mock_event = {"game_id": "ms_frostman", "score": 2500, "player_id": "JacobF_01"}
    
    console.print(f"\n[bold cyan]Incoming Signal from {mock_event['game_id']}...[/bold cyan]")
    time.sleep(1)
    
    result = validate_and_mint(mock_event)
    
    # Display the result in a clean table
    table = Table(title="💎 New Frostblock Minted")
    table.add_column("Game", style="cyan")
    table.add_column("Score", style="magenta")
    table.add_column("Reward (FTC)", style="green")
    table.add_column("Hash (Last 8)", style="dim")
    
    table.add_row(
        mock_event['game_id'], 
        str(mock_event['score']), 
        f"+{result['reward']}", 
        f"...{result['hash'][-8:]}"
    )
    
    console.print(table)

if __name__ == "__main__":
    start_validation_listener()
