from hund import Hund

def hovedprogram():
    hund = Hund(10, 30)

    print("vekt:", hund.hentVekt())

    # spiser og loeper
    hund.spring()
    hund.spis(5)
    hund.spring()
    hund.spis(2)

    print("vekt:", hund.hentVekt())

hovedprogram()