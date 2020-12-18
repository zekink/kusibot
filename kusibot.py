# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
    f'Hi {member.name}, welcome to {client.user.name} playground!'
  )

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  tussi = [
    'Tussi.',
    'Yeah boii!',
    'I am the great %s' % client.user.name
  ]

  if message.content == 'kusibot':
    response = random.choice(tussi)
    await message.channel.send(response)

client.run(TOKEN)