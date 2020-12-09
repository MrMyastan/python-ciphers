def cipher():    
    print("How many rotations?")
    while True:
        try:
            rotations = int(input())
            if 0 <= rotations <= 26:
                break
        except ValueError:
            print("thats not a number buddy")