def vigenere(text, key, mode="encrypt"):
    text = text.upper()
    key = key.upper()
    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            t = ord(ch) - ord('A')
            k = ord(key[j % len(key)]) - ord('A')

            if mode == "encrypt":
                val = (t + k) % 26
            else:
                val = (t - k) % 26

            result += chr(val + ord('A'))
            j += 1
        else:
            result += ch

    return result


# ================= MAIN =================
plaintext = input("Enter plaintext: ")
keyword = input("Enter keyword: ")

cipher = vigenere(plaintext, keyword, "encrypt")
print("Encrypted text:", cipher)

decrypted = vigenere(cipher, keyword, "decrypt")
print("Decrypted text:", decrypted)






# Enter plaintext: HELLO WORLD
# Enter keyword: KEY

# Encrypted text: RIJVS UYVJN
# Decrypted text: HELLO WORLD