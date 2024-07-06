import discord
from discord.ext import tasks
from datetime import datetime
import n225mpl
import jpholiday

intents = discord.Intents.all()
client = discord.Client(intents=intents)

TOKEN = "APP_TOKEN" # Replace APP_TOKEN with your discord app token

CH_NAME = "本日の日経平均"


DATE = "yyyymmdd"

# 土日祝判定
def isBizDay(DATE):
    date_str = DATE
    date_formatted = datetime.strptime(date_str, "%Y%m%d")
    #Date = datetime.date(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8]))
    if date_formatted.weekday() >= 5 or jpholiday.is_holiday(date_formatted):
        return 0
    else:
        return 1


# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    for channel in client.get_all_channels():
        if channel.name == CH_NAME:
            await channel.send("起動しました")
            break
    print("Ready!")
    loop.start()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '15:01':
        formateddate = datetime.now().strftime('%Y%m%d')
        if isBizDay(formateddate) == 1:
            img_in = n225mpl.n225plot()
            img_in.seek(0)
            ch_name = CH_NAME
            for channel in client.get_all_channels():
                if channel.name == ch_name:
                    await channel.send(file=discord.File(img_in,"test.png"))
                    await channel.send("本日の日経平均株価です")
                    break
            guild = client.guilds
            current_guild = guild[0]
            guild_name = current_guild.name
            print("Succcessfully sent to " + guild_name + "!")



client.run(TOKEN)
