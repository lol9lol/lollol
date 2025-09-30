import hashlib

# Function to compute SHA-256 hash of given data
def get_sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Original message
msg1 = "Hello World"
hash1 = get_sha256(msg1)

# Slightly modified message
msg2 = "hello World"   # only changed 'H' -> 'h'
hash2 = get_sha256(msg2)

print("Original Message :", msg1)
print("SHA-256 Hash     :", hash1)
print()
print("Modified Message :", msg2)
print("SHA-256 Hash     :", hash2)

# Check integrity
if hash1 == hash2:
    print("\n✅ Data Integrity Verified")
else:
    print("\n❌ Data Integrity Compromised (hash mismatch)")