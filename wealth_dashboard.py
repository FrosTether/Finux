import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import Color, Rectangle, Line
from kivy.core.window import Window
from kivy.clock import Clock

# --- BILLIONAIRE DASHBOARD THEME ---
C_BG     = (0.05, 0.05, 0.08, 1) # Deep Space
C_GOLD   = (1, 0.84, 0, 1)       # Gold (Wealth)
C_CYAN   = (0.22, 0.74, 1, 1)    # Frost Cyan (Tech)
C_GREEN  = (0.2, 0.8, 0.2, 1)    # Profit
C_TEXT   = (0.9, 0.9, 0.9, 1)

Window.clearcolor = C_BG

class WealthDashboard(App):
    def build(self):
        self.title = "Frost Family Office: Net Worth Tracker"
        self.fszt_price = 1.20  # TARGET PRICE
        self.holdings = 25000000.31 # Your Supply
        
        root = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # --- 1. TOTAL NET WORTH HEADER ---
        root.add_widget(Label(text="TOTAL ESTIMATED VALUE", color=C_GOLD, font_size='14sp'))
        
        self.lbl_net_worth = Label(
            text="$0.00", 
            font_size='50sp', 
            color=C_GREEN, 
            bold=True
        )
        root.add_widget(self.lbl_net_worth)
        
        # Price Ticker (Simulated Live Feed)
        self.lbl_price = Label(text=f"FSZT/USD: ${self.fszt_price:.2f} (+4.2%)", color=C_CYAN)
        root.add_widget(self.lbl_price)

        # Divider
        with root.canvas:
            Color(1, 1, 1, 0.2)
            Line(points=[30, root.height-180, root.width-30, root.height-180], width=1)

        # --- 2. ASSET ALLOCATION (Grid) ---
        grid = GridLayout(cols=2, spacing=10, size_hint_y=0.4)
        
        # Row 1: Genesis Supply
        grid.add_widget(self.create_asset_card("GENESIS VAULT", "25,000,000 FSZT", C_CYAN))
        
        # Row 2: Chronos/Bio Vaults
        grid.add_widget(self.create_asset_card("CHRONOS TIMELINE", "7 Locked Vaults", C_GOLD))
        
        # Row 3: Game Rewards
        grid.add_widget(self.create_asset_card("GAMEFI YIELD", "12,450 FTC", (1, 0.5, 0, 1)))
        
        # Row 4: Liquid (Testnet)
        grid.add_widget(self.create_asset_card("LIQUID (TESTNET)", "5.0 ETH", (0.5, 0.5, 0.5, 1)))
        
        root.add_widget(grid)

        # --- 3. PROJECTED GROWTH (Graph Simulation) ---
        root.add_widget(Label(text="PROJECTED YIELD (2026-2030)", size_hint_y=0.1, color=C_TEXT))
        self.progress = ProgressBar(max=100, value=75, size_hint_y=0.05)
        root.add_widget(self.progress)
        
        # Start Animation
        Clock.schedule_once(self.animate_value, 0.5)
        Clock.schedule_interval(self.live_ticker, 1.0)
        
        return root

    def create_asset_card(self, title, value, color):
        box = BoxLayout(orientation='vertical', padding=10)
        with box.canvas.before:
            Color(0.1, 0.1, 0.15, 1)
            Rectangle(pos=box.pos, size=box.size)
            Color(*color)
            Line(rectangle=(box.x, box.y, box.width, box.height), width=1.2)
            
        box.add_widget(Label(text=title, font_size='12sp', color=color))
        box.add_widget(Label(text=value, font_size='18sp', bold=True))
        return box

    def animate_value(self, dt):
        # Calculate Total: (25M * 1.20) + small assets
        total_val = (self.holdings * self.fszt_price) + 15000 # +$15k misc
        self.lbl_net_worth.text = f"${total_val:,.2f}"

    def live_ticker(self, dt):
        # Simulate market fluctuation
        flux = random.uniform(-0.02, 0.03)
        self.fszt_price += flux
        if self.fszt_price < 1.0: self.fszt_price = 1.0
        
        total_val = (self.holdings * self.fszt_price) + 15000
        
        # Update UI
        self.lbl_net_worth.text = f"${total_val:,.2f}"
        
        # Color logic
        pct_color = C_GREEN if flux >= 0 else (1, 0, 0, 1)
        self.lbl_price.text = f"FSZT/USD: ${self.fszt_price:.2f} ({flux*100:+.2f}%)"
        self.lbl_price.color = pct_color

if __name__ == "__main__":
    Window.size = (400, 700)
    WealthDashboard().run()
