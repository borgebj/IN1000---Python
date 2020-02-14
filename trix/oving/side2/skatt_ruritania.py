
inntekt = float(input("\nHva er din inntekt?: "))

if inntekt < 10000:
    skatt = inntekt * 0.1
    print("Du skal betale",skatt,"i skatt\n")

elif inntekt >= 10000:
    skatt = (10000*0.1) + (inntekt-10000)*0.3
    print("Du skal betale",skatt,"kroner i skatt\n")