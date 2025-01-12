import numpy as np


def hill_cipher_encrypt(text, key):
    # Chuyển đổi ký tự thành số
    def char_to_num(c):
        return ord(c) - ord('A')

    # Chuyển đổi số thành ký tự
    def num_to_char(n):
        return chr(n + ord('A'))

    # Chia văn bản thành các khối
    def split_blocks(text, block_size):
        return [text[i:i + block_size] for i in range(0, len(text), block_size)]

    # Pad thêm ký tự 'X' nếu độ dài văn bản không chia hết cho block_size
    while len(text) % 3 != 0:
        text += 'X'

    # Chuyển đổi văn bản thành mảng số
    blocks = split_blocks(text, 3)
    num_blocks = [[char_to_num(c) for c in block] for block in blocks]

    # Chuyển mảng số thành numpy array
    num_blocks = np.array(num_blocks).T

    # Nhân ma trận khóa với từng khối
    encrypted_blocks = np.dot(key, num_blocks) % 26

    # Chuyển kết quả thành chuỗi ký tự
    encrypted_text = ''.join([num_to_char(num) for num in encrypted_blocks.T.flatten()])

    return encrypted_text



# Ví dụ khóa ma trận K
key = np.array([[6, 24, 1],
                [13, 16, 10],
                [20, 17, 15]])

# Văn bản cần mã hóa
text = "VIETAA"

# Mã hóa văn bản
encrypted_text = hill_cipher_encrypt(text, key)
print("Văn bản mã hóa:", encrypted_text)
