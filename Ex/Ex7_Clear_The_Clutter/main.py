import os


def clearClutter(fileName):
    for file_Iteration in range(len(fileName)):
        os.rename(f"Clutter/{fileName[file_Iteration]}", f"Clutter/{file_Iteration}.txt")


file = os.listdir('Clutter')
clearClutter(file)
