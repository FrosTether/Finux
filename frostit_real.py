import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.clock import Clock
import webbrowser # <--- The Key to opening Chrome
import time

# --- Configuration ---
Window.clearcolor = (0.05, 0.05, 0.08, 1)

# --- Real Google Auth Config (Standard Public Scope) ---
# In a production app, you replace 'YOUR_ID' with your real Google Cloud Client ID.
GOOGLE_AUTH_URL = (
    "https://accounts.google.com/o/oauth2/v2/auth?"
    "scope=email%20profile&"
    "response_type=token&"
    "redirect_uri=http://localhost:8080&"
    "client_id=YOUR_GOOGLE_CLOUD_CLIENT_ID" # Placeholder for the URL structure
)

# --- Screen 1: The Login Portal ---
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        # Branding
        self.logo = Label(
            text='[b]FROSTIT[/b]\n[size=18]Identity Layer v70[/size]', 
            markup=True, 
            font_size='36sp',
            color=(0, 1, 0.8, 1)
        )
        
        self.status = Label(
            text='Waiting for Provider...', 
            color=(0.5, 0.5, 0.5, 1),
            font_size='14sp'
        )

        # The Real Trigger Button
        btn_google = Button(
            text='LAUNCH GOOGLE SIGN-IN',
            size_hint=(1, 0.25),
            background_normal='',
            background_color=(0.25, 0.52, 0.96, 1),
            bold=True
        )
        btn_google.bind(on_press=self.open_google_browser)

        # Skip Button (For testing without internet)
        btn_bypass = Button(
            text='[Dev Bypass]', 
            size_hint=(1, 0.1),
            background_color=(0,0,0,0),
            color=(0.3, 0.3, 0.3, 1)
        )
        btn_bypass.bind(on_press=self.bypass_login)

        layout.add_widget(self.logo)
        layout.add_widget(self.status)
        layout.add_widget(btn_google)
        layout.add_widget(btn_bypass)
        self.add_widget(layout)

    def open_google_browser(self, instance):
        self.status.text = "Browser Launched.\nCheck your open tabs."
        self.status.color = (0, 1, 0, 1)
        
        # This command sends the intent to Android to open Chrome
        # We use a generic account page for the demo so it doesn't error out on a fake ID
        webbrowser.open("https://accounts.google.com/signin") 
        
        # Simulate the "Listening" state while user is in browser
        Clock.schedule_once(self.simulate_return, 4)

    def simulate_return(self, dt):
        # In a real app, the browser would redirect back to us.
        # Here, we assume success after 4 seconds for the demo flow.
        self.manager.current = 'dashboard'

    def bypass_login(self, instance):
        self.manager.current = 'dashboard'

# --- Screen 2: The User Dashboard ---
class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # User Profile Header
        header = Label(
            text='[color=4285F4]G[/color]  Jacob Frost\n[size=14][i]jacob@frostit.app[/i][/size]', 
            markup=True, 
            size_hint_y=0.15,
            halign='center'
        )

        # The "Work" Area
        workspace = Label(
            text='[b]CONNECTED[/b]\n\nGoogle Services: [color=00ff00]LINKED[/color]\nOAuth Token: [color=ffff00]ACTIVE[/color]',
            markup=True,
            font_size='18sp'
        )

        btn_logout = Button(
            text='Sign Out',
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

class FrostitRealApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        return sm

if __name__ == '__main__':
    FrostitRealApp().run()
