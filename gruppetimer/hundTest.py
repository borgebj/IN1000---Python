from hund import Hund

jenteHund = Hund(1, "Laila", 15)
gutteHund = Hund(1, "Robert", 1)

#printer objektet med metode som returnerer verdi
print(jenteHund.hentHund())
print(gutteHund.hentHund())

print("")

#printer selve objektet
print(jenteHund)
print(gutteHund)

print("")

jenteHund = gutteHund
print(jenteHund == gutteHund)
print(jenteHund is gutteHund)