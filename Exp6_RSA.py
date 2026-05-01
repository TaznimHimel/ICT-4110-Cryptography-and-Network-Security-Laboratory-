from math import gcd

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("Inverse doesn't exist")
    return x % phi


def rsa_keygen(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime with phi(n)")

    d = mod_inverse(e, phi)
    return (e, n), (d, n)


def rsa_encrypt_text(text, public_key):
    e, n = public_key
    return [pow(ord(ch), e, n) for ch in text]


def rsa_decrypt_text(cipher, private_key):
    d, n = private_key
    return ''.join(chr(pow(c, d, n)) for c in cipher)


def rsa_encrypt_number(number, public_key):
    e, n = public_key
    if number >= n:
        raise ValueError("Number must be less than n")
    return pow(number, e, n)


def rsa_decrypt_number(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)


# Main
p, q, e = 17, 11, 7
public_key, private_key = rsa_keygen(p, q, e)

print("Public Key:", public_key)
print("Private Key:", private_key)

choice = input("Choose input type (text/number): ").lower()

if choice == "text":
    plaintext = input("Enter plaintext: ")
    cipher = rsa_encrypt_text(plaintext, public_key)
    print("Encrypted:", cipher)

    decrypted = rsa_decrypt_text(cipher, private_key)
    print("Decrypted:", decrypted)

elif choice == "number":
    number = int(input("Enter a number: "))
    cipher = rsa_encrypt_number(number, public_key)
    print("Encrypted:", cipher)

    decrypted = rsa_decrypt_number(cipher, private_key)
    print("Decrypted:", decrypted)

else:
    print("Invalid choice! Please select 'text' or 'number'.")