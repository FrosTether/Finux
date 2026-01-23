import hashlib
import json
from rich.console import Console

console = Console()

def verify_block_hash(block):
    """Recalculates a block's hash to ensure data integrity."""
    # Exclude the hash itself from the calculation
    block_contents = {k: v for k, v in block.items() if k != 'hash'}
    content_string = json.dumps(block_contents, sort_keys=True).encode()
    return hashlib.sha256(content_string).hexdigest()

def is_chain_valid(chain):
    """
    Validates the entire blockchain:
    1. Checks if current hash is authentic.
    2. Checks if previous hash matches preceding block.
    """
    for i in range(1, len(chain)):
        current = chain[i]
        previous = chain[i-1]

        # Validation A: Current block's hash is authentic
        if current['hash'] != verify_block_hash(current):
            console.print(f"[bold red]❌ Integrity Error: Block {i} hash has been tampered with![/bold red]")
            return False

        # Validation B: Link to previous block is intact
        if current['previous_hash'] != previous['hash']:
            console.print(f"[bold red]❌ Link Error: Block {i} references an invalid previous hash![/bold red]")
            return False

    console.print("[bold green]✅ Chain Integrity Verified. All Proof-of-Skill records are authentic.[/bold green]")
    return True

if __name__ == "__main__":
    # Example usage: Load your chain from a JSON file
    try:
        with open('frost_chain.json', 'r') as f:
            ledger = json.load(f)
            is_chain_valid(ledger)
    except FileNotFoundError:
        console.print("[yellow]No ledger found. Start mining with Ms Frostman to generate blocks![/yellow]")
