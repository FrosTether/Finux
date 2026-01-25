import os
from xai_sdk import Client

# Initialize Grok 4.1 Client
client = Client(api_key=os.getenv("XAI_API_KEY"), timeout=3600)

def process_workload(data, local_confidence):
    # Threshold for offloading (e.g., if NPU model is < 85% sure)
    if local_confidence < 0.85:
        print(">> [OFFLOADING] Local NPU uncertain. Escalating to Grok 4.1...")
        
        # Grok 4.1 Thinking mode handles complex data analysis
        chat = client.chat.create(model="grok-4.1-thinking")
        chat.append([{"role": "user", "content": f"Analyze this NPU sensor data: {data}"}])
        
        return chat.sample().message.content
    else:
        return ">> [LOCAL] NPU Task Completed."
