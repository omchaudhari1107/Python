import os

folders = os.listdir("data")
os.remove(f"data")
# Access is denied: 'data'
for folder in folders:
    os.remove(f"data/{folder}")
