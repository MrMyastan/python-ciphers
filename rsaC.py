from rand_prime import generate_prime
from math import gcd, ceil

def manager():
    while True:
        choice = input("Enter keygen to generate keys or transform to encrypt/decrypt: ")
        if choice == "keygen" or choice == "transform":
            break
    if choice == "keygen":
        while True:
            try:
                bits = int(input("How many bits long do you want your key to be? "))
                break
            except ValueError:
                print("Please enter a number\n")
        while True:
            try:
                e = int(input("What do you want your public exponent to be? (recommended is 65537) "))
                break
            except ValueError:
                print("Please enter a number\n")
        result = keygen(bits, e)
        print(f"RSA Modulus, n: {result[0][1]}\nPublic Exponent, e: {result[0][0]}\nPrivate Exponent (keep this secret!), d: {result[1][0]}")

def keygen(bit_length: int, e: int=65537, ) -> tuple:
    bits_per = bit_length // 2
    
    p = generate_prime(bits_per)
    
    if bits_per % 2 == 1:
        bits_per += 1
    q = generate_prime(bits_per)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    if gcd(e, phi) != 1 or e % 2 != 1:
        print("invalid e")
        return ()

    d = pow(e, -1, phi)

    return ((e, n), (d, n))

def i2osp(x: int) -> bytes:
    octets = []
    for i in range(ceil(x / 256)):
        octets.insert(0, x & 255)
        x >>= 8
    return bytes(octets)

def os2ip(X: bytes) -> int:
    XLen = len(X)
    x = 0
    for i in range(XLen):
        x += X[i] * (256 ** (XLen - i - 1))
    return x

def get_int_input(prompt: str) -> int:
    while True:
        try:
            response = int(input(prompt))
            break
        except ValueError:
            print("Please enter a number\n")
    return response

if __name__ == "__main__":
    manager()