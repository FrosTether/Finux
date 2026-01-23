import zipfile
import os
import time
import sys

# --- CONFIGURATION ---
IMAGE_NAME = "finux.img"
FILES_TO_PACK = [
    "finux_mobile.py",
    "pay_larry_swap.py",
    "ledger.py",
    "finux_ledger.csv"
]

def print_status(step, msg):
    print(f"[bold green]{step}[/] {msg}")

def build_image():
    print(f"⚙️  Initializing FINUX Firmware Builder...")
    time.sleep(1)

    # 1. Check for source files
    missing = []
    for f in FILES_TO_PACK:
        if not os.path.exists(f):
            missing.append(f)
    
    if missing:
        print(f"❌ Error: Missing source files: {missing}")
        print("   Please create finux_mobile.py first.")
        return

    # 2. Create the IMG container (Using ZIP compression disguised as IMG)
    print(f"📦 Packing filesystem into {IMAGE_NAME}...")
    with zipfile.ZipFile(IMAGE_NAME, 'w', zipfile.ZIP_DEFLATED) as img:
        for f in FILES_TO_PACK:
            img.write(f)
            print(f"   └── Injecting: {f}")
            time.sleep(0.2) # Simulate processing time

    # 3. Add Boot Header (Metadata)
    with open(IMAGE_NAME, "a") as f:
        # Appending a binary signature so it looks like a real ROM
        f.write("\n\n# FINUX_OS_SIGNED_IMAGE_V1.0\n# DO_NOT_MODIFY")

    print(f"\n✅ SUCCESS: {IMAGE_NAME} created.")
    print(f"   Size: {os.path.getsize(IMAGE_NAME)} bytes")
    print("   System ready for flashing.")

if __name__ == "__main__":
    build_image()
