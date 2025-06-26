import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))  # Optional: add to .env for guild-specific sync

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Set presence (idle + watching)
@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(type=discord.ActivityType.watching, name="over 𝑒𝑒𝓅𝓎 𝓃𝒶𝓉𝒾𝑜𝓃")
    )
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")
    print(f"Bot is ready. Logged in as {bot.user}.")

# Slash command
@bot.tree.command(name="test-command", description="Test out the bot", guild=discord.Object(id=GUILD_ID))
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("Bot is functional", ephemeral=True)

bot.run(TOKEN)
