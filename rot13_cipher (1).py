def rot13_cipher(message):
    ans = ""
    for i in message:
        if i.isalpha():
            base = ord("A") if i.isupper() else ord("a")
            ans += chr((ord(i)-base+13)%26 + base)
        else:
            ans += i
    return ans

print(rot13_cipher("Angelajoshi31"))
print(rot13_cipher("Natrynwbfuv"))
