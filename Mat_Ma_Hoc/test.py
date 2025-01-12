hex_data = "0018195b0b55312a2601472675220310134c4b6231206514161037563c361a081815132206515d0018195b0b55312a2601472675220310134c4b6231206514161037563c361a081815132206515d0018195b0b55312a2601472675220310134c4b6231206514161037563c361a081815132206515d0018195b0b55312a2601472675220310134c4b6231206514161037563c361a081815132206515d0018195b0b55312a2601472675220310134c4b6231206514161037563c361a081815132206515d0018195b0b55312a2601472675220310134c4b6231206514161037563c361a081815132206515d0018195b0b55312a2601472675220310"

# Convert hex string to bytes
data_bytes = bytes.fromhex(hex_data)

# Function to XOR the data with a key and return decoded output
def xor_decrypt(data, key):
    return bytes([b ^ key for b in data])

# Attempting to decrypt with all possible single-byte XOR keys
decoded_results = {}
for key in range(256):
    decoded = xor_decrypt(data_bytes, key)
    decoded_results[key] = decoded.decode('latin1', errors='replace')

# Displaying results for manual inspection
decoded_results