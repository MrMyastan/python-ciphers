from rand_prime import generate_prime
from math import gcd, ceil

def manager():
    while True:
        choice = input("Enter keygen to generate keys or transform to encrypt/decrypt: ")
        if choice == "keygen" or choice == "transform":
            break
    if choice == "keygen":
        bits = get_int_input("How many bits long do you want your key to be? ")
        e = get_int_input("What do you want your public exponent to be? (recommended is 65537) ")
        result = keygen(bits, e)
        print(f"RSA Modulus, n: {result[0][1]}\nPublic Exponent, e: {result[0][0]}\nPrivate Exponent (keep this secret!), d: {result[1][0]}")
    elif choice == "transform":
        n = get_int_input("Enter your RSA modulus, n: ")
        
        while True:
            en_or_de = input("Would you like to encrypt or decrypt?: ")
            if en_or_de == "encrypt" or en_or_de == "decrypt":
                break
        
        # just here to suppress pylance possibly unbound warnings
        exp = 65537
        data = -1
        
        if en_or_de == "encrypt":
            exp = get_int_input("Enter the exponent to use (usually the e of the public key, which is usually 65537):")
            data = os2ip(input("Enter your message (will be converted to an int according to PKCS #1 Section 4.2): ").encode())
        elif en_or_de == "decrypt":
            exp = get_int_input("Enter the exponent to use (usually the d of the private key):")
            data = get_int_input("Enter the int of the encrypted data: ")
        
        transformed = transform(exp, n, data)
        
        if en_or_de == "decrypt":
            transformed = i2osp(transformed).decode()

        print(f"Your transformed data is: {transformed}")

def keygen(bit_length: int, e: int=65537, ) -> tuple:
    bits_per = bit_length // 2
    
    p = generate_prime(bits_per)
    
    if bits_per % 2 == 1:
        bits_per += 1
    q = generate_prime(bits_per)
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    if gcd(e, phi) != 1 or e % 2 != 1:
        raise ValueError("Invalid e")

    d = pow(e, -1, phi)

    return ((e, n), (d, n))

def transform(exp: int, n: int, data: int) -> int:
    if not 0 <= data < n:
        raise ValueError("Message is not less than n and greater than or equal to 0")
    return pow(data, exp, n)

def i2osp(x: int) -> bytes:
    octets = []
    while x:
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