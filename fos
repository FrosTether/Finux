from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
from kivy.clock import Clock
import time

# --- GROK AESTHETICS ---
C_DARK = (0.05, 0.05, 0.08, 1)
C_NEON = (0.22, 1, 0.9, 1) # Cyan
C_WARN = (1, 0.6, 0, 1)    # Orange

Window.clearcolor = (0, 0, 0, 0) # Transparent-ish overlay simulation
Window.size = (350, 180)         # Small Notification Size

class GrokAlert(App):
    def build(self):
        self.title = "System Notification"
        
        # Main Card
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Background Drawing
        with root.canvas.before:
            Color(0.1, 0.1, 0.12, 1) # Dark Card BG
            Rectangle(pos=root.pos, size=root.size)
            
            # Neon Border
            Color(*C_NEON)
            Line(rectangle=(0, 0, 350, 180), width=1.5)
        
        # 1. Header
        header = BoxLayout(size_hint_y=0.3)
        header.add_widget(Label(text="[b]GROK SYSTEM AGENT[/b]", markup=True, color=C_NEON, halign='left', size_hint_x=0.8))
        header.add_widget(Label(text="NOW", color=C_WARN, font_size='10sp', size_hint_x=0.2))
        root.add_widget(header)
        
        # 2. Body Text
        root.add_widget(Label(
            text="Update Available: v1.3-Audited\n> Critical Security Patch\n> Gas Optimization Applied",
            halign='center',
            color=(0.9, 0.9, 0.9, 1)
        ))
        
        # 3. Progress / Action
        self.btn = Button(
            text="INSTALL UPDATE", 
            background_color=C_NEON, 
            color=(0,0,0,1), 
            bold=True,
            on_press=self.start_install
        )
        root.add_widget(self.btn)
        
        self.progress = ProgressBar(max=100, value=0, size_hint_y=None, height=10, opacity=0)
        root.add_widget(self.progress)
        
        return root

    def start_install(self, instance):
        # Animation logic to simulate download
        instance.text = "DOWNLOADING..."
        instance.disabled = True
        self.progress.opacity = 1
        Clock.schedule_interval(self.update_bar, 0.05)

    def update_bar(self, dt):
        self.progress.value += 2
        if self.progress.value >= 100:
            self.btn.text = "RESTARTING KERNEL..."
            self.progress.opacity = 0
            # Close app simulation
            Clock.schedule_once(lambda d: App.get_running_app().stop(), 1)
            return False
        return True

if __name__ == "__main__":
    GrokAlert().run()
