from discord.ext import commands, tasks
import discord, io
from secret import token
from functions import *
import asyncio, aiohttp

bot = commands.Bot(command_prefix='!')
ZodiacSignNameList = ("basak", "terazi", "akrep", "yay", "oglak", "kova", "balik", "koc", "boga", "ikizler", "yengec",
                      "aslan")
channelId = 800639394699935778
susleme = "**"  # 50 eleman var
ever = "@everyone"  # 8 eleman var


@bot.event
async def on_ready():
    print("başladım {0.user}".format(bot))
    await dailyMessageGame()


for x in ZodiacSignNameList:
    @bot.command(name=x)
    async def test(ctx, arg=connectWebSite(x)):
        await ctx.send(arg)

"""
async def dailyMessage():
    while True:
        await asyncio.sleep(10)
        connectChannel = bot.get_channel(channelId)
        await connectChannel.send("selam")
"""


async def dailyMessageGame():
    connectChannel = bot.get_channel(channelId)
    uselessList = []
    while True:
        a = gameNews()
        if a[0] in uselessList:
            pass
        else:

            msg = "{}" \
                  "{}\n" \
                  "\n" \
                  "{}" \
                  "{} {}".format(susleme, a[0], a[1], ever, susleme)
            uselessList.append(a[0])
            print(msg)
            await connectChannel.send(msg)

            # send image from url
            async with aiohttp.ClientSession() as session:
                async with session.get(a[2]) as resp:
                    data = io.BytesIO(await resp.read())
                    await connectChannel.send(file=discord.File(data, '31.png'))
            # -----------------------------------------------

        await asyncio.sleep(rutin)


bot.run(token)
