import discord
from discord.ext import commands
import requests
import datetime

# Triage configuration
TRIAGE_THRESHOLD_YEARS = 5 

@bot.command(name="triage")
@commands.has_role("🛡️ Frost Security")
async def triage_claim(ctx, btc_address: str):
    """Checks BTC address balance and stagnation for restitution eligibility."""
    try:
        # 1. Fetch Raw Blockchain Data
        url = f"https://blockchain.info/rawaddr/{btc_address}"
        data = requests.get(url).json()
        
        balance_satoshi = data.get("final_balance", 0)
        balance_btc = balance_satoshi / 100000000
        tx_count = data.get("n_tx", 0)
        
        # 2. Check for Stagnation (Last Transaction Date)
        if tx_count > 0:
            last_tx_time = data["txs"][0]["time"]
            last_tx_date = datetime.datetime.fromtimestamp(last_tx_time)
            years_stagnant = (datetime.datetime.now() - last_tx_date).days / 365
        else:
            last_tx_date = "N/A (No Transactions)"
            years_stagnant = 0

        # 3. Eligibility Logic
        is_eligible = balance_btc > 0 and years_stagnant >= TRIAGE_THRESHOLD_YEARS
        status_color = discord.Color.green() if is_eligible else discord.Color.red()

        # 4. Generate the Triage Report
        embed = discord.Embed(title=f"🔍 Triage Report: {btc_address}", color=status_color)
        embed.add_field(name="Current Balance", value=f"{balance_btc:.8f} BTC", inline=True)
        embed.add_field(name="Total Tx Count", value=str(tx_count), inline=True)
        embed.add_field(name="Years Stagnant", value=f"{years_stagnant:.2f} yrs", inline=False)
        embed.add_field(name="Restitution Status", value="✅ ELIGIBLE" if is_eligible else "❌ INELIGIBLE", inline=False)
        
        if not is_eligible:
            reason = "Insufficent Stagnation" if years_stagnant < 5 else "Zero Balance"
            embed.set_footer(text=f"Reason: {reason}")

        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send(f"⚠️ Error querying address: {str(e)}")
