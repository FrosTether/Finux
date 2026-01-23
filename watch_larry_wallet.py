import time
import sys
from web3 import Web3
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- SURVEILLANCE TARGET ---
TARGET_ADDRESS = "0x951E5F8be239449cE826815ABc7e9E3068996EbC" # Larry
INITIAL_BALANCE_USD = 600.00
# Using a public RPC for read-only access (Base Network)
RPC_URL = "https://mainnet.base.org"

def monitor_wallet():
    console.print(f"[bold red]👁️  WATCHDOG ACTIVE: MONITORING {TARGET_ADDRESS[:6]}...[/]")
    
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    
    # Get initial state
    try:
        balance_wei = w3.eth.get_balance(TARGET_ADDRESS)
        start_balance = w3.from_wei(balance_wei, 'ether')
    except:
        start_balance = 0.1862 # Fallback if RPC fails in simulation
        
    console.print(f"[dim]Initial Balance: {start_balance:.4f} ETH (~$600)[/dim]")
    console.print("[dim]Polling blockchain every 10 seconds...[/dim]")

    # Infinite Loop
    while True:
        try:
            current_wei = w3.eth.get_balance(TARGET_ADDRESS)
            current_balance = w3.from_wei(current_wei, 'ether')
            
            # If balance drops (Money moved OUT)
            if current_balance < start_balance:
                diff = start_balance - current_balance
                alert_user(diff, current_balance)
                start_balance = current_balance # Reset tracker
            
            # Heartbeat (prints a dot every check)
            print(".", end="", flush=True)
            time.sleep(10)
            
        except KeyboardInterrupt:
            console.print("\n[yellow]Watchdog Deactivated.[/]")
            sys.exit()
        except:
            time.sleep(10)

def alert_user(amount_moved, remaining):
    print("\n")
    console.print(Panel(f"""
[bold red blink]🚨 MOVEMENT DETECTED 🚨[/]
---------------------------
[white]Target:[/white] Uncle Larry
[white]Moved:[/white]  [red]-{amount_moved:.4f} ETH[/]
[white]Rem:[/white]    {remaining:.4f} ETH

[bold yellow]HE IS SPENDING IT.[/]
    """, border_style="red"))
    # Play system beep on termux
    print("\a") 

if __name__ == "__main__":
    monitor_wallet()
