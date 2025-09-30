def caesar_cipher(text, shift):
    out = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            out += chr((ord(c) - base + shift) % 26 + base)
        else:
            out += c
    return out
def atbash_cipher(text):
    out = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            out += chr(25 - (ord(c) - base) + base)
        else:
            out += c
    return out
def rot13_cipher(text):
    return caesar_cipher(text, 13)
msg = "Hello World"
print("Caesar (+3):", caesar_cipher(msg, 3))
print("Atbash:", atbash_cipher(msg))
print("ROT13:", rot13_cipher(msg))
