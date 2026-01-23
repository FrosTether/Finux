import discord
import requests
import asyncio
import os
from dotenv import load_dotenv

# Load sensitive tokens from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
KRAKEN_ADDR = "334BSEeNo9wMhASUH9tCA7CKCMKuuARyRg"
CHANNEL_ID = 123456789012345678 # Replace with your #rewards-feed channel ID

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_rewards():
    """Polls the blockchain every 5 minutes for balance changes."""
    last_balance = 0
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    
    while not client.is_closed():
        try:
            # Query Blockchain API
            url = f"https://blockchain.info/q/addressbalance/{KRAKEN_ADDR}"
            response = requests.get(url)
            current_balance = int(response.text) / 100000000 # Convert Satoshi to BTC
            
            if current_balance > last_balance and last_balance != 0:
                reward_amount = current_balance - last_balance
                embed = discord.Embed(title="❄️ Frost Reward Verified!", color=0x00ff00)
                embed.add_field(name="Amount", value=f"{reward_amount:.8f} BTC")
                embed.add_field(name="Vault", value="Kraken Primary")
                embed.set_footer(text="Do Only Good Everyday (DOGE)")
                await channel.send(embed=embed)
            
            last_balance = current_balance
        except Exception as e:
            print(f"Connection Error: {e}")
            
        await asyncio.sleep(300) # Wait 5 minutes

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    client.loop.create_task(check_rewards())

client.run(TOKEN)
