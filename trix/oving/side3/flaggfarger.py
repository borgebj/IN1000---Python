
flaggOrdbok = {"norge" : ["rødt", "hvitt", "blått"],
              "sverige" : ["blått", "gult"],
              "danmark" : ["rødt", "hvitt"],
              "finnland" : ["hvitt", "blått"],
              "japan" : ["rødt", "hvitt"],
              "gabon" : ["grønt", "gult", "blått"],
              "storbritannia" : ["rødt", "blått", "hvitt"],
              "chile" : ["blått", "hvitt", "rødt"]}

for x in flaggOrdbok:
    print("\n"+x,"har fargene",flaggOrdbok[x])

flaggOrdbok["USA"] = ["rødt", "hvit", "blått"]

"""def prosedyre(land):
    print("\nFargene til",land,"er:",flaggOrdbok[land.lower()],"\n")

prosedyre("Japan")
"""

def prosedyre():
    inp = input("Land?: ")
    if inp in flaggOrdbok:
        print(flaggOrdbok[inp])
prosedyre()