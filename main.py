import discord
from discord.ext import commands

prefix = "."
bot = commands.Bot(command_prefix=prefix)
#print(prefix)

# détecter quand le bot est prêt ("allumé")
@bot.event
async def on_ready():
    print("bot en ligne")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(".commands"))


print("lancement")

# connecte/deconnecte le bot sur un vocal
@bot.command()
async def j(ctx):
    client = ctx.guild.voice_client

    channel = ctx.author.voice.channel
    client = await channel.connect()


@bot.command()
async def d(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()




#async def create_embed(title, description):
#    embed = discord.Embed()
#   embed.title = title
#   embed.description = description
#   return embed

#   description = "bjr"
#   embed = create_embed("yo", description)
#   await message.channel.send(embed=embed)


@bot.command()
async def cnul(ctx):
    vc.play(discord.FFmpegPCMAudio("countdown.mp3"), after=lambda e: print('done', e))


@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")




# @bot.command(pass_context=True)
# async def leave(ctx):
#     server = ctx.message.server
#     voice_bot = bot.voice_client_in(server)
#     await voice_bot.disconnect()


#Pour la liste des commandes, essayer de faire une liste/tableau

@bot.command()
async def commands(ctx):
    embed = discord.Embed(title="Liste des commandes", description=".commands\n   .ia\n   .slt\n   .s\n   .tamere\n   .chinese (ajouter du text)", color=0x1058cb)
    await ctx.send(embed=embed)

@bot.command()
async def serverInfo(ctx):
    server = ctx.guild
    numberOfVoiceChannels = len(server.voice_channels)
    message = f"le serveur contient channel vocal"
    await ctx.send(message)

@bot.command()
async def chinese(ctx, *text):
    chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丁丂凵V山乂Y乙"
    chineseText = []
    for word in text:
        for char in word:
            if char.isalpha():
                index = ord(char) - ord("a")
                transformed = chineseChar[index]
                chineseText.append(transformed)
            else:
                chineseText(char)
        chineseText.append(" ")
    await ctx.send("".join(chineseText))


@bot.command()
async def slt(ctx):
    await ctx.send("Salut fdp", tts = True)

@bot.command()
async def ia(ctx):
    await ctx.send("Bonjour, je suis le bote de eisidisse, il ma programmer pour vous pirater et tousse vous détruire", tts = True)
    messages = await ctx.channel.history(limit=2).flatten()
    for message in messages:
        await message.delete()


@bot.command()
async def tamere(ctx):
    await ctx.send("Non pas les mamans", tts = True)

@bot.command()
async def s(ctx):
    await ctx.send("sssserpent")

@bot.command()
async def ghost(ctx):
    await ctx.send("fantôme gautier APPARAÎT...")


# donner le token pour qu'il se connecte


# connecter au serveur
bot.run(process.env.TOKEN)


#chose a rajouter: faire en sorte que le bot passe un son dans le vocal
