# watcher.py - Fixed Pi Constant
import time
import os

# --- Default Value to Prevent Crash ---
amount_doge = 100  # Default or placeholder value
PI_FROST = 3.14159

def get_freeze_value():
    """Returns the formatted freeze value."""
    freeze_calc = amount_doge * PI_FROST
    return f"{freeze_calc:.5f}"

# This line was crashing because 'amount_doge' wasn't defined above it
print(f"❄️ PI FREEZE: {amount_doge} DOGE -> {get_freeze_value()} FRST (Rate: {PI_FROST})")
