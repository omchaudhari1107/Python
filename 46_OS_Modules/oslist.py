import os

folders = os.listdir("data")
print("Current directory is:", os.getcwd())  # to get current directory
for folder in folders:
    print(folder, ":", os.listdir(f"data/{folder}"))
