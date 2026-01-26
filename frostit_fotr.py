import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
import random
import time

# --- Config ---
Window.clearcolor = (0.05, 0.05, 0.08, 1)

# --- The FOTR Protocol Engine (Simulated) ---
class FotrProtocol:
    @staticmethod
    def generate_tunnel_id():
        # Generates a pseudo-encrypted tunnel hash
        chars = "ABCDEF0123456789"
        return "fotr_" + "".join(random.choice(chars) for _ in range(12))

    @staticmethod
    def encrypt_packet(data):
        return f"[FOTR-ENC::{data}::END]"

# --- Screen 1: The Multi-Auth Gate ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Header
        self.logo = Label(
            text='[b]FROSTIT v71[/b]\n[size=16]Secure Multi-Cloud Gateway[/size]', 
            markup=True, font_size='32sp', color=(0, 1, 0.8, 1)
        )

        self.status_log = Label(
            text='Select Identity Provider...',
            color=(0.6, 0.6, 0.6, 1),
            font_size='14sp',
            size_hint_y=0.2
        )

        # 1. Google Button (Existing)
        btn_google = Button(
            text='Google Cloud',
            size_hint=(1, 0.15),
            background_color=(0.25, 0.52, 0.96, 1)
        )
        
        # 2. Apple Button (New Request)
        # Apple styling: White/Black (Clean)
        btn_apple = Button(
            text=' Sign in with Apple',
            size_hint=(1, 0.15),
            background_normal='',
            background_color=(1, 1, 1, 1),
            color=(0, 0, 0, 1),
            bold=True
        )
        btn_apple.bind(on_press=self.initiate_fotr_tunnel)

        layout.add_widget(self.logo)
        layout.add_widget(self.status_log)
        layout.add_widget(btn_google)
        layout.add_widget(btn_apple)
        self.add_widget(layout)

    def initiate_fotr_tunnel(self, instance):
        # This starts the "Tunneling" sequence instead of just logging in
        self.status_log.text = "Initializing FOTR Protocol..."
        self.status_log.color = (1, 1, 0, 1)
        
        # Step 1: Handshake
        Clock.schedule_once(self.step_tunnel, 1.5)

    def step_tunnel(self, dt):
        tid = FotrProtocol.generate_tunnel_id()
        self.status_log.text = f"Tunnel Established: {tid}\nRouting Apple ID Traffic..."
        self.status_log.color = (0, 1, 0.5, 1)
        
        # Step 2: Route to Dashboard
        Clock.schedule_once(self.finish_login, 2.0)

    def finish_login(self, dt):
        self.manager.current = 'dashboard'

# --- Screen 2: The Secure Workspace ---
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Encrypted Header
        header = Label(
            text='[color=ffffff][/color] Apple ID: [i]jacob...[/i]\n[size=14][color=00ff00]VIA FOTR PROTOCOL[/color][/size]', 
            markup=True, 
            size_hint_y=0.15
        )

        # The Visualizer
        self.monitor = Label(
            text='[b]TRAFFIC MONITOR[/b]\nWaiting for packets...',
            markup=True,
            font_family='Monospace',
            color=(0.8, 0.8, 0.9, 1)
        )

        # Simulation Button
        btn_sync = Button(
            text='Sync iCloud Data (Tunnel)',
            size_hint_y=0.1,
            background_color=(0.5, 0, 0.5, 1) # Purple for Privacy
        )
        btn_sync.bind(on_press=self.sync_data)

        layout.add_widget(header)
        layout.add_widget(self.monitor)
        layout.add_widget(btn_sync)
        self.add_widget(layout)

    def sync_data(self, instance):
        # Simulate packet encryption via FOTR
        raw_data = "Photos_Sync_Packet_01"
        encrypted = FotrProtocol.encrypt_packet(raw_data)
        self.monitor.text = (
            f"[b]SOURCE:[/b] Apple Cloud ☁️\n"
            f"[b]ROUTING:[/b] 127.0.0.1:9050 (FOTR)\n"
            f"[b]PAYLOAD:[/b] {encrypted}\n"
            f"[b]STATUS:[/b] Secure"
        )

class FrostitFotrApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    FrostitFotrApp().run()
