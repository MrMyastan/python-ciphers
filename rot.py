# this is perhaps the worst way to implement rot, but it works
# I mean like seriously, this is a like a few small steps removed from using vim commands or google sheets fill down to create fizzbuzz

numberMappings = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
letterMappings = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: 'a', 28: 'b', 29: 'c', 30: 'd', 31: 'e', 32: 'f', 33: 'g', 34: 'h', 35: 'i', 36: 'j', 37: 'k', 38: 'l', 39: 'm', 40: 'n', 41: 'o', 42: 'p', 43: 'q', 44: 'r', 45: 's', 46: 't', 47: 'u', 48: 'v', 49: 'w', 50: 'x', 51: 'y', 52: 'z'}

def encode():    
    print("How many rotations?")
    while True:
        try:
            rotations = int(input())
            if 0 <= rotations <= 26:
                break
        except ValueError:
            print("thats not a number 0-26")
    toEncode = input("What would you like to encode?\n")
    encoded = ''
    encodeChar = ''
    for char in toEncode:
        upper = False
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if char.isupper():
                upper = True
                char = char.lower()
            encodeChar = letterMappings.get(numberMappings.get(char) + rotations)
            if upper:
                encodeChar = encodeChar.upper()
            encoded = encoded + encodeChar
        else:
            encoded = encoded + char
    print(encoded) 