#Same thing as tapA except you can use dots along with numbers.
def tapcode():
    rows = []
    rows.append(['a','b','c','d','e'])
    rows.append(['f','g','h','i','j'])
    rows.append(['l','m','n','o','p'])
    rows.append(['q','r','s','t','u'])
    rows.append(['v','w','x','y','z'])
    
    endecrypt = input("Would you like to encrypt or decrypt?\n")
    while endecrypt != "encrypt" and endecrypt != "decrypt":
        endecrypt = input("Please enter encrypt or decrypt\n")

    
    dots = input("Would you like your encoded text to be in dots or numbers?")
    while dots != "dots" and dots != "numbers":
        dots = input("Please enter dots or numbers\n")

    endecodedtext = ''
    endecodedchar = ''
    if endecrypt == "encrypt":
        text = input("What would you like to encode\n")

        for char in text:
            if char.isupper():
                char = char.lower()
                
            if char == ' ':
                endecodedtext += "/"
                continue
            
            if char == 'k':
                char = 'c'
            
            for rownum, row in enumerate(rows):
                if char in row:
                    firsttap, secondtap = rownum, row.index(char)
                    
                    if dots == 'numbers':
                        endecodedchar = (str(firsttap + 1) + " " + str(secondtap + 1)) + ","
                    
                    if dots == 'dots':
                        endecodedchar = ((firsttap + 1) * '.') + " " + ((secondtap + 1) * '.') + ","
                    
            endecodedtext += endecodedchar


    if endecrypt == "decrypt":
        tapnumber = 1
        text = input("What would you like to decode\n")

        if dots == 'numbers':    
            for char in text:    
                if char not in ['1','2','3','4','5']:
                    if char == '/':
                        endecodedtext += ' '
                    continue
                    
                if tapnumber == 1:
                    firsttap = int(char) - 1
                    tapnumber += 1
                    continue
                
                if tapnumber == 2:
                    secondtap = int(char) - 1
                    endecodedchar = rows[firsttap][secondtap]
                    tapnumber -= 1
                    endecodedtext += endecodedchar
                    continue

        if dots == 'dots':
            dotnum = 0
            for char in text:
                if char == ' ':
                    firsttap = dotnum - 1
                    dotnum = 0
                
                if char == ',':
                    secondtap = dotnum - 1
                    dotnum = 0

                    endecodedchar = rows[firsttap][secondtap]
                    tapnumber -= 1
                    endecodedtext += endecodedchar
                    continue

                if char == '/':
                    endecodedtext += ' '
                    continue

                if char == '.':
                    dotnum += 1
                    continue
            
    print(endecodedtext)

if __name__ == "__main__":
    tapcode()