import pygame
import random
import requests
import threading
import time
import json

# --- CONFIGURATION: CONNECT TO YOUR LOCAL NODE ---
RPC_URL = "http://127.0.0.1:8070/json_rpc"  # Update this to your Finux/Frostcoin walletd port
RPC_USER = "user"
RPC_PASSWORD = "password"

# --- GAME SETTINGS ---
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
GRID_SIZE = 8
TILE_SIZE = 60
MARGIN = 10
OFFSET_Y = 150  # Space for the Wallet UI at the top

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FROST_BLUE = (0, 191, 255)
DEEP_ICE = (0, 105, 180)
UI_BG = (30, 30, 40)
TEXT_COLOR = (200, 200, 200)

# GEM TYPES (Simple Colors for prototype, replace with Ice assets)
GEM_COLORS = [
    (255, 0, 0),    # Red Fire (Melt)
    (0, 255, 0),    # Green Earth
    (0, 0, 255),    # Blue Ice (Frost)
    (255, 255, 0),  # Yellow Sun
    (128, 0, 128),  # Purple Void
    (0, 255, 255)   # Cyan Diamond
]

class FrostWallet:
    """Handles the connection to the Frostcoin Wallet Daemon (Threaded)"""
    def __init__(self):
        self.balance = "0.0000 FRST"
        self.status = "Disconnect"
        self.lock = threading.Lock()
        self.running = True
        self.thread = threading.Thread(target=self.poll_wallet)
        self.thread.start()

    def get_balance_rpc(self):
        """Standard JSON-RPC call for Monero/CryptoNote or Bitcoin style wallets"""
        payload = {
            "jsonrpc": "2.0",
            "id": "0",
            "method": "get_balance", # Change to "getbalance" if using Bitcoin-fork
            "params": {"account_index": 0} # Adjust params based on your specific API
        }
        try:
            response = requests.post(
                RPC_URL, 
                data=json.dumps(payload), 
                headers={'content-type': 'application/json'},
                auth=(RPC_USER, RPC_PASSWORD),
                timeout=2
            )
            data = response.json()
            
            # Parsing logic (Generic)
            if 'result' in data:
                # Handle atomic units if necessary (e.g., divide by 1e8)
                raw_bal = data['result'].get('balance', 0) 
                return f"{raw_bal / 100000000:.4f} FRST"
            return "Err: API"
        except:
            return "Offline"

    def poll_wallet(self):
        while self.running:
            new_bal = self.get_balance_rpc()
            with self.lock:
                self.balance = new_bal
                self.status = "Live" if "FRST" in new_bal else "Offline"
            time.sleep(5) # Poll every 5 seconds

    def stop(self):
        self.running = False
        self.thread.join()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Frost Crush 2 - Powered by Finux")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.big_font = pygame.font.SysFont("Arial", 36, bold=True)
        
        self.wallet = FrostWallet()
        self.grid = [[random.choice(GEM_COLORS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected = None # (row, col)
        self.score = 0
        
    def draw_ui(self):
        # Top Bar (Wallet UI)
        pygame.draw.rect(self.screen, UI_BG, (0, 0, SCREEN_WIDTH, OFFSET_Y))
        
        # Title
        title = self.big_font.render("FROST CRUSH 2", True, FROST_BLUE)
        self.screen.blit(title, (20, 20))
        
        # Live Wallet Status
        with self.wallet.lock:
            bal_text = self.font.render(f"Wallet: {self.wallet.balance}", True, WHITE)
            status_text = self.font.render(f"Node: {self.wallet.status}", True, (0, 255, 0) if self.wallet.status == "Live" else (255, 0, 0))
        
        self.screen.blit(bal_text, (20, 70))
        self.screen.blit(status_text, (20, 100))
        
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 215, 0))
        self.screen.blit(score_text, (300, 70))

    def draw_grid(self):
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                x = c * TILE_SIZE + MARGIN
                y = r * TILE_SIZE + OFFSET_Y
                
                # Highlight selection
                if self.selected == (r, c):
                    pygame.draw.rect(self.screen, WHITE, (x-2, y-2, TILE_SIZE+4, TILE_SIZE+4), 3)
                
                # Draw Gem (Simple Rect for prototype, use images for final)
                color = self.grid[r][c]
                pygame.draw.rect(self.screen, color, (x+2, y+2, TILE_SIZE-4, TILE_SIZE-4), border_radius=10)
                
                # Add "Frost" shine
                pygame.draw.circle(self.screen, (255,255,255, 100), (x+15, y+15), 5)

    def swap(self, r1, c1, r2, c2):
        self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]
        if not self.check_matches():
            # Swap back if no match (simplified logic)
            self.grid[r1][c1], self.grid[r2][c2] = self.grid[r2][c2], self.grid[r1][c1]
        else:
            self.score += 10 # Add points (or mint tokens here!)

    def check_matches(self):
        # Simplified horizontal match check for prototype
        matched = False
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE-2):
                if self.grid[r][c] == self.grid[r][c+1] == self.grid[r][c+2]:
                    # Generate new gems (fall down logic simplified to random replacement)
                    self.grid[r][c] = random.choice(GEM_COLORS)
                    self.grid[r][c+1] = random.choice(GEM_COLORS)
                    self.grid[r][c+2] = random.choice(GEM_COLORS)
                    matched = True
        
        # Add Vertical checks here...
        return matched

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if my > OFFSET_Y: # Clicked in grid
                    c = (mx - MARGIN) // TILE_SIZE
                    r = (my - OFFSET_Y) // TILE_SIZE
                    
                    if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                        if self.selected:
                            sr, sc = self.selected
                            # Check adjacency
                            if abs(sr - r) + abs(sc - c) == 1:
                                self.swap(sr, sc, r, c)
                                self.selected = None
                            else:
                                self.selected = (r, c)
                        else:
                            self.selected = (r, c)
        return True

    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            running = self.handle_input()
            
            self.draw_ui()
            self.draw_grid()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        self.wallet.stop()
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
