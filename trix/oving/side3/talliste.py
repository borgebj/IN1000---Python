

x = 5
tall = []
while x > 0:
    inp = int(input("Skriv inn heltall: "))
    tall.append(inp)
    x -= 1

sum = 0
for a in tall:
    sum += a
print("Totalsum:", sum)

for b in tall:
    if b < 10:
        print(b)

if 5 in tall:
    print("Verdien 5 finnes i listen")
else:
    print("Verdien 5 finnes ikke i listen")