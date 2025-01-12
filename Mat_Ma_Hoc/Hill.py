import numpy as np

def hill_cipher_encrypt(name, key):
    # Bảng mã hóa ký tự
    char_to_num = {chr(i + 65): i + 1 for i in range(26)}  # A=1, B=2, ..., Z=26
    char_to_num['NULL'] = 27  # NULL=27
    num_to_char = {v: k for k, v in char_to_num.items()}

    # Chọn 3 ký tự đầu tiên và thêm NULL nếu cần
    name = name[:3]
    if len(name) < 3:
        name += 'NULL'  # Thêm NULL nếu tên ít hơn 3 ký tự

    # Chuyển đổi ký tự thành số
    vector = [char_to_num[char] for char in name]

    # Chia vector thành các khối (2 ký tự mỗi khối)
    blocks = [vector[i:i + 2] for i in range(0, len(vector), 2)]

    # Khóa Hill (ma trận)
    K = np.array([[6, 24], [1, 13]])

    encrypted_vectors = []

    for block in blocks:
        # Thêm NULL nếu khối không đủ 2 ký tự
        if len(block) < 2:
            block.append(27)  # NULL

        # Chuyển đổi thành ma trận
        block_matrix = np.array(block).reshape(-1, 1)

        # Mã hóa
        encrypted_block = K @ block_matrix
        encrypted_block = encrypted_block % 27  # Áp dụng modulo 27
        encrypted_vectors.append(encrypted_block.flatten().tolist())

    # Kết quả mã hóa
    encrypted_values = [num for sublist in encrypted_vectors for num in sublist]
    return encrypted_values

# Tên sinh viên
name = "VIET"
result = hill_cipher_encrypt(name, key=None)
print("Kết quả mã hóa:", result)