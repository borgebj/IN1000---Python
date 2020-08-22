from time import sleep
print("")

skattekart = []
stoerrelse = 5

for x in range(stoerrelse):
    rader = []

    for y in range(stoerrelse):
        rader.append("O")

    skattekart.append(rader)

for hver in skattekart:
    for each in hver:
        print(each, end="  ")
    print("")


print("")

x = int(input("X-Koordinat: "))
while x < 1 or x > 5:
    print("Ugyldig koordinat")
    x = int(input("X-Koordinat: "))

y = int(input("Y-Koordinat: "))
while y < 1 or y > 5:
    print("Ugyldig koordinat")
    y = int(input("Y-Koordinat: "))

print("")

skattekart[y-1][x-1] = "X"
for hver in skattekart:
    for each in hver:
        print(each, end="  ")
    print("")

sleep(2)
for x in range(20):
    print("")

vunnet = False
forsok = 3
while vunnet == False and forsok > 0:
    print("\nDu har",forsok,"antall forsok:")

    x = int(input("X-Koordinat: "))
    while x < 1 or x > 5:
        print("Ugyldig koordinat")
        x = int(input("X-Koordinat: "))

    y = int(input("Y-Koordinat: "))
    while y < 1 or y > 5:
        print("Ugyldig koordinat")
        y = int(input("Y-Koordinat: "))

    if skattekart[y-1][x-1] == "X":
        print("\nGratulerer! Du fant skatten og har vunnet.")
        sleep(2)
        vunnet = True
    else:
        print("\nDu fant ikke skatten\n")
        skattekart[y-1][x-1] = "#"
        forsok -= 1

if not vunnet:
    print("\nSpiller 2 vant spillet\n")
    for hver in skattekart:
        for each in hver:
            print(each, end="  ")
        print("")
    print("")
else:
    print("\nSpiller 1 vant spillet\n")
    for hver in skattekart:
        for each in hver:
            print(each, end="  ")
        print("")
    print("")
