def atbash_cipher(message):
    ans = ""
    for i in message:
        if i.isalpha():
            base = ord("A") if i.isupper() else ord("a")
            ans += chr(25 - ord(i) + 2*base)
        else:
            ans += i
    return ans

print(atbash_cipher("Angela"))
print(atbash_cipher("Zmtvoz"))
