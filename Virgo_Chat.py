    def send_message(self, instance):
        msg = self.input_box.text
        self.input_box.text = ""
        self.update_log(f"> YOU: {msg}")

        # --- NEW COMMANDS ---
        if "/inject" in msg:
            # Trigger the Hybrid Pipeline
            prompt = msg.replace("/inject", "").strip()
            self.update_log(f"[\u264d SYSTEM]: Starting Veo-to-Sora Injection...")
            
            # Run in background to not freeze UI (Threaded)
            import threading
            threading.Thread(target=self._run_injection, args=(prompt,)).start()

        elif "/video" in msg:
            # ... (Existing logic) ...
            pass
        else:
            # ... (Existing Grok logic) ...
            pass

    def _run_injection(self, prompt):
        from Virgo_Injection_Engine import InjectionEngine
        engine = InjectionEngine()
        result = engine.run_pipeline(prompt)
        # Use Clock to update UI from background thread
        Clock.schedule_once(lambda dt: self.update_log(f"[\u264d RESULT]: {result}"))
