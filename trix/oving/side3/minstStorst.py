
list = [6, -4, 7, -2, 8, -3, 9, -11]

minst = list[0]
for x in list:
    if x < minst:
        minst = x
print("Den minste:", minst)

storst = list[0]
for y in list:
    if y > storst:
        storst = y
print("Den storste:", storst)