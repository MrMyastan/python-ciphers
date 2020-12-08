print("What cipher would you like to use?")
cipher = input()

if cipher == "rot":
    print("How many rotations?")
    while True:
        try:
            rotations = int(input())
            if 0 <= rotations <= 26:
                break
        except ValueError:
            print("thats not a number buddy")