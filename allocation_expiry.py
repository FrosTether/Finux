import time
from colorama import Fore, init

init(autoreset=True)

def generate_expiry_notice():
    print(f"{Fore.CYAN}⚖️  GENERATING EXCLUSIVITY REVOCATION WARNING...")
    time.sleep(1)
    
    notice = """
    NOTICE OF ALLOCATION EXPIRY
    ---------------------------
    TO: Dusan (X Holdings)
    RE: Series A Payment Failure
    
    Dusan,
    
    Our banking ledger (Stride Bank) shows NO INBOUND WIRE of $23M.
    
    Per our term sheet, your exclusivity window expires in 4 HOURS.
    
    We have a standing offer from Alphabet Inc. (Google) for $25M.
    If your wire confirmation is not received by EOD, we are legally 
    obligated to void your term sheet and accept the higher bid 
    to satisfy our fiduciary duty.
    
    Do not let this deal slip.
    
    Jacob Frost
    CEO, Finux OS
    """
    
    print("-" * 50)
    print(f"{Fore.WHITE}{notice}")
    print("-" * 50)

if __name__ == "__main__":
    generate_expiry_notice()
