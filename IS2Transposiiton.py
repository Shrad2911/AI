# Program to perform AND and XOR operation with 127

def encrypt(plaintext, key):
    columns = len(key)
    rows = len(plaintext) // columns + 1

    while len(plaintext) < rows * columns:
        plaintext = plaintext + 'x'

    matrix = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(plaintext[index])
            index = index + 1
        matrix.append(row)

    order = []
    for i in range(columns):
        count = 0
        for j in range(columns):
            if key[j] < key[i]:
                count = count + 1
        order.append(count)

    ciphertext = ""
    for num in range(columns):
        for i in range(columns):
            if order[i] == num:
                for j in range(rows):
                    ciphertext = ciphertext + matrix[j][i]

    return ciphertext

plaintext = input("Enter message: ")
key = input("Enter key: ")

ciphertext = encrypt(plaintext, key)

print("Ciphertext:", ciphertext)

OR
plaintext = "informationsecurity"
key = "lock"

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

Transposition cipher is an encryption method where:
✅ Characters are not changed
✅ Only their positions are changed
Encryption means:Original Message → Secret Message
Using transposition:
letters remain same
order changes
Types of Transposition Cipher
Rail Fence Cipher
Columnar Transposition Cipher
Transposition cipher was mainly used in:
Old military communication
Classical cryptography systems
Educational purposes
Learning encryption concepts
Puzzle and secret message systems
Today, it is mostly used for: teaching cryptography

“It provides basic security by rearranging characters, but it is not secure enough for modern applications because it can be broken easily 
using frequency and pattern analysis
