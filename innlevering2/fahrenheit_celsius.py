"""Dette programmet konverterer grader fra fahrenheit om til celsius, gjennom både egendefinert variabel og brukerinputt"""

#Definerer variabelen "fahrenheit" som 77
fahrenheit = 77

#printer ut variabelen ovenfor.
print("Temperaturen i fahrenheit er:",fahrenheit)

#Konverterer fahrenheit-gradene som ble definert over til celsius gjennom en formel.
celsius = float((fahrenheit-32)*5/9)

#printer ut celsius etter at fahrenheit ble konvertert gjennom formelen.
print("Temperaturen i celsius er:",celsius)

#Variabel som henter info fra brukeren, overskriver den tidligere variabelen med likt navn
fahrenheit = float(input("Skriv inn grader i fahrenheit: "))

#printer ut tekst sammen med variabelen som brukeren skrev inn
print("Temperaturen er",fahrenheit,"grader fahrenheit")

#variabel som regner ut fahrenheit om til celsius
celsius = float((fahrenheit-32)*5/9)

#printer ut tekst og gradene brukeren skrev inn som fahrenheit til celsius
print("Temperaturen er", celsius,"grader celsius")
