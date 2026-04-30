def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)

    shared_A = pow(B, a, p)
    shared_B = pow(A, b, p)

    if shared_A == shared_B:
        print("Shared key established successfully!")
    else:
        print("Error in key exchange!")

    return A, B, shared_A

# Main
p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))
a = int(input("Enter private key of A: "))
b = int(input("Enter private key of B: "))

A, B, shared = diffie_hellman(p, g, a, b)

print("Public key of A:", A)
print("Public key of B:", B)
print("Shared key:", shared)



# Sample Input:
# Enter prime number p: 23
# Enter primitive root g: 5
# Enter private key of A: 6
# Enter private key of B: 15
# Shared key established successfully!
# Public key of A: 8
# Public key of B: 19
# Shared key: 2