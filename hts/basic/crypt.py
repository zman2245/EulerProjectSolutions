import argparse

def decrypt(s):
    decrypted = ""
    length = len(s)
    i = 0
    while i < length:
        val = ord(s[i]) - i
        c = chr(val)
        decrypted += c
        i += 1

    print decrypted


def encrypt(s):
    encrypted = ""
    length = len(s)
    i = 0
    while i < length:
        val = ord(s[i]) + i
        c = chr(val)
        encrypted += c
        i += 1

    print encrypted


parser = argparse.ArgumentParser(description="Encrypt/Decrypt for basic level 6 on hackthissite.")
parser.add_argument('-e', metavar='e', type=encrypt)
parser.add_argument('-d', metavar='d', type=decrypt)
args = parser.parse_args()
print args
