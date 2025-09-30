import hashlib

def md5_hash(data: str) -> str:
    """Return MD5 hash of input string"""
    return hashlib.md5(data.encode()).hexdigest()

def sha256_hash(data: str) -> str:
    """Return SHA-256 hash of input string"""
    return hashlib.sha256(data.encode()).hexdigest()
def combined_hash(data: str) -> str:
    """Custom combination of MD5 and SHA-256"""
    md5_digest = md5_hash(data)
    sha_digest = sha256_hash(data)
    
    # Step 1: Interleave MD5 and SHA-256 (first half of MD5 + first half of SHA + ...)
    combined = ''.join(a + b for a, b in zip(md5_digest, sha_digest))
    
    # Step 2: Append remaining part of longer hash if any
    if len(md5_digest) > len(sha_digest):
        combined += md5_digest[len(sha_digest):]
    else:
        combined += sha_digest[len(md5_digest):]
    
    # Step 3: Optional: Hash the combination again with SHA-256
    final_hash = sha256_hash(combined)
    
    return final_hash
if __name__ == "__main__":
    text = "HelloWorld123"

    print("MD5 Hash:       ", md5_hash(text))
    print("SHA-256 Hash:   ", sha256_hash(text))
    print("Combined Hash:  ", combined_hash(text))