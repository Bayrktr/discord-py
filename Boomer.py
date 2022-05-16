from discord.ext import commands
from secret import token
from functions import *

bot = commands.Bot(command_prefix='!')
ZodiacSignNameList = ("basak", "terazi", "akrep", "yay", "oglak", "kova", "balik", "koc", "boga", "ikizler", "yengec",
                      "aslan")

@bot.event
async def on_ready():
    print("başladım {0.user}".format(bot))

for x in ZodiacSignNameList:
    @bot.command(name=x)
    async def test(ctx, arg=connectWebSite(x)):
        await ctx.send(arg)


bot.run(token)
