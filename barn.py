from gave import Gave

class Barn:

    def __init__(self, navn):
        self._navn = navn
        self._gaver = []
        self._totalPris = 0

    def barnNavn(self):
        return self._navn

    def totalPris(self):
        return self._totalPris

    def apneGave(self, gave):
        x = gave.gavePris()
        self._gaver.append(x)
        self._totalPris += int(x)

    def skrivBarn(self):
        print(self._navn)
        for x in self._gaver:
            print(x)
        print(self._totalPris)
