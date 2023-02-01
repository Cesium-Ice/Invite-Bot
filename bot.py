# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
  guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
  print(
    f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})'
  )

async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
    f'Hi {member.name}, welcome to my Discord server!'
  )

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.lower() == '!invite':
    response = "Message with generated invite link"
    await message.channel.send(response)
    await message.author.create_dm()
    await message.author.dm_channel.send(f'Hi {message.author.name}, here is a temp invite link!')
client.run(TOKEN)
