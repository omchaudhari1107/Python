# readline(),writeln()

f0 = open('file.txt', 'rt')
f1 = open('file1.txt', 'wt')
while True:
    line = f0.readline()
    if not line:
        break
    f1.writelines(line)
print("File Content Copied!!")
