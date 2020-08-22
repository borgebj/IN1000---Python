from studentSystem import Studentsystem

def hovedprogam():
    print("---------------------------------------------------------------------------\n")

    test = Studentsystem()
    test.hentFil("emnestudenter.txt")
    test.printUt()
    print("\n---------------------------------------------------------------------------")


hovedprogam()

