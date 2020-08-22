
print("")
saldo = float(input("Hva er din saldo?: "))

vare = float(input("Hva er prisen pa varen du vil kjope?: "))

if vare > saldo:
    print("Du har ikke rad, du mangler", vare-saldo,"kroner")
else:
    print("\nDu har rad, med", saldo-vare,"kroner igjen")
print("")