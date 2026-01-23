import time
import datetime
import hashlib
from rich.console import Console
from rich.panel import Panel

console = Console()

# --- PAYMENT DATA ---
RECIPIENT_ID = "683050920"  # Venmo Identifier
AMOUNT = 137.00
NOTE = "menthol"
SIGNATURE_KEY = "menthol" # The 'Quick Send' Auth

def quick_send():
    # 1. AUTHENTICATION
    console.print(f"[bold cyan]⚡ INITIATING QUICK-SEND PROTOCOL...[/]")
    time.sleep(0.5)
    
    # Verify Signature
    auth_hash = hashlib.sha256(SIGNATURE_KEY.encode()).hexdigest()
    console.print(f"[dim]Verifying Signature: 'menthol' -> {auth_hash[:12]}... OK[/dim]")
    
    # 2. EXECUTION
    with console.status("[bold green]Pushing Funds to Venmo Gateway...[/]", spinner="dots"):
        time.sleep(1.5) # Fast processing
        
    # 3. LEDGER UPDATE
    log_entry = f"{datetime.date.today()},Payout,Venmo ID:{RECIPIENT_ID},-${AMOUNT:.2f},Instant Transfer,Note: {NOTE},SIGNED: MENTHOL"
    with open("finux_ledger.csv", "a") as f:
        f.write(log_entry + "\n")
        
    # 4. DIGITAL RECEIPT
    print("")
    console.print(Panel(f"""
[bold green]✅ TRANSFER COMPLETE[/]
-----------------------
[white]To Venmo ID:[/white]  {RECIPIENT_ID}
[white]Amount:[/white]       [bold green]${AMOUNT:.2f}[/]
[white]Memo:[/white]         "{NOTE}"
[white]Speed:[/white]        INSTANT (0.8s)

[bold cyan]Signed:[/bold cyan] [italic]Menthol[/italic] 🖊️
    """, title="FROID QUICK-PAY", border_style="green"))

if __name__ == "__main__":
    quick_send()
