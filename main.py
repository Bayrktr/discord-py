from discord.ext import commands, tasks
import discord, io, random, time
from secret import token
from functions import *
from ChannelIdNumbers import *

prefix = '!'
bot = commands.Bot(command_prefix=prefix)
ZodiacSignNameList = ("basak", "terazi", "akrep", "yay", "oglak", "kova", "balik", "koc", "boga", "ikizler", "yengec",
                      "aslan")
helpMessage = [['Burcunun günlük yorumunu görmek için', '!burc <burçIsmi>'],
               ['Verdiğin kelime ile alakalı rastgele bir gif için', '!gif <kelime>'],
               ['Hava durumunu görmek için', '!havadurumu <İlAdı>'],
               ['Haber Paylaşma Komutları İçin', '!gamehaber ve !animehaber (Yetkili Ekibin Erişimi var)'], [
                   'Yazdığın kelimelerin boşluklu olmamasına ve türkçe karakter içermemesine dikkat et lütfeen :smiling_face_with_3_hearts:']]


@bot.event
async def on_ready():
    print("başladım {user[0}}")


"""
async def dailyMessage():
    while True:
        await asyncio.sleep(10)
        connectChannel = bot.get_channel(channelId)
        await connectChannel.send("selam")
"""


@bot.event
async def on_message(message):
    if message.author == bot.user:
        pass
    else:
        checkMessage = str(message.content).split()
        if len(checkMessage) != 0:
            if checkMessage[0] == "!phelp" and message.channel.id == gifChannelId:
                connectChannel = bot.get_channel(gifChannelId)
                embed = discord.Embed(
                    colour=discord.Colour.orange()
                )
                embed.set_author(name="Help")
                embed.add_field(name=helpMessage[0][0], value=helpMessage[0][1], inline=False)
                embed.add_field(name=helpMessage[1][0], value=helpMessage[1][1], inline=False)
                embed.add_field(name=helpMessage[2][0], value=helpMessage[2][1], inline=False)
                embed.add_field(name=helpMessage[3][0], value=helpMessage[3][1], inline=False)
                embed.add_field(name='Dikkat et', value=helpMessage[4][0], inline=False)
                await connectChannel.send(embed=embed)
                await message.delete()

            if checkMessage[0] == "!gif":
                if message.channel.id == gifChannelId and len(checkMessage) == 2:
                    connectChannel = bot.get_channel(gifChannelId)
                    embed = discord.Embed(
                    )
                    embed.set_image(url=takeGif(checkMessage[1]))
                    await connectChannel.send(embed=embed)
                    await message.delete()

            if checkMessage[0] == "!burc":
                if message.channel.id == gifChannelId and len(checkMessage) == 2:
                    if checkMessage[1] in ZodiacSignNameList:
                        connectChannel = bot.get_channel(gifChannelId)
                        await connectChannel.send(connectWebSite(checkMessage[1]))

            if checkMessage[0] == '!havadurumu':
                if message.channel.id == gifChannelId and len(checkMessage) == 2:
                    connectChannel = bot.get_channel(gifChannelId)
                    weDatas = weatherDatas(checkMessage[1])
                    if len(weDatas) != 2:
                        await connectChannel.send(weDatas)
                    else:
                        embed = discord.Embed(
                            colour=int(weDatas[1])
                        )
                        embed.set_author(name=weDatas[0][1])
                        embed.add_field(name=weDatas[0][2], value=weDatas[0][0], inline=False)
                        await connectChannel.send(embed=embed)

            if checkMessage[0] == '!helpwork':
                authority = False
                for x in message.author.roles:
                    print(x.name)
                    if x.name == "Admin":
                        authority = True
                        break
                    else:
                        pass
                if message.channel.id == develeChannelId and len(checkMessage) == 1 and authority:
                    connectChannel = bot.get_channel(develeChannelId)
                    embed = discord.Embed(
                        colour=discord.Colour.orange()
                    )
                    embed.set_author(name="WorkHelp")
                    embed.add_field(name="'", value="'", inline=False)
                    time.sleep(5)
                    await connectChannel.send(embed=embed)

            if checkMessage[0] == "!animehaber":
                authority = False
                for x in message.author.roles:
                    print(x.name)
                    if x.name == "Yönetim / Absolute Being":
                        authority = True
                        break
                    else:
                        pass
                if message.channel.id == botCommandsChannelId and len(checkMessage) == 1 and authority:
                    await dailyMessageAnime()
                    await message.delete()

            if checkMessage[0] == "!gamehaber":
                authority = False
                for x in message.author.roles:
                    print(x.name)
                    if x.name == "Yönetim / Absolute Being":
                        authority = True
                        break
                    else:
                        pass
                if message.channel.id == botCommandsChannelId and len(checkMessage) == 1 and authority:
                    await dailyMessageGame()
                    await message.delete()


async def dailyMessageAnime():
    connectChannel = bot.get_channel(animeNewsChannelId)
    a = animeNews()
    print(txtTakeListAnime())
    if a[1].translate(Tr2Eng) in txtTakeListAnime():
        pass
    else:
        msg = "{}" \
              "{} \n" \
              "{}\n" \
              "{}\n" \
              "{} \n" \
              "{}\n" \
              "\n" \
              "Kaynak : {}\n".format("**", a[1], "**", "`", a[0], "`", a[2])
        txtInsertDataAnime(a[1])
        print(msg)
        await connectChannel.send(msg)


async def dailyMessageGame():
    connectChannel = bot.get_channel(gameNewsChannelId)
    a = gameNews()
    print(a[1])
    checkList = txtTakeListAnime()
    checkListTwo = []
    for x in checkList:
        checkListTwo.append(x.strip('\n'))
    print(checkListTwo)
    if str(a[0]).translate(Tr2Eng) in checkListTwo:
        pass
    else:
        msg = "{} \n" \
              "{} \n" \
              "\n" \
              "{} \n" \
              "{} \n" \
              "{} \n" \
              "\n" \
              "Kaynak : {} \n" \
              "{}".format("**", a[0], "**", "`", a[1], "`", a[3])
        txtInsertDataGame(a[0])
        await connectChannel.send(msg)


bot.run(token)
