print("---------------------------------\n")

# oppgave 1
# leser inn temperatur og dato fra fil og lager ordbok som returneres
def lesFraFil(fil):
    fil = open(fil)
    temperaturBok = {}
    for linje in fil:
        setning = linje.strip().split(",")
        temperaturBok[setning[0]] = float(setning[1])
    fil.close()
    return temperaturBok


temperaturBok = lesFraFil("max_temperatures_per_month.csv")
print("Foer:", temperaturBok, "\n")


# oppgave 2 og 3
# sammenligner ordbok fra lesFraFil med ny fil og skriver ut nye varmerekorder
def lesDagligTemperatur(gammelBok, fil):
    fil = open(fil)
    for linje in fil:
        setning = linje.strip().split(",")
        maaned = setning[0]
        dag = setning[1]
        temperatur = float(setning[2])

        if ( temperatur > gammelBok[maaned] ):
            print("Ny varmerekord paa", dag, maaned+":", temperatur, "Celsius (gammel varmerekord var", gammelBok[maaned], "grader Celsius)")
            gammelBok[maaned] = temperatur
    fil.close()
    return gammelBok


oppdatertBok = lesDagligTemperatur(temperaturBok, "max_daily_temperature_2018.csv")
print("\nEtter:", oppdatertBok)


# oppgave 4
def ordbokTilFil(oppdatertBok, filnavn):
    fil = open(filnavn, "w")
    for nokkel in oppdatertBok:
        fil.write(nokkel+","+str(oppdatertBok[nokkel])+"\n")
    fil.close()


ordbokTilFil(oppdatertBok, "nyFil.csv")


# oppgave 5 - ekstraoppgave
def rapporterVarmebolge(filnavn):
    fil = open(filnavn)

    dager = []
    streak = 0

    print("\nRapport for varmebolger 2018")
    for linje in fil:
        setning = linje.strip().split(",")

        maaned = setning[0]
        dag = setning[1]
        temperatur = setning[2]

        if (temperatur > 25):
            dager.append([maaned, dag, temperatur])
            streak += 1




rapporterVarmebolge("max_daily_temperature_2018.csv")

print("\n---------------------------------")