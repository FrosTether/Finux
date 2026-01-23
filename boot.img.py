import zipfile
import sys
import os

IMAGE = "finux.img"

if not os.path.exists(IMAGE):
    print("❌ System Image not found.")
    sys.exit(1)

print(f"❄️  Mounting {IMAGE}...")

# Read the OS directly from the image into memory
try:
    with zipfile.ZipFile(IMAGE, 'r') as z:
        # Extract to temporary memory and execute
        boot_script = z.read("finux_mobile.py")
        exec(boot_script)
except Exception as e:
    print(f"❌ Boot Error: {e}")
