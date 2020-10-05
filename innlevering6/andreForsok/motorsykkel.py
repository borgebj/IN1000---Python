
# 1.1
class Motorsykkel:
    def __init__(self, merke, regNr, kmStand):
        self._merke = merke
        self._regNr = regNr
        self._kmStand = kmStand

    # 1.2
    def kjor(self, km):
        self._kmStand += km

    # 1.3
    def hentKilometerstand(self):
        return self._kmStand

    # 1.4
    def skrivUt(self):
        print(self._merke)
        print(self._regNr)
        print(self._kmStand)