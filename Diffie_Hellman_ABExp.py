def diffie_hellman(p, g, a, b):
    # Alice computes A = g^a mod p
    A = pow(g, a, p)
    
    # Bob computes B = g^b mod p
    B = pow(g, b, p)

    # Alice computes the shared secret s = B^a mod p
    s_alice = pow(B, a, p)
    
    # Bob computes the shared secret s = A^b mod p
    s_bob = pow(A, b, p)
    
    return s_alice, s_bob

# Example usage
p = 7  # prime modulus
g = 5   # generator
a = 3   # Alice's private key
b = 4  # Bob's private key

s_alice, s_bob = diffie_hellman(p, g, a, b)
print(f"Alice's shared secret: {s_alice}")
print(f"Bob's shared secret: {s_bob}")