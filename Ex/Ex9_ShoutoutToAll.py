from win32com.client import Dispatch
import time

sound = Dispatch("SAPI.SpVoice")

# l = ["Rahul", "Nishant", "Harry"]
# for i in l:
#     sound.Speak(f"Shoutout to {i}")
#     time.sleep(1)
while True:
    sound.Speak("Haare Krishna Haare Krishna, Krishna Krishna Haare Haare , Haare Rama Haare Rama ,Rama Rama Haare Haare ")
