def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Take input
p = int(input("Enter prime number p: "))

# Check prime
if not is_prime(p):
    print("Error: Enter a prime number!")
else:
    g = int(input("Enter generator number g: "))
    A = int(input("Enter private key of A: "))
    B = int(input("Enter private key of B: "))

    # Calculate public keys
    public_key_A = pow(g, A, p)
    public_key_B = pow(g, B, p)

    # Calculate shared secret keys
    secret_A = pow(public_key_B, A, p)
    secret_B = pow(public_key_A, B, p)

    # Print results
    print(f"Public key of A : {public_key_A}")
    print(f"Shared secret A : {secret_A}")
    print(f"Public key of B : {public_key_B}")
    print(f"Shared secret B : {secret_B}")
