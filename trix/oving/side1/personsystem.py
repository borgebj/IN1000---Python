
class Person:
    def __init__(self, navn):
        self._navn = navn

    def hentNavn(self):
        return self._navn


class Personsystem:

    def __init__(self):
        self._liste = []

    def leggTilPerson(self, person):
        self._liste.append(person)

    def finnPerson(self, navn):
        for x in self._liste:
            if x.hentNavn() == navn:
                return x
        return None


def hovedprogram():
    personsystem = Personsystem()

    personsystem.leggTilPerson(Person("Borge"))
    personsystem.leggTilPerson(Person("Fryser"))
    personsystem.leggTilPerson(Person("Bill"))
    personsystem.leggTilPerson(Person("Bob"))
    personsystem.leggTilPerson(Person("Arne"))

    print("")
    assert personsystem.finnPerson("Bob") is not None
    print("")

hovedprogram()

