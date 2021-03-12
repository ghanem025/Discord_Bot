# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL
from discord import FFmpegPCMAudio
from asyncio import sleep as s

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='&',intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} is connected to the following guild:')

#@client.event
#async def on_message(message):
 #   quote = ['NO FUCK YOU HOE DONT PING ME',
 #   '...','stop pinging me pls am trying to play genshin'
  #  ,'NEXT TIME YOU PING ME AM CRASHIN THIS SERVER',
  #  'bro stop']
  #  if '<@&818409732788191253>') in message.content.split():
  #   await message.channel.send('HERRO')
  #  else:
  #      print('no ping')


@client.event
async def on_member_join(member):
    await member.create_dm()
    if member.name == "Chobaka78":
        await member.dm_channel.send(f'{member.name} welcome to server you fucking rat')
    else:
        await member.dm_channel.send(f'{member.name} welcome to my server')


@client.command()
async def members(ctx):
    guild = discord.utils.find(lambda g: g.name==GUILD, client.guilds)
    members = '\n - '.join([member.name for member in guild.members])
    await ctx.send(f'server members\n - {members}')

@client.command()
async def impact(ctx):
    quote = ['you mean genshin impact?????? ok we get it you play genshin bro', 'lol do you even have a five star???','you forgot to do your dailys dog' ]
    await ctx.send(random.choice(quote))
@client.command()
async def shutrat(ctx, id):
    #mention = <@{member.id}>
    guild = discord.utils.find(lambda g: g.name==GUILD, client.guilds)
    members = '\n - '.join([member.name for member in guild.members])
    for member in guild.members:
        await ctx.send(f'{id} {member.name} said SHUT RAT')

@client.command()
async def monke(ctx):
    memes = ['https://tenor.com/view/reject-modernity-return-to-monke-monke-gif-19167526',
    'https://tenor.com/view/obese-monkey-fat-monkey-summer-belly-eating-lettuce-summer-look-gif-13014350',
    'https://tenor.com/view/mono-gif-18377629',
    'https://tenor.com/view/monkey-pissed-mad-angry-annoyed-gif-4691438',
    'https://tenor.com/view/sad-gibbon-sad-gibbon-monkey-sad-monkey-gif-19435323',
    'https://tenor.com/view/monke-gif-19801646',
    'https://tenor.com/view/monki-flip-monkey-monkey-flip-gif-18319480',
    'https://tenor.com/view/monki-flip-gif-18400231']
    await ctx.send(random.choice(memes))

@client.command()
async def sadge(ctx):
    memes = ['https://tenor.com/view/sadgecry-sadge-cry-gif-18423674',
    'https://tenor.com/view/sadge-guitar-mills-song-pepe-gif-18595045',
    'https://tenor.com/view/sadge-sad-xqc-sad-pepe-sad-feelsbad-gif-17782875',
    'https://tenor.com/view/sadge-cliff-sad-saaadge-gif-18209034']
    await ctx.send(random.choice(memes))

@client.command(pass_context=True)
async def play(ctx, url):
    quote = ['https://www.youtube.com/watch?v=3J_7BEHLRTE',
    'https://www.youtube.com/watch?v=JjIiK9VcIsA',
    'https://www.youtube.com/watch?v=G-UN6uRMBRw',
    'https://www.youtube.com/watch?v=yM6-QVxIXTs',
    'https://www.youtube.com/watch?v=sfFv3MTPdkw']
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    YDL_OPTIONS = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],'outtmpl': 'song.%(ext)s',}

    with YoutubeDL(YDL_OPTIONS) as ydl:
        ydl.download([url])

    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send(f"Music is now playing")

@client.command()
async def remind(ctx,time: int, *, message):
    await ctx.send(f'i will remind you in {time} minute')
    await s(60*time)
    await ctx.send(f'{message}, {ctx.author.mention}')




client.run(TOKEN)


