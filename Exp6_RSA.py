from math import gcd

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

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


def rsa_encrypt(text, public_key):
    e, n = public_key
    return [pow(ord(ch), e, n) for ch in text]


def rsa_decrypt(cipher, private_key):
    d, n = private_key
    return ''.join(chr(pow(c, d, n)) for c in cipher)


# Main
p, q, e = 61, 53, 17

public_key, private_key = rsa_keygen(p, q, e)

print("Public Key:", public_key)
print("Private Key:", private_key)

plaintext = input("Enter plaintext: ")
cipher = rsa_encrypt(plaintext, public_key)
print("Encrypted:", cipher)

decrypted = rsa_decrypt(cipher, private_key)
print("Decrypted:", decrypted)