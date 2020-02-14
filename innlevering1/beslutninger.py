"""Dette programmet spør brukeren om de kunne tenke seg en brus, og ved hjelp av input fra brukeren og if-setninger sjekker programmet hva brukeren svarte og skriver ut tekst i forhold til hva som var svart."""

#Input spør om brukeren kunne tenkt seg en brus, hvor jeg tok inn ja/nei i teksten for å gi bedskjed om at dette er et ja/nei spørsmål.
brus = input("Kunne du tenkt deg en brus? (ja/nei): ")

#Dette ser hva brukeren har skrevet inn, og sjekker om dette passer med "if" eller "elif".
if brus == "ja":
    print("Her har du en brus!")
elif brus == "nei":
    print("Den er grei")
#Hvis det ikke passer går den inn i "else" og det printes ut "Det forstod jeg ikke helt".
else:
    print("Det forstod jeg ikke helt.")
