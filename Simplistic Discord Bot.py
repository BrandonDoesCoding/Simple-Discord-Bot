import discord
from discord.ext import commands

TOKEN = 'Please enter your discor dtokenm'
bot = commands.Bot(command_prefix='Please choose your own command prefit')

@bot.command(name='hello', help='Responds with a simple greeting.')
async def hello(ctx):
    await ctx.send('Hello, {user}!')

@bot.command(name='Template', help='A template message.')
async def custom(ctx, *args):
    response = ' '.join(args)
    await ctx.send(response)

bot.run(TOKEN)
