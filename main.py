### Modules ###
import os
import time
import random
import os.path
from keep_alive import keep_alive
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import *
from discord.ext import tasks
### Modules end ###

### Startup/variables ###
ids = [
    738290097170153472,
    796442663309017131
]
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
intents = discord.Intents.all()
errHandlerVer = 'v2.4'
botVer = 'v4.1.7'
owner = 'PET GAMERS YT#5195'
theme_color = discord.Color.random()
homedir = os.path.expanduser("~")
client = commands.Bot(command_prefix=".", intents=intents)
global startTime
startTime = time.time()
client.remove_command('help')
### Startup/variables end ###

### Functions and classes ###

class colors:
    cyan = '\033[96m'
    red = '\033[91m'
    green = '\033[92m'
    end = '\033[0m'

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M:%S")

### Functions and classes end ###

## Events ###
@client.event
async def on_ready():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"cat videos"))
    print('Bot is online')
    print('==================')
    print('------------------')
    print('Bot Info')
    print(f'Bot version: {colors.cyan}{botVer}{colors.end}')
    print(f'Error handler version: {colors.cyan}{errHandlerVer}{colors.end}')
    print(f'Username: {colors.green}{client.user.name}{colors.end}\nId: {colors.green}{client.user.id}{colors.end}\nDeveloper name: {colors.green}{owner}{colors.end}')
    print('==================')
    print('Bot config:')
    print('------------------')
    print(f'Ping: {round(client.latency * 1000)}')
    print('------------------')
    boot = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    print(f'Startup time: {boot}')
    print('==================')
    print('Bot admins')
    print('------------------')
    print(colors.cyan)
    for id in ids:
        print(id)
    print(colors.end)
    print('==================')
    print('System info')
    print('Running as: ' + str(os.system("whoami")))
    print('------------------')
    print('Os name: ' + str(os.name))
    print('------------------')
    print('Current working dir: ' + str(os.getcwd()))
    print('------------------')

# Error handler #
@client.event
async def on_command_error(ctx, error):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if isinstance(error, CommandNotFound):
        print(f'[{current_time}] {colors.red}Ignoring exception at CommandNotFound. Details: This command does not exist.{colors.end}')
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f':stopwatch: Command currently on cooldown. Please try again after **{str(datetime.timedelta(seconds=int(round(error.retry_after))))}**')
        print(f'[{current_time}] {colors.red}Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown.{colors.end}')
    if isinstance(error, MissingRequiredArgument):
        await ctx.send('Your command has missing required argument(s).')
        print(f'[{current_time}] {colors.red}Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.{colors.end}')
    if isinstance(error, MissingPermissions):
        await ctx.send('You are restricted access to this command.')
        print(f'[{current_time}] {colors.red}Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.{colors.end}')
    if isinstance(error, BadArgument):
        await ctx.send('Invalid argument!')
        print(f'[{current_time}] {colors.red}Ignoring exception at BadArgument. Details: Arguments were incorrect.{colors.end}')
    if isinstance(error, BotMissingPermissions):
        await ctx.send('Oops, looks like I don\'t have to right permissions to do this command')
        print(f'[{current_time}] {colors.red}Ignoring exception at BotMissingPremissions. Details: The bot doesn\'t have the required permissions.{colors.end}')
# Error handler end #

@client.event
async def on_message(ctx):
    print(ctx.content.lower())
    if ctx.content.lower() in [
        '<@!924676808488669185> hello', 
        '<@924676808488669185> hello', 
        '@kamilla#5860 hello', 
        '<@!924676808488669185> hey', 
        '<@924676808488669185> hey', 
        '@kamilla#5860 hey', 
        '<@!924676808488669185> hi', 
        '<@924676808488669185> hi', 
        '@kamilla#5860 hi', 
        '<@!924676808488669185> hlo', 
        '<@924676808488669185> hlo',
        '@kamilla#5860 hlo', 
        '<@!924676808488669185> hai', 
        '<@924676808488669185> hai', 
        '@kamilla#5860 hai', 
        '<@!924676808488669185> heyo', 
        '<@924676808488669185> heyo',
        '@kamilla#5860 heyo', 
        '<@!924676808488669185> hallo', 
        '<@924676808488669185> hallo',
        '@kamilla#5860 hallo', 
        '<@!924676808488669185> namaste', 
        '<@924676808488669185> namaste'
        '@kamilla#5860 namaste', 
        '<@!924676808488669185> hiya', 
        '<@924676808488669185> hiya',
        '@kamilla#5860 hiya']:
        responses = [
            f'Hello {ctx.author.mention}!',
            f'Hi {ctx.author.mention}!',
            f'Heyo {ctx.author.mention}!',
            f'Namaste {ctx.author.mention}!',
            f'Hiya {ctx.author.mention}',
            f'Sup {ctx.author.mention}!'
        ]
        await ctx.reply(random.choice(responses))
    elif ctx.content.lower() in [
        '<@!924676808488669185> hru', 
        '<@924676808488669185> hru',
        '@kamilla#5860 hru', 
        '<@!924676808488669185> hry', 
        '<@924676808488669185> hry',
        '@kamilla#5860 hry', 
        '<@!924676808488669185> how r u', 
        '<@924676808488669185> how r u',
        '@kamilla#5860 how r u', 
        '<@!924676808488669185> how are you', 
        '<@924676808488669185> how are you',
        '@kamilla#5860 how are you', 
        '<@!924676808488669185> how you do', 
        '<@924676808488669185> how you do',
        '@kamilla#5860 how you do', 
        '<@!924676808488669185> how u doing', 
        '<@924676808488669185> how u doing',
        '@kamilla#5860 how u doing', 
        '<@!924676808488669185> how r you', 
        '<@924676808488669185> how r you',
        '@kamilla#5860 how r you', 
        '<@!924676808488669185> how are u', 
        '<@924676808488669185> how are u',
        '@kamilla#5860 how are u']:
        replies = [
            'I\'m fine, thanks for asking!',
            'I\'m good, thanks for asking!',
            'I\'m doing good, thanks for asking!',
            'I\'m going fine, thanks for asking!'
        ]
        await ctx.reply(random.choice(responses))
    elif ctx.content.lower() in [
        '<@!924676808488669185> good morning', 
        '<@924676808488669185> good morning',
        '@kamilla#5860 good morning', 
        '<@!924676808488669185> gm', 
        '<@924676808488669185> gm',
        '@kamilla#5860 gm']:
        replies = [
            f'Good morning {ctx.author.mention}!',
            f'Gm {ctx.author.mention}'
        ]
        await ctx.reply(random.choice(responses))
    elif ctx.content.lower() in [
        '<@!924676808488669185> good afternoon', 
        '<@924676808488669185> good afternoon',
        '@kamilla#5860 good afternoon', 
        '<@!924676808488669185> ga', 
        '<@924676808488669185> ga',
        '@kamilla#5860 ga']:
        replies = [
            f'Good afternoon {ctx.author.mention}! I hope ur day is going well.',
            f'Hi, good afternoon {ctx.author.mention}!'
        ]
        await ctx.reply(random.choice(responses))
    elif ctx.content.lower() in [
        '<@!924676808488669185> ge',
        '<@924676808488669185> ge', 
        '@kamilla#5860 ge', 
        '<@!924676808488669185> good evening', 
        '<@924676808488669185> good evening',
        '@kamilla#5860 good evening']:
        replies = [
            f'Good evening {ctx.author.mention}!',
            f'Hi, good evening {ctx.author.mention}'
        ]
        await ctx.reply(random.choice(responses))
    elif ctx.content.lower() in ['<@!924676808488669185> gn', '<@924676808488669185> gn', '@kamilla#5860 gn', '<@!924676808488669185> good night', '<@924676808488669185> good night', '@kamilla#5860 good night', '<@!924676808488669185> night', '<@924676808488669185> night', '@kamilla#5860 night', '<@!924676808488669185> imma go sleep', '<@924676808488669185> imma go sleep', '@kamilla#5860 imma go sleep']:
        replies = [
            f'Ok good night {ctx.author.mention}, sleep well :D',
            f'Alr gn {ctx.author.mention}'
        ]
        await ctx.reply(random.choice(responses))
    await client.process_commands(ctx)

### Events end ###

### Commands ###

@client.command()
async def help(ctx):
    e = discord.Embed(title='Kamilla Help', description='Here are some responses that I can reply to!\nTo communicate with me, simply ping me\n\n`hello/hi/heyo/hiya/hallo/halo/hoi/hai/hlo/namaste`, `how are you/hru/hry/how r u/how r you/how are u/how u doing/how u do`, `good morning/gm`, `good afternoon/ga`, `good evening/ge`, `good night/gn/imma go sleep/night`', color=theme_color)
    await ctx.send(embed=e)

@client.command()
async def shutdown(ctx):
    if ctx.author.id in ids:
        def check(msg):
            return msg.author == ctx.message.author and msg.channel == ctx.message.channel and (msg.content)
        await ctx.send('You sure?')
        msg = await client.wait_for("message", check=check)
        if msg.content.lower() == 'y' or msg.content == 'yes':
            await ctx.send('Shutting down the bot...')
            time.sleep(0.5)
            raise SystemExit('Bot shutdown')
        elif msg.content == 'n' or msg.content == 'no':
            await ctx.send('Ok')
        else:
            await ctx.send(f'What is {msg.content}? You are supposed to reply with yes or no.')
    else:
        return

### Commands end ###
keep_alive()
client.run('')  # Get the bot token from your discord developer portal page
