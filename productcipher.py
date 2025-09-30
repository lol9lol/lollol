import string, random

# Simple substitution (Caesar shift 3)
sub_key = {c: string.ascii_uppercase[(i+3)%26] for i, c in enumerate(string.ascii_uppercase)}
inv_sub_key = {v: k for k, v in sub_key.items()}

def substitution(text, key):
    return ''.join(key.get(c, c) for c in text)

def transposition_encrypt(text, key=4):
    return ''.join(text[i::key] for i in range(key))

def transposition_decrypt(text, key=4):
    rows = len(text) // key + (len(text) % key > 0)
    chunks = [text[i*rows:(i+1)*rows] for i in range(key)]
    return ''.join(''.join(chunks[j][i] for j in range(key) if i < len(chunks[j])) for i in range(rows))

# Product Cipher
def encrypt(text): return transposition_encrypt(substitution(text, sub_key))
def decrypt(text): return substitution(transposition_decrypt(text), inv_sub_key)

# Example
msg = "HELLO WORLD"
enc = encrypt(msg)
dec = decrypt(enc)

print("Plaintext:", msg)
print("Encrypted:", enc)
print("Decrypted:", dec)