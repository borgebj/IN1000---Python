"""Dette programmet skriver ut tekst i terminalen ved hjelp av kommandoen "print", og tar vare på ulike verdier i variabler som settes sammen med "print" for å skrive ut både tekst og verdien gitt til variablene."""

#Et program som skriver ut teksten: "Hei Student!"
print("Hei Student!")

#Input spør om et navn, og deretter printer ut "Hei" sammen med navnet brukeren tastet inn.
navn = input("Hva er navnet ditt? ")
print("Hei",navn)

#Begge tallene får definert sin egen variabel, og deretter skrives disse variabelene ut på hver sin linje.
a = 4
b = 6
print(a)
print(b)


#Gjennom den nye variabelene "sum" blir de to tidligere variablene lagt sammen til et nytt tall. Nå printes ut både teksten og den nye variabelen.
#Teksten og variabelen blir skilt med anførselstegn og komma.
sum = a-b
print("Differanse:", sum)

#Nytt navn blir spurt av brukeren, som da legges nå inn i variablene "navn2". Deretter kombineres variabelene "navn" og "navn2" til én variabel, altså variabelen "sammen".
#Print skriver ut kombinasjonen av begge navnene.
navn2 = input("Hva er ditt navn? ")
sammen = navn+navn2
print(sammen)

#Her endres variabelen "sammen" slik at den får teksten "og" mellom de to variablene jeg kombinerer.
#Jeg skiller variabelene og teksten ved å sette inn anførselstegn mellom pluss-tegnene og mellomrom før og etter ordet "og".
sammen = navn+" og "+navn2
print(sammen)
