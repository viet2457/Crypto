def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(Mi, mi):

    gcd, inverse, _ = extended_gcd(Mi, mi)
    if gcd != 1:
        raise ValueError(f"{Mi} và {mi} không nguyên tố cùng nhau")
    return inverse % mi


def crt(a, m):

    M = 1
    for mi in m:
        M *= mi

    x = 0
    for ai, mi in zip(a, m):
        Mi = M // mi
        Ni = mod_inverse(Mi, mi)
        x += ai * Mi * Ni

    return x % M


a = [2, 5, 2]  # Các phần dư
m = [3, 5, 7]  # Các modulo

# Tính giá trị x
x = crt(a, m)
print(f"Giá trị x thỏa mãn hệ đồng dư là: x ≡ {x} mod {m[0] * m[1] * m[2]}")
