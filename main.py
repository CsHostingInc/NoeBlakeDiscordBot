import discord
from discord.ext import commands

TOKEN = 'Token'
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('-----------')
    print('bot is ready')
    print(f'Logged in as - {bot.user}')
    print(f'Bot ID - {bot.user.id}')
    print('-----------')


bot.run(TOKEN)

