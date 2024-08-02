import os
import random
import discord
from discord.ext import commands

# from bot_logic import gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет!')

@bot.command()
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

    if not message.content.startswith(bot.command_prefix):
        await message.channel.send(message.content)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def catalog(ctx):
    await ctx.send('все команды вводятся через $:')
    await ctx.send('$catalog - список команд')
    await ctx.send('$hello - приветствие')
    await ctx.send('$bye - смайлик')
    await ctx.send('$joined @user_name - сообщает о времени присоеденения польвователя к серверу')
    await ctx.send('$meme - отпровляет рандомный мем')
    await ctx.send('$roll ?d? - кидает кость')
    await ctx.send('бот также копирует все отправленные сообщения')

@bot.command()
async def meme(ctx):
    files = os.listdir("mems")

    with open("mems/" + random.choice(files), "rb") as f:
        picture = discord.File(f)
    await ctx.send(file = picture)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

bot.run("MTI2MTY3NjQ5NzExNTE1NjUwMg.GeYIzq.foBu0k0TvSbQHJ27I4cksi7_SQ9OXnwo1HUPA8")
