from rand_prime import generate_prime
from math import gcd

def init():
    print(keygen(int(input())))

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



if __name__ == "__main__":
    init()