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
    #todo: change this so I grab this channel from the client permissions, instead of hardcoding
    channel = client.get_channel(1070253269907161118)

    link = await channel.create_invite(max_age=86400, max_uses=1)

    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    response = f"Hi {message.author.name}, here is an invite for {guild.name}: {link}\n Please note that this invite can only be used once and expires in 24 hours."
    await message.channel.send(response)
    # await message.author.create_dm()
    # await message.author.dm_channel.send(f'Hi {message.author.name}, here is a temp invite link!')

client.run(TOKEN)
