def caesar_cipher(message, shift):
    ans = ""
    for i in message:
        if i.isalpha():
            base = ord("A") if i.isupper() else ord("a")
            ans += chr((ord(i)-base+shift)%26 + base)
        else:
            ans += i
    return ans

print(caesar_cipher("iuw456@#$wer", 3)) #encrypt
print(caesar_cipher("iuw456@#$wer", -3)) #decrypt
