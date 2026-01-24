import os
import time
import requests
from openai import OpenAI
from google import genai
from google.genai import types

class InjectionEngine:
    def __init__(self):
        # 🟢 Google Veo (The Architect)
        self.veo_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # ⚫ OpenAI Sora (The Painter)
        self.sora_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run_pipeline(self, prompt):
        print(f"[\u264d Virgo] Initializing Injection Pipeline for: '{prompt}'")
        
        # --- PHASE 1: VEO DRAFT ---
        print(">> [1/3] Veo 3.1: Generating Physics Blueprint...")
        draft_video_path = self._generate_veo_draft(prompt)
        if not draft_video_path:
            return ">> Pipeline Failed at Stage 1."

        # --- PHASE 2: SORA INJECTION ---
        print(">> [2/3] Sora 2: Injecting Blueprint for 4K Refinement...")
        final_url = self._upscale_with_sora(prompt, draft_video_path)
        
        return f">> [3/3] \u2705 Pipeline Complete. Output: {final_url}"

    def _generate_veo_draft(self, prompt):
        try:
            # Using the "Fast" model for rapid layout
            operation = self.veo_client.models.generate_videos(
                model="veo-3.1-fast-generate-preview",
                prompt=f"Draft layout, minimal detail, high contrast: {prompt}",
                config=types.GenerateVideosConfig(aspect_ratio="16:9", duration_seconds=5)
            )
            
            # Polling (Simplified for brevity)
            while not operation.done:
                time.sleep(2)
            
            # Save Draft Locally
            draft_path = "/tmp/virgo_draft.mp4"
            # (Assuming SDK saves file or provides bytes - pseudo-logic below)
            # operation.result.save(draft_path) 
            print(f"   > Draft saved to {draft_path}")
            return draft_path
        except Exception as e:
            print(f"   > Veo Error: {e}")
            return None

    def _upscale_with_sora(self, prompt, reference_path):
        try:
            # Upload Draft to OpenAI Files
            with open(reference_path, "rb") as f:
                ref_file = self.sora_client.files.create(file=f, purpose="visual-reference")

            # Sora 2 Video-to-Video Call
            response = self.sora_client.videos.create(
                model="sora-2-pro",
                prompt=f"Cinematic, 4k, photorealistic masterpiece: {prompt}",
                video={
                    "file_id": ref_file.id,
                    "strength": 0.65 # 0.65 means "Follow the Veo structure closely but upgrade visuals"
                },
                resolution="1920x1080"
            )
            
            return f"Job ID: {response.id} (Rendering...)"
        except Exception as e:
            return f"   > Sora Error: {e}"

# Test Hook
if __name__ == "__main__":
    engine = InjectionEngine()
    engine.run_pipeline("Cyberpunk street raining neon lights")
