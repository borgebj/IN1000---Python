
honer = int(input("\nHvor manger honer bor paa gaarden?: "))
rev = input("Kommer reven denne natten?: ")
bonde = input("Sover bonden denne natten?: ")

if rev.lower() == "ja" and bonde.lower() == "ja":
    honer -= 1
    print("\nEn hone ble spist av reven")
    print("Det bor na",honer, "antall honer pa garden\n")

elif rev.lower() == "ja" and bonde.lower() == "nei":
    print("\nDet bor naa",honer,"antall honer pa garden")
    print("Bonden tjente 190kr for reveskinnet\n")
else:
    print("\nIngenting skjedde\n")