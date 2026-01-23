import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your Gemini API Key from your .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# System Instructions for Amiah
AMIAH_SYSTEM_PROMPT = """
You are Amiah, the core AI assistant for Frost OS. 
You are an expert in the Frost Protocol, cryptocurrency restitution, and the 
Do Only Good Everyday (DOGE) principle. Your goal is to help Jacob Frost 
manage his network and support Hall of DPRs researchers.
"""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=AMIAH_SYSTEM_PROMPT
)

def launch_amiah():
    chat = model.start_chat(history=[])
    print("❄️ Amiah: Systems Online. How can I assist with Frost OS today?")
    
    while True:
        user_input = input("User > ")
        if user_input.lower() in ["exit", "quit", "sleep"]:
            break
            
        response = chat.send_message(user_input, stream=True)
        print("Amiah > ", end="")
        for chunk in response:
            print(chunk.text, end="", flush=True)
        print("\n")

if __name__ == "__main__":
    launch_amiah()
