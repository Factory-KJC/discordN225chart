import discord
from discord.ext import tasks
from datetime import datetime
import src.n225mpf as n225mpf
import jpholiday
from discord import File
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

TOKEN = os.getenv('DISCORDN225TOKEN')

CH_NAME = "本日の日経平均"


# 土日祝判定関数
def is_biz_day(date):
    date_formatted = datetime.strptime(date, "%Y%m%d")
    if date_formatted.weekday() >= 5 or jpholiday.is_holiday(date_formatted):
        return False
    else:
        return True


# Bot起動時の処理
@client.event
async def on_ready():
    print("Bot is ready!")
    for channel in client.get_all_channels():
        if channel.name == CH_NAME:
            await channel.send("Botが起動しました")
            break
    loop.start()

# 定期実行タスクの設定
@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '15:25':
        formatted_date = datetime.now().strftime('%Y%m%d')
        if is_biz_day(formatted_date):
            chart_image = n225mpf.n225plot()
            await send_chart_to_channels(chart_image, formatted_date)

# チャートををチャンネルに送信する関数
async def send_chart_to_channels(chart_image, formatted_date):
    for channel in client.get_all_channels():
        if channel.name == CH_NAME:
            chart_image.seek(0)
            chart_file = File(fp=chart_image, filename="n225chart.png")
            await channel.send(file=chart_file)
            await channel.send(f"{datetime.now().strftime('%Y/%m/%d')}の日経平均株価です")
            guild = channel.guild
            print(f"Successfully sent to {guild.name}!")


# Botの実行
def main():
    client.run(TOKEN)
