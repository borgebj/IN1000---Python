def pros1(a):
    print(a*2)

def pros2(b):
    print(b)
    pros1(b+2)

pros1(5)
pros2(4)
