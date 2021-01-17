# credit to https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb for most of this (i modified it a little)
from secrets import randbits, randbelow

def is_prime(n: int, k: int=128) -> bool:
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randbelow(n - 3) + 2
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_candidate(length: int) -> int:
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = randbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p

def generate_prime(length: int=1024, k: int=128) -> int:
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in bits
            k -- int -- num of primality test loops
        return a prime
    """
    p = generate_prime_candidate(length)
    # keep generating while the primality test fail
    while not is_prime(p, k):
        p = generate_prime_candidate(length)
    return p