from math import gcd

# ---------- Modular Inverse ----------
def mod_inverse(a, m):
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists.")

# ---------- Determinant ----------
def determinant(matrix):
    n = len(matrix)

    if n == 2:
        return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]) % 26

    elif n == 3:
        a,b,c = matrix[0]
        d,e,f = matrix[1]
        g,h,i = matrix[2]
        det = (a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g))
        return det % 26

    else:
        raise ValueError("Only 2x2 or 3x3 matrices supported.")

# ---------- Matrix Inverse ----------
def matrix_inverse(matrix):
    n = len(matrix)
    det = determinant(matrix)

    if gcd(det, 26) != 1:
        raise ValueError("Key matrix not invertible mod 26.")

    det_inv = mod_inverse(det, 26)

    if n == 2:
        a, b = matrix[0]
        c, d = matrix[1]
        return [
            [( d * det_inv) % 26, (-b * det_inv) % 26],
            [(-c * det_inv) % 26, ( a * det_inv) % 26]
        ]

    elif n == 3:
        # Cofactor matrix
        def minor(m, i, j):
            return [
                [m[x][y] for y in range(3) if y != j]
                for x in range(3) if x != i
            ]

        cof = []
        for i in range(3):
            row = []
            for j in range(3):
                sub = minor(matrix, i, j)
                val = determinant(sub)
                if (i + j) % 2 != 0:
                    val = -val
                row.append(val % 26)
            cof.append(row)

        # Transpose (adjoint)
        adj = [[cof[j][i] for j in range(3)] for i in range(3)]

        # Multiply by det inverse
        return [[(adj[i][j] * det_inv) % 26 for j in range(3)] for i in range(3)]

# ---------- Text Processing ----------
def process_text(text, size):
    text = "".join(ch for ch in text.upper() if ch.isalpha())
    while len(text) % size != 0:
        text += 'X'
    return text

def text_to_numbers(text):
    return [ord(c) - 65 for c in text]

def numbers_to_text(nums):
    return "".join(chr(n % 26 + 65) for n in nums)

# ---------- Multiply Matrix × Vector ----------
def multiply(matrix, vector):
    result = []
    for row in matrix:
        val = sum(row[i] * vector[i] for i in range(len(vector))) % 26
        result.append(val)
    return result

# ---------- Encrypt ----------
def encrypt_hill(text, key):
    n = len(key)
    text = process_text(text, n)
    nums = text_to_numbers(text)

    result = []
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        result.extend(multiply(key, block))

    return numbers_to_text(result)

# ---------- Decrypt ----------
def decrypt_hill(cipher, key):
    inv_key = matrix_inverse(key)
    nums = text_to_numbers(cipher)

    n = len(key)
    result = []
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        result.extend(multiply(inv_key, block))

    return numbers_to_text(result)


# ================= MAIN =================

# 🔹 Choose key size (2 or 3)

# Example 2x2 key
key = [[3, 3],
       [2, 5]]

# Example 3x3 key
# key = [
#     [6, 24, 1],
#     [13,16,10],
#     [20,17,15]
# ]

plaintext = input("Enter plaintext: ")

cipher = encrypt_hill(plaintext, key)
print("Encrypted text:", cipher)

plain = decrypt_hill(cipher, key)
print("Decrypted text:", plain)