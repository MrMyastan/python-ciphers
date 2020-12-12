import rot_but_bad
import rotA
import rotC

cipherDispatch = {"rot": rot_but_bad.encode, "rotA": rotA.rot, "rotC": rotC.rot}

print("What cipher would you like to use?")
cipher = input()

if cipher in cipherDispatch:
    cipherDispatch[cipher]()
else:
    print("we dont have that one")