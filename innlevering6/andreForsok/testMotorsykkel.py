from motorsykkel import Motorsykkel

def hovedprogram():
    m1 = Motorsykkel("Børg", "555666", 5)
    m2 = Motorsykkel("børg2", "55621", 5)
    m3 = Motorsykkel("børg3", "62352", 1)

    m1.skrivUt()
    m2.skrivUt()
    m3.skrivUt()

    m3.kjor(10)
    m3.skrivUt()

hovedprogram()