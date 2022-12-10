import os
import discord
from discord.ext import commands


intents = discord.Intents().all()
client = commands.Bot(command_prefix="$",
                      case_insensetive=True,
                      intents=intents)

@client.event
async def on_ready():
  print('botcado is online!')

@client.event
async def on_message(message):
  if (message.channel.id == 1034430668819668992):

    if (message.content.lower() != "avi"):
      await message.delete()
