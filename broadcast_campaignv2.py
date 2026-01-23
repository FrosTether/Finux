import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

def deploy_ota_update():
    console.print(Panel("[bold white on red] 📡 BROADCASTING: THE MOGA / ❤️‍🩹 UPDATE [/]", border_style="red"))
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(style="red"),
        TextColumn("{task.percentage:>3.0f}%"),
    ) as progress:
        
        # 1. Pushing Bigg Miami's "Angels and Demons"
        t1 = progress.add_task("[yellow]Injecting 'Angels and Demons' into Lobby...", total=100)
        for _ in range(25):
            time.sleep(0.04)
            progress.update(t1, advance=4)
            
        # 2. Applying ❤️‍🩹 Branding
        t2 = progress.add_task("[magenta]Applying Heart-Mending UI Assets...", total=100)
        for _ in range(20):
            time.sleep(0.05)
            progress.update(t2, advance=5)
            
        # 3. Finalizing Sector Distribution
        t3 = progress.add_task("[white]Syncing with Toledo/Mansfield Nodes...", total=100)
        for _ in range(10):
            time.sleep(0.1)
            progress.update(t3, advance=10)

    console.print("\n[bold green]✔ OTA DEPLOYMENT COMPLETE: THE 9TH DISTRICT IS VESTED.[/]")

if __name__ == "__main__":
    deploy_ota_update()
