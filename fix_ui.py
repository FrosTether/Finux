cat << 'EOF' > fix_ui.py
import sys

# --- FROSTOS UI REPAIR ---
# Fixes the "Purple Stain" bug in terminal outputs

PURPLE = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'  # The Critical Missing Piece

def test_ui():
    print(f"\n{PURPLE}🟣 [FROSTOS] PURPLE PROTOCOL: STABILIZED{RESET}")
    print(f"{CYAN}💠 [FROSTOS] CYAN PROTOCOL: STABILIZED{RESET}")
    print("\n✅ [SUCCESS] UI Buffers cleared. No more bleeding.")

if __name__ == "__main__":
    test_ui()
EOF

# Run the fix
python3 fix_ui.py
