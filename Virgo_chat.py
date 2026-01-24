import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window

# Import your new Core
import sys
sys.path.append("/home/frost/finux/virgo/")
from Virgo_Core import VirgoCore

# 🎨 Virgo Aesthetics
Window.clearcolor = (0.05, 0.05, 0.08, 1) # Deep Void Blue
TEXT_COLOR = (0.7, 0.9, 1, 1) # Ice Blue

class VirgoChat(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.core = VirgoCore()
        
        # 1. The Output Console (Top)
        self.history = Label(
            text="[ ♍ VIRGO SYSTEM ONLINE ]\nWaiting for input...",
            size_hint=(1, 0.8),
            halign="left",
            valign="top",
            color=TEXT_COLOR
        )
        self.history.bind(size=self.history.setter('text_size'))
        self.add_widget(self.history)

        # 2. Input Zone (Bottom)
        self.input_box = TextInput(
            size_hint=(1, 0.1),
            multiline=False,
            background_color=(0.1, 0.1, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=TEXT_COLOR
        )
        self.input_box.bind(on_text_validate=self.send_message)
        self.add_widget(self.input_box)

    def send_message(self, instance):
        msg = self.input_box.text
        self.input_box.text = ""
        
        # Echo User
        self.update_log(f"> YOU: {msg}")

        # 🧠 Command Parsing
        if "/video" in msg:
            # Trigger Sora/Veo Injection
            prompt = msg.replace("/video", "").strip()
            response = self.core.generate_video(prompt, engine="hybrid")
            self.update_log(f"[VIDEO]: {response}")
        
        elif "/veo" in msg:
            prompt = msg.replace("/veo", "").strip()
            response = self.core.generate_video(prompt, engine="veo")
            self.update_log(f"[VEO]: {response}")

        else:
            # Default to Grok Brain
            response = self.core.ask_brain(msg)
            self.update_log(f"[GROK]: {response}")

    def update_log(self, text):
        current = self.history.text
        new_text = current + "\n" + text
        # Keep only last 10 lines to prevent clutter
        self.history.text = "\n".join(new_text.split('\n')[-15:])

class VirgoApp(App):
    def build(self):
        return VirgoChat()

if __name__ == "__main__":
    VirgoApp().run()
