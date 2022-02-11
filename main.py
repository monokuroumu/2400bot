import os
import json
import discord
import random
import datetime
from replit import db

client = discord.Client()

def is_me(message):
  return message.author == client.user

def is_command(message):
  return message.content.startswith('!')

@client.event
async def on_ready():
  print('connected as {0.user}'.format(client))

@client.event
async def on_message(message):
  # not replying to ourselves
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(os.environ['TOKEN'])

    