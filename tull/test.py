import time
k = input("Skriv inn ordet bil: ")

while k.lower() != "bil":
    print("Mente du bil?\n")
    time.sleep(1.5)
    k = input("Skriv inn ordet bil: ")

print("\nDet er riktig\n")