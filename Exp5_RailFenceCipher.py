def rail_fence(text, key, mode="encrypt"):
    if key <= 1:
        return text

    if mode == "encrypt":
        rails = ['' for _ in range(key)]
        row, direction = 0, 1

        for ch in text:
            rails[row] += ch
            row += direction
            if row == 0 or row == key - 1:
                direction *= -1

        return ''.join(rails)

    else:
        # Create pattern
        pattern = [['\n' for _ in range(len(text))] for _ in range(key)]
        row, direction = 0, 1

        for col in range(len(text)):
            pattern[row][col] = '*'
            row += direction
            if row == 0 or row == key - 1:
                direction *= -1

        # Fill pattern
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if pattern[i][j] == '*' and index < len(text):
                    pattern[i][j] = text[index]
                    index += 1

        # Read zigzag
        result = []
        row, direction = 0, 1
        for col in range(len(text)):
            result.append(pattern[row][col])
            row += direction
            if row == 0 or row == key - 1:
                direction *= -1

        return ''.join(result)


# ================= MAIN =================
plaintext = input("Enter plaintext: ")
depth = int(input("Enter depth: "))

cipher = rail_fence(plaintext, depth, "encrypt")
print("Encrypted text:", cipher)

decrypted = rail_fence(cipher, depth, "decrypt")
print("Decrypted text:", decrypted)