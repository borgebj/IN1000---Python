
def finnAlleFibTall(tall):

    list = []
    tall1 = 0
    tall2 = 1

    list.append(tall1)

    while tall2 <= tall:
        list.append(tall2)
        fibbo = tall1 + tall2
        tall1 = tall2
        tall2 = fibbo
    return list

def laBrukerSkirveInntall():
    inp = input("Skriv inn tall: ")
    tall = int(inp)
    return tall


tall = laBrukerSkirveInntall()
print(finnAlleFibTall(tall))