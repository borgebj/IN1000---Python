
def brillesjekk(styrke):
    ny_styrke = [2.5, 2.7]
    styrke = ny_styrke

pers_styrke = [1.5, 1.5]
brillesjekk(pers_styrke)
print(pers_styrke[0])
# Printer 1.5, fordi pers_styrke (SELVE LISTEN) endrer seg ikke i prosedyren.


def brillesjekk2(styrke):
    styrke[0] = 1.75

pers_styrke = [1.5, 1.5]
brillesjekk2(pers_styrke)
print(pers_styrke[0])
# Printer 1.75, fordi prosedyren endret indeks 0 til 1.75. 


tall = 5.241235

print(round(tall, 5))