import subprocess
import discord
from discord.ext import commands

@bot.command(name="mint")
@commands.has_role("🛡️ Frost Security")
async def approve_and_mint(ctx, btc_address: str, ftc_wallet: str, amount: float):
    """Triggers the Python minting script for an approved restitution claim."""
    try:
        # 1. Verification Logging
        await ctx.send(f"🔨 **Initiating Minting Protocol** for {ftc_wallet}...")
        
        # 2. Execute the restitution script as a subprocess
        # This passes the wallet and amount directly to your local Python core
        result = subprocess.run(
            ['python3', 'restitution_logic.py', '--wallet', ftc_wallet, '--amount', str(amount)],
            capture_output=True, text=True
        )

        # 3. Handle Script Response
        if result.returncode == 0:
            embed = discord.Embed(title="❄️ Restitution Successful", color=0x00ff00)
            embed.add_field(name="FTC Distributed", value=f"{amount} FTC", inline=True)
            embed.add_field(name="Tx Hash", value=result.stdout.strip(), inline=False)
            embed.set_footer(text="Identity Verified via voluntaryist.base.eth")
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"❌ **Minting Failed:** {result.stderr}")

    except Exception as e:
        await ctx.send(f"⚠️ **System Error:** {str(e)}")
