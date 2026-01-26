import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

class FrostoiseSystem(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, padding=50, **kwargs)
        self.pressure = 0
        
        # Terminal-style Header
        self.header = Label(
            text="[SYSTEM] Command: HYDRO PUMP", 
            font_size='22sp', 
            color=(0.2, 0.6, 1, 1),
            size_hint_y=None, height=50
        )
        self.add_widget(self.header)

        # Status Label
        self.status_label = Label(text="Initiating Pressure Build...", font_size='18sp')
        self.add_widget(self.status_label)
        
        # Progress Bar Drawing Setup
        with self.canvas.after:
            Color(0.1, 0.1, 0.1, 1) # Background track
            self.track = Rectangle(size=(0, 0)) 
            Color(0.2, 0.6, 1, 1)   # Water Blue
            self.bar = Rectangle(size=(0, 0))

        self.bind(size=self._update_rect, pos=self._update_rect)

        # Start the "Build"
        Clock.schedule_interval(self.update_pressure, 0.04)

    def _update_rect(self, *args):
        # Keeps the bar centered if you resize the window
        bar_width = self.width * 0.8
        self.track.pos = (self.center_x - bar_width/2, self.center_y)
        self.track.size = (bar_width, 40)
        self.bar.pos = self.track.pos

    def update_pressure(self, dt):
        if self.pressure < 100:
            self.pressure += 1
            bar_max_width = self.width * 0.8
            self.bar.size = ((self.pressure / 100) * bar_max_width, 40)
            self.status_label.text = f"PRESSURE BUILD: {self.pressure}%"
            return True
        else:
            self.status_label.text = "[LAUNCH READY]"
            self.status_label.color = (0, 1, 0, 1)
            self.show_launch_button()
            return False

    def show_launch_button(self):
        # Create the button once 100% is reached
        btn = Button(
            text="LAUNCH BOTS", 
            size_hint=(None, None), 
            size=(200, 60),
            pos_hint={'center_x': 0.5},
            background_color=(0, 1, 0, 1)
        )
        btn.bind(on_press=self.start_bots)
        self.add_widget(btn)

    def start_bots(self, instance):
        print("\033[92m[FROSTOISE] BOTS DEPLOYED! Hydro Pump at Max Capacity.\033[0m")
        # Add your bot logic here!

class FrostoiseApp(App):
    def build(self):
        return FrostoiseSystem()

if __name__ == "__main__":
    # The terminal intro you liked
    print("\033[94m🌊 Frostoise Engine Loading...\033[0m")
    FrostoiseApp().run()
# Automated Uplink Notification
import os
os.system("echo 'Frostoise Core Online - 1655 W Main Node Initiated' | mail -s '♍🧲 System Live' voluntaryistj@gmail.com")
