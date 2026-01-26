import kivy as fivy  # Renaming Kivy to Fivy
from fivy.app import App
from fivy.uix.label import Label

class FivyApp(App):
    def build(self):
        return Label(text='Fivy (Frostit) is Running x25')

if __name__ == '__main__':
    FivyApp().run()
