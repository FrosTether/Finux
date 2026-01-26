from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class FrostSearchInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.debounce_event = None
        self.debounce_delay = 0.5  # 500ms delay

    def on_text(self, instance, value):
        # Cancel the pending AI call if the user is still typing
        if self.debounce_event:
            self.debounce_event.cancel()
        
        # Schedule the AI search for 0.5 seconds from now
        self.debounce_event = Clock.schedule_once(
            lambda dt: self.trigger_ai_search(value), 
            self.debounce_delay
        )

    def trigger_ai_search(self, query):
        if not query.strip():
            return
        print(f"📡 [UPLINK] Sending search to AI: {query}")
        # Insert your AI API call logic here
