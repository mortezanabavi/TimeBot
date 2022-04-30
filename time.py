from pyrogram import Client, filters
from time import sleep
from datetime import datetime
import schedule
import pytz

bot = Client(
    name = "BotSession",
    api_id = ,
    api_hash = "",
    no_updates = True
)


def job():
    with bot:
        now = datetime.now(pytz.timezone("Asia/Tehran"))
        formatted_Time = now.strftime("%I:%M")
        bot.update_profile(last_name = f" | {formatted_Time}")


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    sleep(1)
