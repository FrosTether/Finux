# FOME: FROST OF MY ENVIRONMENT (GNOME-Based)
# Engine: Kivy (Touch Friendly)
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class FOMEShell(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1) # GNOME Grey
        layout = FloatLayout()

        # 1. The Top Bar (GNOME Style)
        top_bar = Button(
            text="Activities                                                       Jan 30 21:30", 
            size_hint=(1, 0.05), 
            pos_hint={'top': 1},
            background_color=(0, 0, 0, 1),
            color=(1, 1, 1, 1)
        )
        layout.add_widget(top_bar)

        # 2. The App Grid (Overview)
        grid = GridLayout(cols=3, padding=50, spacing=20, size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        apps = ["Frost Crush 2", "Wallet", "Settings", "Terminal", "Files", "FrostMart"]
        for app in apps:
            btn = Button(
                text=app, 
                background_color=(0.2, 0.2, 0.2, 1), 
                color=(0, 1, 1, 1),
                background_normal='' # Flat design
            )
            # GNOME Rounded corners simulated via Kivy canvas would go here
            grid.add_widget(btn)
            
        layout.add_widget(grid)

        # 3. The Dash (Left Dock)
        dash = Button(size_hint=(0.05, 0.6), pos_hint={'x': 0.01, 'center_y': 0.5}, background_color=(0.15, 0.15, 0.15, 1))
        layout.add_widget(dash)

        return layout

if __name__ == '__main__':
    FOMEShell().run()
