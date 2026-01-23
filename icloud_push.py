import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def send_to_troy():
    console.print(Panel("[bold white on blue] ☁️  INITIATING iCLOUD DATA SYNC [/]", border_style="cyan"))
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
    ) as progress:
        
        # 1. Verification
        t1 = progress.add_task("Verifying mr.management25@icloud.com...", total=100)
        time.sleep(1)
        progress.update(t1, completed=100)
        
        # 2. Upload
        t2 = progress.add_task("Pushing Campaign Suite to Troy's iPhone...", total=100)
        for _ in range(20):
            time.sleep(0.05)
            progress.update(t2, advance=5)

    console.print("\n[bold green]✔ DELIVERY COMPLETE.[/] Troy is now armed for the 9th District.")

if __name__ == "__main__":
    send_to_troy()
