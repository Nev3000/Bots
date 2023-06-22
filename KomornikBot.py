import discord
from discord.ext import commands
import asyncio
from datetime import datetime
import random

TOKEN = ""

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

base_message = "Cześć, proszę o przekazanie środków finansowych."

paraphrased_messages = [
    "Hej, czy mogę prosić o przesłanie funduszy?",
    "Witam, będę wdzięczny za przekazanie środków.",
    "Dzień dobry, proszę o wysłanie pieniędzy.",
    "Siema, potrzebuję hajsu, możesz przesłać?",
    "Witaj, czy byłbyś uprzejmy przelać mi pewną sumę pieniędzy?",
    "Halo, potrzebuję wsparcia finansowego, czy mógłbyś pomóc?",
    "Witam serdecznie, czy mógłbyś przesłać mi pewną kwotę pieniędzy?",
    "Cześć, czy mogłabyś wysłać mi jakieś fundusze?",
    "Dobry dzień, potrzebuję trochę gotówki, czy możesz przelać?",
    "Witaj, czy byłbyś tak miły i przesłał mi pewną ilość pieniędzy?"
]

def send_message():
    while True:
        now = datetime.now()
        if now.day == 8 and now.hour == 3:
            # Wybieranie losowej parafrazy
            paraphrased_message = random.choice(paraphrased_messages)
            # Pobieranie losowego użytkownika do wysłania wiadomości
            user = random.choice(bot.users)
            channel = user.dm_channel
            if channel is None:
                channel = await user.create_dm()
            asyncio.run_coroutine_threadsafe(channel.send(paraphrased_message), bot.loop)
        asyncio.sleep(3600)  # Pauza 1 godzina

@bot.event
async def on_ready():
    print("Bot gotowy.")

@bot.command()
async def start(ctx):
    await ctx.send("Rozpoczynam automatyczne wysyłanie wiadomości.")
    bot.loop.create_task(send_message())

@bot.command()
async def stop(ctx):
    await ctx.send("Zatrzymuję automatyczne wysyłanie wiadomości.")
    for task in asyncio.all_tasks():
        task.cancel()

bot.run(TOKEN)
