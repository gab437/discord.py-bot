import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!", case_insensitive=True)

@client.event
async def on_ready():
  print('o bot {0.user} está online!'.format(client))

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cog.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cog.{extension}')


for nome in os.listdir('./cog'):
  if nome.endswith('.py'):
   client.load_extension(f'cog.{nome[:-3]}')


client.run('TOKEN_DO_SEU_BOT')
