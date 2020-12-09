
def gjenta(a):
    a = a + a
    return a


a = "ab"
b = gjenta(a)
print(a+b)

# a + a = "ab" + "ab" = "abab"
# b = "abab"
# a + b = "ab" + "abab" = "ababab"

def voks(alder):
    alder = alder+1


alder_1 = 20
voks(alder_1)
print(alder_1)

#lurespørsmål: ingenting returneres, 20 blir skrevet ut