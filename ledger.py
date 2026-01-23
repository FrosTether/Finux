import csv
import os
import datetime

# --- CONFIGURATION ---
LEDGER_FILE = "finux_ledger.csv"

def init_ledger():
    """Creates the ledger file if it doesn't exist."""
    if not os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "Recipient", "Amount (USD)", "Method", "Note", "Status"])
        print(f"📁 Created new ledger: {LEDGER_FILE}")

def log_transaction(recipient, amount, method, note):
    """Saves a transaction to the CSV file."""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    entry = [date_str, time_str, recipient, amount, method, note, "COMPLETED"]
    
    with open(LEDGER_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(entry)
    
    print("\n✅ Transaction Recorded Successfully.")
    print(f"   To: {recipient}")
    print(f"   Amt: ${amount}")
    print(f"   Via: {method}")

def view_ledger():
    """Displays recent transactions."""
    if not os.path.exists(LEDGER_FILE):
        print("No ledger file found.")
        return

    print("\n--- RECENT TRANSACTIONS ---")
    with open(LEDGER_FILE, mode='r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        for row in reader:
            print(f"[{row[0]}] Sent ${row[3]} to {row[2]} ({row[4]})")
    print("---------------------------")

# --- INTERACTIVE MENU ---
if __name__ == "__main__":
    init_ledger()
    
    while True:
        print("\n=== FINUX OFF-CHAIN LEDGER ===")
        print("1. Log New Payment")
        print("2. View History")
        print("3. Exit")
        
        choice = input("Select: ")
        
        if choice == "1":
            print("\nENTER DETAILS:")
            r = input("Recipient (e.g., email/user): ")
            a = input("Amount (USD): ")
            m = input("Method (Venmo, CashApp, Wire): ")
            n = input("Note/Memo: ")
            log_transaction(r, a, m, n)
            
        elif choice == "2":
            view_ledger()
            
        elif choice == "3":
            break
