import google.generativeai as genai
import tweepy
import time
import random

# 1. Setup API Anchors
X_CLIENT = tweepy.Client(consumer_key="...", consumer_secret="...", access_token="...", access_token_secret="...")
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# 2. The "Amiah" Visual Narrative
DOODLE_PROMPTS = [
    "A simple, minimalist doodle of Amiah (a sleek AI mascot) riding a Frost Protocol logo to the moon, hand-drawn style, blue and silver palette.",
    "A cute Amiah robot holding a 'DOGE' sign while sitting on a Kraken, crayon drawing style.",
    "Amiah the AI assistant as a graffiti-style sketch on a neon Monroeville brick wall, vibrant and street-art inspired."
]

def release_the_flood():
    print("❄️ Amiah: Initiating Internet Flood...")
    while True:
        # Generate the visual
        prompt = random.choice(DOODLE_PROMPTS)
        model = genai.GenerativeModel('gemini-1.5-flash')
        # (In a real scenario, you'd save the image output to 'temp_doodle.png')
        
        # Craft the "Viral Hook"
        caption = random.choice([
            "Amiah is watching. The Frost Protocol is coming. #AmiahDoodle #FTC",
            "Do Only Good Everyday. Amiah does it in 0.1ms. ❄️🚀",
            "Frost OS V1.1: The cold never bothered us anyway. #FrostnerLock"
        ])
        
        # Post to the network
        try:
            # X_CLIENT.create_tweet(text=caption) # Uncomment to go live
            print(f"✅ Posted: {caption}")
        except Exception as e:
            print(f"⚠️ Rate limit or Error: {e}")

        time.sleep(1800) # Wait 30 mins to avoid spam filters

if __name__ == "__main__":
    release_the_flood()
