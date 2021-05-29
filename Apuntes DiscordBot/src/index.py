from env import (_botKey)
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='>', description="Esto es un Bot de Ayuda")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(_botKey)