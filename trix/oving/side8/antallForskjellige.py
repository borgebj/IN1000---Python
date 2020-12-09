

def sjekkForskjellige(streng):
    brukt = []
    antall = 0
    for x in streng:
        if x not in brukt:
            antall += 1
            brukt.append(x)
    return antall

en = "aabbccdd"
to = "accag"

Ten = sjekkForskjellige(en)
Tto = sjekkForskjellige(to)

print("4:",Ten)
print("3:", Tto)


