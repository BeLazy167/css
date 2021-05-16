import hashlib  
g=int(input("Enter value of g: "))
p=int(input("Enter value of p: "))
a=int(input("Enter random number for alice: "))
b=int(input("Enter random number for bob: "))
A = (g**a) % p 
B = (g**b) % p 
print('g: ',g,' (a shared value), n: ',p, ' (a prime number)') 
print('\nAlice calculates:') 
print('a (Alice random): ',a) 
print('Alice value (A): ',A,' (g^a) mod p') 
print('\nBob calculates:') 
print('b (Bob random): ',b) 
print('Bob value (B): ',B,' (g^b) mod p') 
print('\nAlice calculates:') 
keyA=(B**a) % p 
print('Key: ',keyA,' (B^a) mod p') 
print('Key: ',hashlib.sha256(str(keyA).encode()).hexdigest()) 
print('\nBob calculates:') 
keyB=(A**b) % p 
print('Key: ',keyB,' (A^b) mod p') 
print('Key: ',hashlib.sha256(str(keyB).encode()).hexdigest())