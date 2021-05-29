import discord  
from discord.ext import commands

bot = commands.Bot(command_prefix='>', description="Esto es un Bot de Ayuda")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('ODQ4MzA2ODAyNzA4ODQwNDQ4.YLKtRg.NdnIVJhMsCSMUkDmalC1epjz5iA')