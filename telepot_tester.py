import json
import telepot, os
from time import sleep
from telepot.loop import MessageLoop


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False



if os.path.exists("./config.json"):
    svd = input("Use saved config file? Y/n ")
    if svd.lower() == "y" or svd == "1":
        usdcfg=True
        credentials = json.load(open("config.json", "r"))

        token_ = credentials["token"]
        chat_id_ = credentials["chat_id"]

    else:
        token_ = input("BOT TOKEN : ")
        chat_id_ = input("OWNER ID  : ")

bot = telepot.Bot(token_)

def bsend(msg):
    bot.sendMessage(chat_id_, msg)

refresh_seconds = input("REFRESH RATE (s) : ")

if not(usdcfg):
    svin = input("DO you want to save this credentials in a configuration file? Y/n ")

    if svin.lower() == "y":
        print("Saving...")

        config_content = {
            "token" : token_,
            "chat_id" : chat_id_
        }

        with open("config.json", "w") as configfile:
            json.dump(config_content, configfile)
        
        print("Done!")


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    

if isfloat(refresh_seconds):
    rfrsh = float(refresh_seconds)
else:
    rfrsh = int(refresh_seconds)

while 1:
    sleep(rfrsh)
    cmd = input("> ")

    if cmd.startswith("bsend "):
        msg_ = cmd[6:]
        bsend(msg_)
    elif cmd.startswith("ssend "):
        msg_ = cmd.replace("ssend ", "")[11:]
        chid = cmd.replace("ssend ", "").replace(msg_, "")
        
        bot.sendMessage(int(chid), msg_)



MessageLoop(bot, handle).run_as_thread()