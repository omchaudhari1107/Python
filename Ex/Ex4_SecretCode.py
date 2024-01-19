import random
import string

password = input("Enter password for encryption: ")


def Encoding(a, size):
    letter = string.digits + string.ascii_lowercase
    rmd = ''.join(random.choice(letter) for _ in range(size))
    a = a[:len(a)] + a[0]
    a = rmd[:2] + a[1:len(a)] + rmd[3:len(rmd)]
    return a


def Decoding(a, size):
    a = a[2:len(a[3:len(a)])]
    charc = a[len(a) - 1]
    a = charc + a
    a = a[:len(a) - 1]
    return a


if len(password) > 3:
    codedString = Encoding(password, 6)
    print(f"Encoding a string:{codedString}")
    EncodedString = Decoding(codedString, 6)
    print(f"Decoding a string:{EncodedString}")
else:
    codedString = password[::-1]
    print(f"Encoding a string:{codedString}")
    EncodedString = password[::1]
    print(f"Decoding a string:{EncodedString}")
