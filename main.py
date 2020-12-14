import rot_but_bad
import rotA
import rotC
import tapC
import tapA
import tapA1

cipherDispatch = {"rot": rot_but_bad.encode, "rotA": rotA.rot, "rotC": rotC.rot, "tapC": tapC.tapcode, "tapA": tapA.tapcode, "tapA1": tapA1.tapcode}

print("What cipher would you like to use?")
cipher = input()

if cipher in cipherDispatch:
    cipherDispatch[cipher]()
else:
    print("we dont have that one")