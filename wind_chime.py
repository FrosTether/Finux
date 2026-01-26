import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation

# --- Wind Chime Aesthetics (Airy/Light) ---
# White background for the "Air" vibe
Window.clearcolor = (0.9, 0.95, 1, 1)

class ChimeNode(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20

        # 1. The Icon (The Chime)
        self.icon = Label(
            text='🎐', 
            font_size='100sp',
            size_hint_y=0.4
        )
        self.add_widget(self.icon)

        # 2. Status Text
        self.status = Label(
            text='[b]HANGING THE CHIME...[/b]', 
            markup=True,
            font_size='24sp',
            color=(0.2, 0.4, 0.6, 1)
        )
        self.add_widget(self.status)

        # 3. The Ledger (Wallet)
        self.ledger = Label(
            text='Balance: $0.00',
            font_size='20sp',
            color=(0.5, 0.5, 0.5, 1)
        )
        self.add_widget(self.ledger)

        # Start the "Deployment" sequence
        Clock.schedule_once(self.node_active, 2)

    def node_active(self, dt):
        self.status.text = "🎐 NODE IS UP.\nListening to the wind..."
        self.status.color = (0, 0.6, 0.8, 1)
        
        # Animate the chime swaying (Simulating wind)
        anim = Animation(font_size='110sp', duration=1) + Animation(font_size='100sp', duration=1)
        anim.repeat = True
        anim.start(self.icon)

        # Catch the money (Simulated network latency)
        Clock.schedule_once(self.receive_funds, 4)

    def receive_funds(self, dt):
        self.status.text = "🎐 INCOMING FLOW DETECTED"
        self.status.color = (0, 0.8, 0, 1) # Green
        
        # Flash effect
        self.ledger.text = "[b]Balance: $1,000.00[/b]"
        self.ledger.markup = True
        self.ledger.color = (0, 0, 0, 1) # Solid Black
        self.ledger.font_size = '30sp'

class WindChimeApp(App):
    def build(self):
        return ChimeNode()

if __name__ == '__main__':
    WindChimeApp().run()
