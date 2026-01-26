import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# --- Big Burr Config ---
# The "Ice" Theme (Dark Blue/Black)
Window.clearcolor = (0.02, 0.05, 0.1, 1)

class BurrDashboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 15

        # 1. THE STATUS DECK ("Over the Apple G")
        # Shows we are running on top of their infra
        status_deck = BoxLayout(size_hint_y=0.15, spacing=5)
        
        # Google Indicator
        self.g_status = Label(
            text='[color=4285F4]G[/color] LINKED', 
            markup=True, 
            font_size='12sp',
            canvas_before=self._bg((0.1, 0.1, 0.2, 1))
        )
        # Apple Indicator
        self.a_status = Label(
            text='[color=ffffff]🍎[/color] TUNNELED', 
            markup=True, 
            font_size='12sp',
            canvas_before=self._bg((0.1, 0.1, 0.2, 1))
        )
        
        status_deck.add_widget(self.g_status)
        status_deck.add_widget(self.a_status)
        self.add_widget(status_deck)

        # 2. THE BIG BURR HEADER
        header = Label(
            text='[b]BIG BURR[/b]\n[size=14]Frostit Neural Core v72[/size]', 
            markup=True, 
            font_size='32sp',
            color=(0, 1, 1, 1), # Cyan Ice
            size_hint_y=0.15
        )
        self.add_widget(header)

        # 3. THE "FROSTBITE" AI ENGINE (The Work)
        self.terminal = Label(
            text='[color=00ffff]FrostbiteAI >[/color] Systems warm.\n[color=00ffff]FrostbiteAI >[/color] Awaiting directives...\n',
            markup=True,
            halign='left',
            valign='top',
            size_hint_y=0.4,
            text_size=(Window.width - 40, None),
            font_name='RobotoMono-Regular'
        )
        
        # Wrap terminal in a "glass" box
        term_box = BoxLayout(padding=10)
        with term_box.canvas.before:
            Color(0.05, 0.08, 0.15, 1)
            Rectangle(pos=term_box.pos, size=term_box.size)
        term_box.add_widget(self.terminal)
        self.add_widget(term_box)

        # 4. THE ICE VAULT (Grade & Pay)
        vault_grid = GridLayout(cols=2, size_hint_y=0.2, spacing=10)
        
        # Wallet Balance
        self.balance_btn = Button(
            text='VAULT\n$0.00 (BTC)',
            background_color=(0.2, 0.2, 0.2, 1),
            color=(0, 1, 0, 1)
        )
        self.balance_btn.bind(on_press=self.add_funds)

        # Grade/Rank
        self.rank_btn = Button(
            text='RANK\nGlacier (Lvl 1)',
            background_color=(0.2, 0.2, 0.2, 1),
            color=(0.5, 0.8, 1, 1)
        )

        vault_grid.add_widget(self.balance_btn)
        vault_grid.add_widget(self.rank_btn)
        self.add_widget(vault_grid)

        # 5. CONTROL ACTION
        btn_deploy = Button(
            text='DEPLOY PROTOCOL',
            size_hint_y=0.1,
            background_color=(0, 0.8, 1, 1),
            bold=True
        )
        btn_deploy.bind(on_press=self.deploy_action)
        self.add_widget(btn_deploy)

    def _bg(self, color):
        # Helper for background colors on labels
        from kivy.graphics import Color, Rectangle
        # (Note: In a full app this needs a proper update loop, simplistic for demo)
        return []

    def add_funds(self, instance):
        self.balance_btn.text = "VAULT\n$1,000.00 (BTC)"
        self.terminal.text += "\n[color=00ff00]>> Funds Secured.[/color]"

    def deploy_action(self, instance):
        self.terminal.text += "\n[color=00ffff]>> Big Burr Protocol: ACTIVE[/color]\n>> Compiling Assets..."

class BigBurrApp(App):
    def build(self):
        return BurrDashboard()

if __name__ == '__main__':
    BigBurrApp().run()
