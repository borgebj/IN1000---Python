# coding=utf-8

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()

# Beskrivelse av programflyt:

# 1. Først defineres funksjonen "minFunksjon()" som ikke skal ta imot eller inneholder noen parametre.
# 2. Prosedyren* "hovedprogram()" blir dermed definert og, som forrige, ikke inneholder eller tar imot noen parametre.
# 3. Prosedyren* "hovedprogram()" blir kalt opp.

# 4. variabelen "a" blir gitt verdien 42.
# 5. variabelen "b" blir gitt verdien 0.
# 6. programmet printer ut variabel "b" til terminalen, som printer da ut tallet 0.
# 7. variabelen "b" får en ny verdi. "b" blir nå variabelen "a"
# 8. variabelen "a" blir gitt en ny verdi, og blir nå "minFunksjon()" - a'en i b = a vil ikke bli endret av dette, fordi dette ble definert etter at "b" ble lik variabelen "a"
# 9. programmet printer ut variabel "b", som nå har blitt det samme som variabel "a" - altså: funksjonen "minFunksjon()" blir kalt opp, fordi a = minFunksjon(), og b = a.
# variabelen a kaller altså opp "minFunksjon", og blir altså gitt verdien funksjonen returnerer.

# 10. En for-løkke blir laget som gjør koden under på hvert tall i range 2 (0 - 1), fordi den starter fra 0.
# 11. variabelen "c" blir gitt verdien 2.
# 12. programmet printer ut variabel "c" til terminalen, som printer da ut tallet 2
# 13. variabelen "c" legger dermed til 1. c += 1 > c = c + 1. Fordi variabelen "c" er 2, blir "c" nå 3.
# 14. variabelen "b" blir gitt verdien 10. (siden disse er lokale variabler påvirkes ikke funksjonene hverandre med variabler)
# 15. variabelen "b" legger dermed lik variabelen "a" - men siden "a" ikke er definert inne i denne funksjonen, kommer feilmelding.
# 16. programmet printer så ut variabel "b"

# 17. for-løkken kjøres på nytt, og variabelen "c" blir gitt verdien 2 på nytt.
# 18. programmet printer ut variabelen "c" som har blitt gitt verdien 2. Altså tallet 2 printes ut.
# 19. variabelen "b" blir gitt verdien 10 på nytt.
# 20. variabelen "b" legger til variabelen "a" på nytt (som ikke er definert)
# 21. programmet printer dermed ut variabel "b"

# 22. funksjonen returnerer variabelen "b" - dette vil nå si at <minFunksjon = b (verdien b er gitt)>
# 23. programmet printer ut variabel "b", som tidligere ble lik variabelen a, som da var tallet 42. Tallet 42 printes dermed ut på terminalen.
# 24. programmet printer ut variabel "a" som har blitt gitt verdien som "minFunksjon" returnerer, altså variabel b "fra minFunksjon"


#feilen med koden var at variabelen "a" i minFunksjon() manglet, fordi variabelen "a" i funksjonen hovedprogram() er en lokal variabel til DEN funksjonen, og kan altså ikke bli brukt i andre funksjoner.