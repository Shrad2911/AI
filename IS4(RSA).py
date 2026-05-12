p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))
or
p = 3
q = 11
n = p * q
phi = (p-1) * (q-1)
e = 7
d = 1
loop finds the private key d.Condition:
while (d * e) % phi != 1:
    d = d + 1

message = 5

cipher = (message ** e) % n

plain = (cipher ** d) % n

print("Value of p =", p)
print("Value of q =", q)
print("Value of n =", n)
print("Value of phi =", phi)

print("\nPublic Key (e,n) =", e, n)
print("Private Key (d,n) =", d, n)

print("\nOriginal Message =", message)

print("Encrypted Message =", cipher)
print("Decrypted Message =", plain)

The RSA Algorithm is a cryptography algorithm used for secure communication.
RSA is mainly used for:
Encryption
Decryption
Digital signatures
Secure data transfer
It is called an asymmetric encryption algorithm because it uses two keys:
Public Key → used for encryption
Private Key → used for decryption

e is the public exponent.
Conditions:
e must be less than phi
e and phi must be coprime
Here: gcd(7,20)=1  So 7 is valid.
