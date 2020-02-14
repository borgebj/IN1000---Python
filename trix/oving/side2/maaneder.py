
maaneder = ["Januar", "Februar", "Mars", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Desember"]

inp = int(input("\nHeltall: "))

if 0 < inp <= 12:
    print("Maaned nr",inp, "er:", maaneder[inp-1]+"\n")
else:
    print(inp, "er ikke et gyldig antall maanedstall.\n")