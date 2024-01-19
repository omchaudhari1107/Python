f = open('hello.txt', 'rt')  # or rb-read binary(image file etc..)
# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# create (x): This mode creates a file and gives an error if the file already exists.
# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
# binary (b): used to handle binary files (images, pdfs, etc).

# read a file
text = f.read()
print(text)

# write to a file
f1 = open('hello1.txt', 'w')
f1.write(text)
f1.close()

# write to a file using append mode
f2 = open('hello2.txt', 'w')  # it appends the file means not overwrite
f2.write(text)
f2.close()

# using "with" keyword we do not need to close a file using .close
f3 = open('hello3.txt', 'wt')
with open('hello3.txt', 'wt'):
    f3.write("Hello world!")
