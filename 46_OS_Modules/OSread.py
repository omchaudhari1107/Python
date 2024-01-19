import os

folders = os.listdir("data")

for folder in folders:
    print(os.listdir(f"data/{folder}"))
