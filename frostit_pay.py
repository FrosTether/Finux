import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.clock import Clock
import random

# --- Config ---
Window.clearcolor = (0.02, 0.05, 0.1, 1)

class TransferScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # 1. Header
        self.header = Label(
            text='[b]FROSTBITE NETWORK[/b]\n[size=14]Secure Liquidity Stream[/size]', 
            markup=True, 
            font_size='28sp',
            color=(0, 1, 1, 1),
            size_hint_y=0.2
        )
        self.add_widget(self.header)

        # 2. Transaction Details
        details = GridLayout(cols=2, spacing=10, size_hint_y=0.3)
        
        # Source
        details.add_widget(Label(text='SOURCE:', color=(0.5, 0.5, 0.5, 1), halign='right'))
        details.add_widget(Label(text='[b]ICE VAULT (You)[/b]', markup=True, halign='left'))
        
        # Destination (The Wind Chime)
        details.add_widget(Label(text='TARGET:', color=(0.5, 0.5, 0.5, 1), halign='right'))
        details.add_widget(Label(text='[b]🎐 WIND CHIME NODE[/b]', markup=True, halign='left', font_name='Roboto')) # Standard font supports emoji often
        
        # Amount
        details.add_widget(Label(text='AMOUNT:', color=(0.5, 0.5, 0.5, 1), halign='right'))
        self.amount_lbl = Label(text='[b]$1,000.00[/b]', markup=True, halign='left', color=(0, 1, 0, 1))
        details.add_widget(self.amount_lbl)

        self.add_widget(details)

        # 3. The "Stream" (Progress Bar)
        self.status_lbl = Label(text='Status: READY', color=(0.7, 0.7, 0.7, 1), size_hint_y=0.1)
        self.add_widget(self.status_lbl)

        self.progress = ProgressBar(max=100, value=0, size_hint_y=0.05)
        self.add_widget(self.progress)

        # 4. The Trigger Button
        self.btn_send = Button(
            text='INITIATE LIQUID TRANSFER',
            background_color=(0, 0.8, 1, 1),
            bold=True,
            size_hint_y=0.15
        )
        self.btn_send.bind(on_press=self.start_transfer)
        self.add_widget(self.btn_send)

    def start_transfer(self, instance):
        # Lock the button
        self.btn_send.disabled = True
        self.btn_send.text = "PROCESSING..."
        self.status_lbl.text = "Status: HANDSHAKE WITH 🎐..."
        self.status_lbl.color = (1, 1, 0, 1) # Yellow
        
        # Start the "Flow"
        Clock.schedule_interval(self.update_stream, 0.05)

    def update_stream(self, dt):
        if self.progress.value < 100:
            self.progress.value += 2  # Speed of transfer
            
            # Simulated Network Log
            if self.progress.value == 30:
                self.status_lbl.text = "Status: ENCRYPTING ASSETS..."
            elif self.progress.value == 60:
                self.status_lbl.text = "Status: ROUTING VIA FROSTBITE..."
            elif self.progress.value == 90:
                self.status_lbl.text = "Status: DEPOSITING TO 🎐..."
        else:
            self.finish_transfer()
            return False # Stop the clock

    def finish_transfer(self, dt=None):
        self.status_lbl.text = "Status: TRANSFER COMPLETE [HASH: #A9F2]"
        self.status_lbl.color = (0, 1, 0, 1) # Green
        self.btn_send.text = "SENT SUCCESSFUL"
        self.btn_send.background_color = (0.2, 0.2, 0.2, 1)
        
        # Visual Confirmation
        self.header.text = "[b]FROSTBITE NETWORK[/b]\n[size=14]Transaction Finalized[/size]"

class FrostitPayApp(App):
    def build(self):
        return TransferScreen()

if __name__ == '__main__':
    FrostitPayApp().run()
