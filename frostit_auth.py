import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
import time

# --- System Config ---
Window.clearcolor = (0.05, 0.05, 0.08, 1) # Deep Space Black

# --- Screen 1: The Gatekeeper (Google Login) ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Logo / Branding
        logo = Label(
            text='[b]FROSTIT[/b]\n[size=20]Secure Environment[/size]', 
            markup=True, 
            font_size='40sp',
            color=(0, 1, 0.8, 1)
        )
        
        # Status Text
        self.status = Label(text='Identity Verification Required', color=(0.5, 0.5, 0.5, 1))

        # The "Google" Button (No Password Needed)
        # Using Google Blue hex code: #4285F4
        btn_google = Button(
            text='Sign in with Google',
            size_hint=(1, 0.2),
            background_normal='',
            background_color=(0.25, 0.52, 0.96, 1),
            bold=True
        )
        btn_google.bind(on_press=self.do_google_login)

        layout.add_widget(logo)
        layout.add_widget(self.status)
        layout.add_widget(btn_google)
        self.add_widget(layout)

    def do_google_login(self, instance):
        # 1. Simulate the Network Handshake
        self.status.text = "Connecting to Google OAuth 2.0..."
        self.status.color = (1, 1, 0, 1) # Yellow
        
        # 2. Simulate Token Verification (Delay)
        Clock.schedule_once(self.finish_login, 1.5)

    def finish_login(self, dt):
        # 3. Unlock the App
        self.manager.current = 'dashboard'

# --- Screen 2: The Dashboard (Vibe Space) ---
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Header
        header = Label(
            text='[color=00ff00]●[/color] Jacob Frost [i](Authenticated)[/i]', 
            markup=True, 
            size_hint_y=0.1,
            halign='left'
        )
        header.bind(size=header.setter('text_size'))

        # The Workspace
        workspace = Label(
            text='[b]FROSTIT CORE[/b]\n\nAccess Granted.\nAlgorithm v68305 Active.\n\nReady for input...',
            markup=True,
            color=(0.8, 0.8, 0.9, 1)
        )

        # Logout
        btn_logout = Button(
            text='Disconnect Session',
            size_hint_y=0.1,
            background_color=(1, 0.2, 0.2, 1)
        )
        btn_logout.bind(on_press=self.logout)

        layout.add_widget(header)
        layout.add_widget(workspace)
        layout.add_widget(btn_logout)
        self.add_widget(layout)

    def logout(self, instance):
        self.manager.current = 'login'

# --- The Main App Controller ---
class FrostitAuthApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    FrostitAuthApp().run()
