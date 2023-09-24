import telepot
from time import sleep
from pprint import pprint
from telepot.loop import MessageLoop

TOKEN = ""

bot = telepot.Bot()

def handle(msg):
    pprint(msg)


MessageLoop(bot, handle).run_as_thread()

pprint(bot.getMe())
#bot.sendMessage(518431247, "Ciao peppino")

while 1:
    sleep(0.5)
