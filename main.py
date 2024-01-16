import discord
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = ''

# Replace 0 with the channel IDs and corresponding emojis
CHANNEL_EMOJIS = {
  0: '🤑',  # Emoji for Channel 1
  0: '🔥',  # Emoji for Channel 2
}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.channel.id in CHANNEL_EMOJIS:
        emoji = CHANNEL_EMOJIS[message.channel.id]
        await message.add_reaction(emoji)

bot.run(TOKEN)
