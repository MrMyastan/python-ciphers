def rot():
    text = input("What would you like to encrypt/decrypt?\n")

    endecrypt = input("Would you like to encrypt or decrypt?\n")
    while endecrypt != "encrypt" and endecrypt != "decrypt":
        print("Please enter encrypt or decrypt\n")
        endecrypt = input()
    
    print("How many rotations?")
    while True:
        try:
            rotations = int(input()) % 26
            break
        except ValueError:
            print("Please enter a number\n")

    result = ''
    for char in text:
        upper = False
        if char.isupper():
                upper = True
                char = char.lower()

        if not 'a' <= char <= 'z':
            result += char
            continue

        char_ASCII = ord(char)

        if endecrypt == "encrypt":
            char_ASCII += rotations
        else:
            char_ASCII -= rotations

        if ord('z') < char_ASCII:
            char_ASCII -= 26

        if char_ASCII < ord('a'):
            char_ASCII += 26
        
        encodedchar = chr(char_ASCII)

        if upper:
            encodedchar = encodedchar.upper()

        result += encodedchar

    print(result)

if __name__ == "__main__":
    rot()