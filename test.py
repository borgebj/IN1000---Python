
def lagSynonymordbok(synonymer):
    ordbok = {}

    for liste in synonymer:
        for bokstav in liste:
            liste.remove(bokstav)
            synonymliste = liste
            ordbok[bokstav] = synonymliste
            print(bokstav, "-", synonymliste)

    return ordbok

synonymer = [
    ["a", "e", "i", "o", "u"],
    ["HOM", "c", "d"],
    ["y", "HOM"],
    ["k", "l", "m", "n", "p", "q"],
    ["x"]
]

synonymordbok = lagSynonymordbok(synonymer)
for x in synonymordbok:
    print(x, "-", synonymordbok[x])


print(synonymordbok)
assert synonymordbok["e"] == [ ["a", "i", "o", "u"] ]
assert synonymordbok["a"] == [ ["e", "i", "o", "u"] ]
assert synonymordbok["u"] == [ ["a", "e", "i", "o"] ]
assert synonymordbok["c"] == [ ["HOM", "d"] ]
assert synonymordbok["HOM"] == [ ["c", "d"], ["y"] ]
assert synonymordbok["x"] == [ [] ]


