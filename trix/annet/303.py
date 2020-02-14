
maaneder = ["januar", "februar", "mars", "april", "mai", "juni", "juni", "august", "september", "oktober", "november", "desember"]

def maaned():
    nr = int(input("oppgi maanedsnummer: "))
    
    if nr > 0 and nr < 13:
        print(nr,"-", maaneder[nr-1],"\n")
    else:
        print("Ugyldig maanedsnr\n")

maaned()
maaned()
maaned()
