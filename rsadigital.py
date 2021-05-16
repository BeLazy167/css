from Crypto.PublicKey import RSA 
from hashlib import sha512 

keyPair = RSA.generate(bits=1024) 
print(f"Public key: (n={hex(keyPair.n)}, e={hex(keyPair.e)})") 
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")


# RSA sign the message 
msg = b'This is America' 
hash = int.from_bytes(sha512(msg).digest(), byteorder='big') 
signature = pow(hash, keyPair.d, keyPair.n) 
print("Signature:", hex(signature)) 


# RSA verify signature 
msg = b'A message' 
hash = int.from_bytes(sha512(msg).digest(), byteorder='big') 
hashFromSignature = pow(signature, keyPair.e, keyPair.n) 
print("Signature valid:", hash == hashFromSignature) 

# RSA verify signature (tampered msg)
msg = b'A message (tampered)' 
hash = int.from_bytes(sha512(msg).digest(), byteorder='big') 
hashFromSignature = pow(signature, keyPair.e, keyPair.n) 
print("Signature valid (tampered):", hash == hashFromSignature)