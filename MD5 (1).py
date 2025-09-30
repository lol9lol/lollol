import hashlib

# Function to compute MD5 hash of given data
def get_md5(data):
    return hashlib.md5(data.encode()).hexdigest()

# Original message
msg1 = "Hello World"
hash1 = get_md5(msg1)

# Slightly modified message
msg2 = "hello World"   # only changed 'H' -> 'h'
hash2 = get_md5(msg2)

print("Original Message :", msg1)
print("MD5 Hash         :", hash1)
print()
print("Modified Message :", msg2)
print("MD5 Hash         :", hash2)

# Check integrity
if hash1 == hash2:
    print("\n✅ Data Integrity Verified")
else:
    print("\n❌ Data Integrity Compromised (hash mismatch)")