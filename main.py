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

@bot.command()
async def eco_time(ctx):
    await ctx.send('Виды отходов	Период разложения')
    await ctx.send('Пищевые отходы 	     до 1 месяца')
    await ctx.send('Газетная бумага 	 до 1 года')
    await ctx.send('Картонные коробки 	 до 1 года')
    await ctx.send('Бумага	             2 года')
    await ctx.send('Доски деревянные 	 до 10 лет')
    await ctx.send('Железная арматура	 до 10 лет')
    await ctx.send('Железные банки	     до 10 лет')
    await ctx.send('Старая обувь	     до 10 лет')
    await ctx.send('Старая обувь	     до 10 лет')
    await ctx.send('Автоаккумуляторы 	 до 100 лет')
    await ctx.send('Фольга 	             до 100 лет')
    await ctx.send('батарейки 	         до 100 лет')
    await ctx.send('Резиновые покрышки	 более 100 лет')
    await ctx.send('Пластиковые бутылки	 более 100 лет')
    await ctx.send('Полиэтилен 	         200 лет')
    await ctx.send('Алюминиевые банки	 500 лет')
    await ctx.send('Стекло	             1000 лет')

@bot.command()
async def eco_pollution(ctx):
    await ctx.send('10. Красочная промышленность')
    await ctx.send('9. Промышленное производство товаров')
    await ctx.send('8. Химическое производство')
    await ctx.send('7. Промышленные зоны')
    await ctx.send('6. Промышленные свалки')
    await ctx.send('5. Традиционная добыча золота')
    await ctx.send('4. Кожевенные заводы')
    await ctx.send('3. Выплавка свинца')
    await ctx.send('2. Добыча и обработка руды')
    await ctx.send('1. Использованные свинцово-кислотные батареи')

#@bot.command()
#async def eco_pollution(ctx):
#   await ctx.send()

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
    await ctx.send('$roll _d_ - кидает кость')
    await ctx.send('$eco_time - время разложения предметов')
    await ctx.send('$eco_pollution - причины загризнений')
    await ctx.send('$eco_what "любая среда" - что загрязняет что')
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

bot.run("")
