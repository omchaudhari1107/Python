import time

timeStrap = time.strftime('%H:%M')
hour = int(time.strftime('%H'))
if 0 <= hour <= 12:
    print("Good Morning! The time is", timeStrap, "AM")
elif 12 < hour < 17:
    print("Good Afternoon! The time is", timeStrap, "PM")
elif 17 <= hour <= 24:
    print("Good Night! The time is", timeStrap, "PM")
else:
    print('Error')
