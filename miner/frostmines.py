import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

# --- SCREEN 1: THE REACTOR (Mining) ---
class ReactorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.hash_label = Label(text="HASHRATE: 0.00 MH/s", font_size='24sp', color=(0, 1, 0, 1))
        layout.add_widget(self.hash_label)

        layout.add_widget(Label(text="[FROST CRUSH] & [FROSTMAN] DRIVERS LOADED", markup=True))

        btn_games = Button(text="ENTER GAMEFI TERMINAL", size_hint=(1, 0.2), background_color=(0.22, 0.74, 1, 1))
        btn_games.bind(on_press=self.go_to_games)
        layout.add_widget(btn_games)

        self.add_widget(layout)
        Clock.schedule_interval(self.update_hash, 1.0)

    def update_hash(self, dt):
        self.hash_label.text = f"HASHRATE: {random.uniform(45, 60):.2f} MH/s"

    def go_to_games(self, instance):
        self.manager.current = 'games'

# --- SCREEN 2: GAME SELECTION ---
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        layout.add_widget(Label(text="SELECT MINING PROTOCOL", font_size='20sp', bold=True))

        # Game 1: FrostMan (Pacman Genesis Hack)
        btn_pac = Button(text="> EXECUTE FROSTMAN.EXE", background_color=(1, 1, 0, 1), color=(0,0,0,1))
        btn_pac.bind(on_press=lambda x: self.launch_game("FROSTMAN"))
        layout.add_widget(btn_pac)

        # Game 2: Frost Crush
        btn_crush = Button(text="> EXECUTE FROST_CRUSH.EXE", background_color=(1, 0, 1, 1))
        btn_crush.bind(on_press=lambda x: self.launch_game("FROST CRUSH"))
        layout.add_widget(btn_crush)

        btn_back = Button(text="RETURN TO REACTOR", size_hint=(1, 0.2))
        btn_back.bind(on_press=self.go_back)
        layout.add_widget(btn_back)

        self.status = Label(text="STATUS: IDLE")
        layout.add_widget(self.status)
        self.add_widget(layout)

    def launch_game(self, game_name):
        self.status.text = f"RUNNING {game_name}...\n(Proof-of-Play Mining Active)"

    def go_back(self, instance):
        self.manager.current = 'reactor'

class FrostMinesApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ReactorScreen(name='reactor'))
        sm.add_widget(GameScreen(name='games'))
        return sm

if __name__ == '__main__':
    FrostMinesApp().run()