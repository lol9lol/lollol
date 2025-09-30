def gcd(a,b):
    result = min(a,b)
    while result > 1:
        if a%result == 0 and b% result == 0:
            break
        result -= 1
    return result

p = int(input("Enter prime number1 p: "))
q = int(input("Enter prime number2 q:"))

n = p * q
quotient_fn = (p - 1) * (q - 1)

for e in range(2, quotient_fn):
    if gcd(quotient_fn, e) == 1:
        break

k = 1
while True:
    d = (1 + quotient_fn * k) / e
    if d == int(d):
        d = int(d)
        break
    k += 1

print(f"Public key: ({e}, {n})")
print(f"Private key: ({int(d)}, {n})")


