with open('file0.txt', 'r') as f:
    print(type(f))  # <class '_io.TextIOWrapper'>
    f.seek(10)  # it says from where to read the character, from 10th character the file is being read
    print(f.tell())  # it tells that from where the seeking is taking place, which is 10 in this program
    data = f.read(5)
    print(data)
with open('file1.txt', 'w') as f:
    f.write("Hello world!!")
    print(f.truncate(2))  # it says that only first 5 character is allowed in my file
