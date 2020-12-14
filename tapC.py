def tapcode():
    text = input("What would you like to en/decode?\n")
    endecode = input("Would you like to encode or decode?\n")
    while endecode != "encode" and endecode != "decode":
        print("Please enter encode or decode\n")
        endecrypt = input()
    if endecode == "encode":
        encode(text)
    else:
        decode(text)

def encode(text: str):
    text = text.upper().replace('K', 'C')
    result = ''
    for char in text:
        if char == " ":
            result += '/'
            continue
        if not 'A' <= char <= 'Z':
            continue
        if char <= 'E':
            result += '1'
            base = 64
        elif char <= 'J':
            result += '2'
            base = 69
        elif char <= 'P':
            result += '3'
            base = 75
        elif char <= 'U':
            result += '4'
            base = 80
        elif char <= 'Z':
            result += '5'
            base = 85
        result += ' ' + str(ord(char) - base) + ','
    print(result)

def decode(text: str):
    words_temp = text.split("/")
    words = list()
    result = ''
    for word in words_temp:
        words.append(word.split(","))
    for word in words:
        word.pop()
        for char in word:
            try:
                if not 0 < int(char[0]) < 6 and not 0 < int(char[2]):
                    continue
            except ValueError:
                continue
            base = 60
            if int(char[0]) <= 2:
                base = 59
            result_ord = base + (5 * int(char[0])) + int(char[2])
            result += chr(result_ord)
        result += " "
    print(result)
            
if __name__ == "__main__":
    tapcode()