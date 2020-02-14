
#oppgave a)
a = 10
a = str(a)
b = "hei!"
c = a+b
print(c)
#er dette lovlig kode?
#Nei, dette er ikke lovlig kode for du kan ikke konkatenere str og int sammen, a ma bli gjort om til streng. (str(a))
#Det kommer feilmelding

#oppgave b)
x = "10"
y = "hei!"
print(x + y)
#er dette lovlig kode?
#Ja, dette er fordi bade x og y er streng, sa de kan konkateneres. Ingen feilmelding: programmet vil skrive ut: 10hei!

#oppgave c)
i = 10
i = str(i)
j = "12"
print(i + j)
#er dette lovlig kode?
#Nei, som i oppgave a) kan ikke int og streng konkateneres, i ma bli gjort om til streng forst. Feilmelding.