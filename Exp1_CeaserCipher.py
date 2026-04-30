def encrypt(text, key):
    key %= 26
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch
    return result


def decrypt(text, key):
    return encrypt(text, -key)


plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))

cipher = encrypt(plaintext, key)
print("Encrypted text:", cipher)

plain = decrypt(cipher, key)
print("Decrypted text:", plain)