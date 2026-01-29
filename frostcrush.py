from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from random import choice

# Configuration
COLORS = [(0.2, 0.8, 1, 1), (1, 0.2, 0.2, 1), (0.2, 1, 0.2, 1), (1, 1, 0.2, 1)] # Ice Blue, Red, Green, Yellow

class FrostCrushGame(GridLayout):
    def __init__(self, **kwargs):
        super(FrostCrushGame, self).__init__(**kwargs)
        self.cols = 7
        self.spacing = 2  # Gap between "ice" blocks
        self.padding = 10
        self.generate_board()

    def generate_board(self):
        self.clear_widgets()
        for i in range(49): # 7x7 Grid
            btn = Button(background_normal='', background_color=choice(COLORS))
            btn.bind(on_press=self.on_crush)
            self.add_widget(btn)

    def on_crush(self, instance):
        # Placeholder for Match-3 Logic
        # In the final version, this checks neighbors
        print("Frosty Block Crushed!")
        instance.background_color = (1, 1, 1, 0.5) # Fade out effect

class FrostCrushApp(App):
    def build(self):
        return FrostCrushGame()

if __name__ == '__main__':
    FrostCrushApp().run()
