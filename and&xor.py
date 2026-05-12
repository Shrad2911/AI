# Program to perform AND and XOR operation with 127
text = "Hello world" OR
# Take input from user
text = input("Enter a string: ")

print("\nOriginal String :", text)

# AND Operation
print("\nAND Operation with 127:")

for ch in text:
    ascii_value = ord(ch)          # Convert character to ASCII
    and_value = ascii_value & 127  # Perform AND operation

    print("Character :", ch,
          " ASCII :", ascii_value,
          " AND Result :", and_value)

# XOR Operation
print("\nXOR Operation with 127:")

for ch in text:
    ascii_value = ord(ch)          # Convert character to ASCII
    xor_value = ascii_value ^ 127  # Perform XOR operation

    print("Character :", ch,
          " ASCII :", ascii_value,
          " XOR Result :", xor_value)


ord(ch) → converts character into ASCII value
chr() → converts ASCII value back into character
& 127 → performs AND operation with 127
^ 127 → performs XOR operation with 127
