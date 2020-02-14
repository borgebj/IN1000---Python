
def velkommen(bruker):
    print("Velkommen", str(bruker) + "!")

inp = input("Skriv inn navn: ")
velkommen(inp)

def strenginator(streng1, streng2):
    konkatenert = streng1+" "+streng2
    return konkatenert

strengA = "Hei"
strengB = "verden!"
konkatenert = strenginator(strengA, strengB)
print(konkatenert)