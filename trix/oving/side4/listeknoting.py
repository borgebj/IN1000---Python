
def vanligKonkat(liste1, liste2):
    list = liste1 + liste2
    return list

def annenHverKonkat(liste1, liste2):
    liste = []
    teller = 0
    for x in liste1:
        liste.append(x)
        liste.append(liste2[teller])
        teller += 1
    print(liste)



annenHverKonkat([1,2,3],["a","b","c"])

