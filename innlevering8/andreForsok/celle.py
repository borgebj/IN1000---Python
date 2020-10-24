
#celle status:
#levende:
# < 2 levende naboer = død
# 2 eller 3 levende naboer = levende
# > 3 levende naboer = død
#død:
# 3 levende naboer = levende

class Celle:
    def __init__(self):
        self._status = "dod"

    def settDoed(self):
        self._status = "dod"

    def settLevende(self):
        self._status = "levende"

    def erLevende(self):
        if self._status == "levende":
            return True
        return False

    def hentStatusTegn(self):
        if self._status == "levende":
            return "O"
        return "."