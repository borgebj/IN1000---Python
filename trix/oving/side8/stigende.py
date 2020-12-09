

def sjekkSortert(liste):
    if len(liste) == 0: return False
    else:
        forrige = liste[0]
        for x in liste:
            if x < forrige:
                return False
            forrige = x
        return True


en = [1, 2, 3, 5, 6, 9]
to = [1, 3, 5, 2, 6, 7]

Ten = sjekkSortert(en)
Tto = sjekkSortert(to)

print("True:", Ten)
print("False:", Tto)