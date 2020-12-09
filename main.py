import rot

cipherDispatch = {"rot": rot.cipher}

print("What cipher would you like to use?")
cipher = input()

if cipher in cipherDispatch:
    cipherDispatch[cipher]()
else:
    print("we dont have that one")