import discord
from discord import channel
from discord.ext import commands

Intents = discord.Intents.all()

bot = commands.Bot(command_prefix='*', Intents = Intents)

@bot.event
async def on_ready():
    print(">>>Bot is online<<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(889083051953508382)
    await channel.send(f'[member]join!')

@bot.event
async def on_member_remove(member):
    print("[member] leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(bot.letency)

bot.run('ODg5MDUwMzU4NDc3ODkzNjMz.YUbmqw.P_G3VwQxpS2xGdnhfGrv5bg-f7c')