import requests
import discord
import pyowm
import time
from colorama import *

init()
print(Fore.WHITE)
print(Back.RED + "		Бот запущен!")
print(Back.GREEN + "		Чтобы остановить бота нажмите:")
print(Back.BLUE + "		Ctrl + c")

client = discord.Client()
owm = pyowm.OWM('1185ea9bbccb63c2181abff7cf05b7a4', language="ru")

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

@client.event
async def on_message(message):
    if message.content.startswith('/pogoda ufa'):
        observation = owm.weather_at_place('Ufa,RUS')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        await message.channel.send("В городе Уфа сейчас " + w.get_detailed_status())
        await message.channel.send("Температура сейчас примерно " + str(temp) + " градусов ")
        if temp <= 0:
            await message.channel.send("На улице очень холодно, одевайся как танк")
        elif temp < 10:
            await message.channel.send("Сейчас очень холодно, одевайся тепло")
        elif temp < 20:
            await message.channel.send("Сейчас холодновато, одевайся потеплее")
        elif temp > 20:
            await message.channel.send("Сейчас на улице жарко, одень только кепку")
        elif temp > 30:
            await message.channel.send("На улице как в Сахаре, лучше посидеть дома")
    elif message.content.startswith('/pogoda moscow'):
        observation = owm.weather_at_place('Moscow,RUS')
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]

        await message.channel.send("В городе Москва сейчас " + w.get_detailed_status())
        await message.channel.send("Температура сейчас примерно " + str(temp) + " градусов ")

        if temp <= 0:
            await message.channel.send("На улице очень холодно, одевайся как танк")
        elif temp < 10:
            await message.channel.send("Сейчас очень холодно, одевайся тепло")
        elif temp < 20:
            await message.channel.send("Сейчас холодновато, одевайся потеплее")
        elif temp > 20:
            await message.channel.send("Сейчас на улице жарко, одень только кепку")
        elif temp > 30:
            await message.channel.send("На улице как в Сахаре, лучше посидеть дома")
    elif message.content.startswith('/coronovirus'):
        await message.channel.send("Мы все умрем от короновируса!!!!!!! АХАХАХАХ)))))))")

client.run('NjkzODU5MzkyMTg5MzY2MzMy.XoDNIA.E_GXrXZYQrSuq-xxwAI13f5K1DQ')

on = 1
while on == 1:
    print("Прошло 10 минут")
    time.sleep(600)