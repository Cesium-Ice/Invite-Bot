# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
  print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})'
  )

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  print ("message detected: {}\n".format(message.content))
  if message.content == '!invite':
    response = "Message with generated invite link"
    await message.channel.send(response)
    # await message.author.create_dm()
    # await message.author.dm_channel.send(f'Hi {message.author.name}, here is a temp invite link!')

client.run(TOKEN)
