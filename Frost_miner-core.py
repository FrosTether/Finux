from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
import requests
import json
import random

# CONFIGURATION: Toggle this to build the "Kylecoin" version
APP_MODE = "FROSTNERJO" # Options: "FROSTNERJO" or "KYLECOIN"

class MiningInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10
        self.balance = 0.00
        self.mining_active = False
        
        # 1. Dynamic UI Loading
        if APP_MODE == "FROSTNERJO":
            self.theme_color = (0, 0.6, 1, 1) # Frost Blue
            self.coin_name = "FNR"
            self.logo_src = "assets/frost_logo.png"
        else:
            self.theme_color = (0, 1, 0.2, 1) # Kyle Green
            self.coin_name = "KYLE"
            self.logo_src = "assets/kyle_logo.png"

        # 2. The "WiFi" Header (Interlink Status)
        self.add_widget(Label(text="📡 LINKED TO: Monroeville-Node-01", size_hint=(1, 0.1)))
        
        # 3. Main Dashboard
        self.img = Image(source=self.logo_src, size_hint=(1, 0.4))
        self.add_widget(self.img)
        
        self.lbl_balance = Label(text=f"0.0000 {self.coin_name}", font_size='40sp')
        self.add_widget(self.lbl_balance)

        # 4. The "Mine" Button
        self.btn_mine = Button(text="START MINING", background_color=self.theme_color, size_hint=(1, 0.2))
        self.btn_mine.bind(on_press=self.toggle_mining)
        self.add_widget(self.btn_mine)

    def toggle_mining(self, instance):
        self.mining_active = not self.mining_active
        if self.mining_active:
            self.btn_mine.text = "⛏️ MINING ACTIVE (Syncing...)"
            Clock.schedule_interval(self.mine_cycle, 3) # "Mine" every 3 seconds
        else:
            self.btn_mine.text = "RESUME MINING"
            Clock.unschedule(self.mine_cycle)

    def mine_cycle(self, dt):
        """Simulates mining by pinging the Monroeville Node."""
        # In a real build, this hits your API: http://monroeville-node.local/mine
        reward = random.uniform(0.01, 0.05)
        self.balance += reward
        self.lbl_balance.text = f"{self.balance:.4f} {self.coin_name}"
        
        # The "WiFi" Interlink: Syncs data to the shared JSON ledger
        # This allows the Kylecoin app to see Frostnerjo balances and vice-versa
        print(f"📡 Syncing {reward} {self.coin_name} to Shared Storage...")

class FrostMinerApp(App):
    def build(self):
        return MiningInterface()

if __name__ == '__main__':
    FrostMinerApp().run()
