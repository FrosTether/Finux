import os
import time
import sys
import random
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.layout import Layout
from rich.live import Live

console = Console()

# --- SYSTEM CONFIGURATION ---
OS_NAME = "FROID OS"
BUILD_VER = "v1.0-STABLE (Menthol Signed)"
KERNEL_MODULES = [
    "finux_mobile.py",
    "pay_larry_menthol.py", 
    "fsp_protocol.py",
    "buy_bitcoin_reserve.py",
    "finux_ledger.csv"
]

def clear_screen():
    os.system('clear')

def install_binaries():
    clear_screen()
    console.print(Panel(f"[bold white on blue] ❄️  {OS_NAME} SYSTEM INSTALLER [/]", border_style="blue"))
    time.sleep(1)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
    ) as progress:
        
        # 1. Verify Integrity
        t1 = progress.add_task("[cyan]Verifying Binary Signatures...", total=100)
        for _ in range(15):
            time.sleep(0.05)
            progress.update(t1, advance=7)
            
        # 2. Flash Kernel
        t2 = progress.add_task("[yellow]Flashing Kernel to /system/bin...", total=100)
        for _ in range(20):
            time.sleep(0.08)
            progress.update(t2, advance=5)
            
        # 3. Optimize FSP
        t3 = progress.add_task("[red]Compiling FSP Security Layers...", total=100)
        for _ in range(15):
            time.sleep(0.05)
            progress.update(t3, advance=7)

    console.print("\n[bold green]✔ INSTALLATION COMPLETE[/]")
    time.sleep(1)

def generate_kernel_if_missing():
    """Ensures the OS Dashboard exists before rebooting."""
    if not os.path.exists("finux_mobile.py"):
        console.print("[dim]Rebuilding Core Kernel...[/dim]")
        # (Minimal recovery kernel just in case)
        with open("finux_mobile.py", "w") as f:
            f.write(r"""
import os
import time
from rich.console import Console
from rich.panel import Panel

console = Console()
os.system('clear')
console.print(Panel("[bold cyan]❄️  FROID OS v1.0 ONLINE[/]", style="cyan"))
print("\n[green]System Status:[/green] OPTIMAL")
print("[green]Bitcoin Reserve:[/green] $50M (SECURED)")
print("[green]Menthol Protocol:[/green] ACTIVE")
print("\n[yellow]Ready for command, Mr. Frost.[/yellow]")
            """)

def reboot_sequence():
    console.print("[bold red]⚠ SYSTEM REBOOT INITIATED[/]")
    for i in range(3, 0, -1):
        console.print(f"Rebooting in {i}...")
        time.sleep(1)
    
    # "The Reboot"
    clear_screen()
    
    # Simulated Bootloader Animation
    boot_steps = [
        "Initializing Bootloader...",
        "Loading FROID Kernel...",
        "Mounting /crypto_partition...",
        "Verifying Menthol Signature...",
        "Starting System UI..."
    ]
    
    for step in boot_steps:
        print(f"[BOOT] {step}")
        time.sleep(0.4)
        
    time.sleep(1)
    
    # Launch the OS
    os.system('python finux_mobile.py')

if __name__ == "__main__":
    install_binaries()
    generate_kernel_if_missing()
    reboot_sequence()
