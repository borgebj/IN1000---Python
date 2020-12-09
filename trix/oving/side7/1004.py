
class Node:
    def __init__(self, tall):
        self._innhold = tall
        self._nesteNode = None


class Lenkeliste:
    def __init__(self):
        self._forsteNode = None

    def leggTilNode(self, node):
        if (self._forsteNode == None):
            self._forsteNode = node
        else:
            currNode = self._forsteNode
            while (currNode._nesteNode != None):
                currNode = currNode._nesteNode
            currNode._nesteNode = node

    def printLenkeliste(self):
        currNode = self._forsteNode
        while (currNode != None):
            print(currNode._innhold)
            currNode = currNode._nesteNode


def Hovedprogram():
    ll = Lenkeliste()

    ll.leggTilNode(Node(1))
    ll.leggTilNode(Node(5))
    ll.leggTilNode(Node(9))

    ll.printLenkeliste()

Hovedprogram()
