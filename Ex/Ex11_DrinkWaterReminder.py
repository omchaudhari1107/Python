import time
from win32com.client import Dispatch


def IncreaseTime(afterWard):
    t = time.localtime()
    minute = int(time.strftime("%M", t))
    return minute + afterWard


sound = Dispatch("SAPI.SpVoice")
sound.Speak("After How many minute you want to drink water: ")
minutes = int(input("After How many minute you want to drink water: "))
Drinking_time = IncreaseTime(minutes)
while True:
    t = time.localtime()
    Hour = int(time.strftime("%M", t))
    if Hour == Drinking_time:
        for i in range(2):
            sound.Speak("Drrink Water")
        break
