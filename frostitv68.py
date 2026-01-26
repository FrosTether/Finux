import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# --- Frostit v683 Config ---
# Deep Focus Theme (Dark "Vibe" Mode)
Window.clearcolor = (0.05, 0.05, 0.08, 1)

class FrostitDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # 1. Top Bar: Status & Integration
        top_bar = BoxLayout(size_hint_y=0.1, spacing=10)
        
        self.status_label = Label(
            text='[b]FROSTIT v683[/b] | System: [color=00ff00]ONLINE[/color]', 
            markup=True, 
            size_hint_x=0.7,
            halign='left', 
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        
        # The "Pay/Integrate" Button
        btn_integrate = Button(
            text='CONNECT GOOGLE', 
            size_hint_x=0.3,
            background_color=(0, 0.5, 1, 1), # Google Blue
            color=(1, 1, 1, 1)
        )
        btn_integrate.bind(on_press=self.integrate_services)
        
        top_bar.add_widget(self.status_label)
        top_bar.add_widget(btn_integrate)
        self.add_widget(top_bar)

        # 2. The Editor Area (Vibe Coding Space)
        self.editor = TextInput(
            text='# Frostit Code Space\n# Type your vibe here...',
            background_color=(0.1, 0.1, 0.12, 1),
            foreground_color=(0.8, 0.8, 0.8, 1),
            multiline=True,
            font_name='RobotoMono-Regular', # Default monospace if available
            size_hint_y=0.8
        )
        self.add_widget(self.editor)

        # 3. Bottom Control Deck
        bottom_deck = BoxLayout(size_hint_y=0.1, spacing=10)
        
        btn_run = Button(
            text='EXECUTE',
            background_color=(0, 1, 0.5, 1), # Neon Green
            color=(0, 0, 0, 1)
        )
        btn_run.bind(on_press=self.run_code)
        
        bottom_deck.add_widget(btn_run)
        self.add_widget(bottom_deck)

    def integrate_services(self, instance):
        # Simulating the "Integrate Everything" request
        self.status_label.text = '[b]FROSTIT[/b] | Cloud Link: [color=00ffff]ESTABLISHED[/color]'
        self.editor.text += "\n>> Connecting to Neural Backend...\n>> Google Integration: ACTIVE"

    def run_code(self, instance):
        self.editor.text += "\n>> Running v683 Protocol... SUCCESS."

class FrostitApp(App):
    def build(self):
        return FrostitDashboard()

if __name__ == '__main__':
    FrostitApp().run()
