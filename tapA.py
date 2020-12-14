#Have to admit, while the list of lists was my idea, I didn't know how to do it in a way that worked so I had a little help with rows.append
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
                    endecodedchar = (str(firsttap + 1) + " " + str(secondtap + 1)) + ","
                    
            endecodedtext += endecodedchar


    if endecrypt == "decrypt":
        tapnumber = 1
        text = input("What would you like to decode\n")
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
            
    print(endecodedtext)

if __name__ == "__main__":
    tapcode()