from dato import Dato

d1 = Dato(15, 10, 2020)

aar = d1.lesAar()
print(aar)

if d1.sjekkDag(15):
    print("Loenningsdag!")
elif d1.sjekkDag(1):
    print("Ny maaned, nye muligheter")

print(d1)