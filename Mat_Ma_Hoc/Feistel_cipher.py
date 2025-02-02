# Feistel Cipher in Python to encrypt input text

# Helper function for Feistel round function (simple XOR with key)
def feistel_round(data, key):
    return data ^ key


# Feistel Cipher encryption function
def feistel_encrypt(plaintext, key, rounds=2):
    # Convert plaintext to integer (assumes ASCII text input)
    L = (plaintext[0] << 8) + plaintext[1]  # Left half
    R = (plaintext[2] << 8) + plaintext[3]  # Right half

    for _ in range(rounds):
        # Apply round function and XOR
        temp = R
        R = L ^ feistel_round(R, key)
        L = temp

    # Combine left and right halves
    ciphertext = (L << 16) + R
    return ciphertext


# Take input from the user
input_text = input("Enter a 4-character string to encrypt: ")

# Ensure the input is exactly 4 characters
if len(input_text) != 4:
    raise ValueError("Input string must be exactly 4 characters.")

# Convert input text to ASCII values
plaintext = [ord(char) for char in input_text]
key = 0x1234  # Example key

# Encrypt using Feistel Cipher
ciphertext = feistel_encrypt(plaintext, key)

# Output the ciphertext in hexadecimal
print(f"Ciphertext: {hex(ciphertext)}")
