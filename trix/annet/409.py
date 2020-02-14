#coding=utf-8
import random
#oppg 4.09 fra Trix - Skattejakt m/ rutenett

def hovedprogram():
    #tom nøsted liste
    skattekart = []
    stoerrelse = 5

    for e in range(stoerrelse):
        a = []

        for e in range(stoerrelse):
            a.append("O")

        skattekart.append(a)




    #x er hver liste i skattekart > printer ut hver liste på hver sin linje
    for x in skattekart:
        string = ""
        for y in x:
            string += y
        print(string)

hovedprogram()

