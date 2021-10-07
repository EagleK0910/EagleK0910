import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import datetime

with open('setting.json',mode= 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (毫秒)')
        
    @commands.command()
    async def hi(self, ctx):
        await ctx.send('1234')
        
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="SAO諮詢群", url="https://discord.gg/erVN9PyAJd", description="連結網址", color=0xff00ea)
        embed.set_author(name="資訊", icon_url="https://media.discordapp.net/attachments/894199025463623730/895307699166789652/882991365351420005.png")
        embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/0ohIbwppTohDwC7vAO8e8VbFW58B-CRSaPNZUNoib00/https/truth.bahamut.com.tw/s01/202107/51312f32f8441de0f904fe808fa42ef9.JPG?width=1251&height=663")
        embed.add_field(name="NO.1", value="test1", inline=True)
        embed.add_field(name="NO.2", value="test2", inline=True)
        embed.add_field(name="NO.3", value="test3", inline=False)
        embed.add_field(name="NO.4", value="test4", inline=False)
        embed.set_footer(text="作者: ﷼星ོꦿ痕ོꦿ❧#7636")
        await ctx.send(embed=embed)
        
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)
        
    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)
        
    @commands.command()
    async def rand_squad(self, ctx):
        for member in ctx.guild.members:
            print(member.status)
        
def setup(bot):
    bot.add_cog(Main(bot))