
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Line, Rectangle
from kivy.clock import Clock
from kivy.utils import platform

class HUDOverlay(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # 1. RETICLE (The Center Target)
        with self.canvas:
            Color(0, 0.9, 1, 0.8) # Frost Cyan
            # Draw corner brackets for the viewfinder
            self.line1 = Line(points=[100, 200, 100, 300], width=2)
            self.line2 = Line(points=[100, 300, 200, 300], width=2)
            self.line3 = Line(points=[600, 200, 600, 300], width=2)
            self.line4 = Line(points=[600, 300, 500, 300], width=2)
            
        # 2. DATA STREAM (Left Side)
        self.data_log = Label(
            text="Initializing Visual Cortex...", 
            font_size='14sp', 
            color=(0, 1, 0, 1), 
            halign='left', 
            valign='top', 
            pos_hint={'x': 0.05, 'top': 0.9}, 
            size_hint=(0.4, 0.5)
        )
        self.data_log.bind(size=self.data_log.setter('text_size'))
        self.add_widget(self.data_log)

        # 3. SYSTEM STATUS (Top Right)
        self.status = Label(
            text="FROST OS: ONLINE
BATTERY: 98%
NET: SECURE", 
            font_size='12sp', 
            color=(0, 0.9, 1, 1), 
            halign='right',
            pos_hint={'right': 0.95, 'top': 0.95}
        )
        self.add_widget(self.status)

        # 4. BOTTOM BAR (Mining Stats)
        self.miner = Label(
            text="[ MINING ACTIVE: 12.5 FNR/hr ]", 
            font_size='16sp', 
            bold=True, 
            color=(1, 0.5, 0, 1), 
            pos_hint={'center_x': 0.5, 'y': 0.05}
        )
        self.add_widget(self.miner)

        # Start the "Scanning" Loop
        Clock.schedule_interval(self.update_hud, 0.2)

    def update_hud(self, dt):
        # Simulate AI Scanning Logic
        scans = [
            "Scanning object...", "Analyzing geometry...", 
            "Identity: UNKNOWN", "Value: 0.0004 BTC", 
            "Texture: Organic", "Threat Level: 0", 
            "FrostMind: Connected", "Uploading to Node..."
        ]
        
        # Add random "Hex" codes to look like raw data
        hex_code = "0x" + "".join([random.choice("0123456789ABCDEF") for i in range(8)])
        
        current_text = self.data_log.text.split("\n")
        if len(current_text) > 8: 
            current_text.pop(0) # Keep log short
            
        new_line = f"> {random.choice(scans)} [{hex_code}]"
        current_text.append(new_line)
        self.data_log.text = "\n".join(current_text)

class FrostGlassApp(App):
    def build(self):
        layout = FloatLayout()
        
        # LAYER 1: THE CAMERA
        # Resolution optimized for high FPS
        self.cam = Camera(resolution=(640, 480), play=True)
        self.cam.allow_stretch = True
        self.cam.keep_ratio = False
        layout.add_widget(self.cam)
        
        # LAYER 2: THE FROST HUD
        layout.add_widget(HUDOverlay())
        
        return layout

if __name__ == '__main__':
    import random # Re-import for safety inside class
    FrostGlassApp().run()
