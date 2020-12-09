
#oppgaven
def sjekkListeTall(liste):
    tall = liste[0]
    for x in range(len(liste)):
        if liste[x] != tall:
            return -1
    return tall

#tester
LEn = [1, 1, 1, 1, 1, 2, 1, 1, 1]
LTo = [5, 5, 5, 5, 5, 5, 5, 5, 5]

tallEn = sjekkListeTall(LEn)
tallTo = sjekkListeTall(LTo)

print("-1:", tallEn)
print("5:", tallTo)

