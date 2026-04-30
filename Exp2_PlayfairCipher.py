def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix_list = []

    # Add key letters
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix_list.append(ch)

    # Add remaining letters
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            matrix_list.append(ch)

    # Convert to 5x5 matrix
    matrix = [matrix_list[i:i+5] for i in range(0, 25, 5)]

    # Create position dictionary (for fast lookup)
    pos = {matrix[i][j]: (i, j) for i in range(5) for j in range(5)}

    return matrix, pos


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    result = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'

        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 != 0:
        result += 'X'

    return result


def encrypt_playfair(text, matrix, pos):
    text = prepare_text(text)
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = pos[a]
        r2, c2 = pos[b]

        if r1 == r2:  # Same row
            cipher += matrix[r1][(c1 + 1) % 5]
            cipher += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:  # Same column
            cipher += matrix[(r1 + 1) % 5][c1]
            cipher += matrix[(r2 + 1) % 5][c2]

        else:  # Rectangle
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


def decrypt_playfair(text, matrix, pos):
    text = "".join(ch for ch in text.upper() if ch.isalpha())
    plain = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        r1, c1 = pos[a]
        r2, c2 = pos[b]

        if r1 == r2:  # Same row
            plain += matrix[r1][(c1 - 1) % 5]
            plain += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:  # Same column
            plain += matrix[(r1 - 1) % 5][c1]
            plain += matrix[(r2 - 1) % 5][c2]

        else:  # Rectangle
            plain += matrix[r1][c2]
            plain += matrix[r2][c1]

    return plain


# ================= MAIN =================
key = input("Enter keyword: ")
plaintext = input("Enter plaintext: ")

matrix, pos = generate_key_matrix(key)

print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

cipher = encrypt_playfair(plaintext, matrix, pos)
print("\nEncrypted text:", cipher)

decrypted = decrypt_playfair(cipher, matrix, pos)
print("Decrypted text:", decrypted)