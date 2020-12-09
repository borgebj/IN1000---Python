

def brillesjekk1(styrke):
    ny_styrke = [2.5, 2.75]
    return ny_styrke


def brillesjekk2(styrke):
    styrke[0] = 1.75


styrke1 = [1.5, 1.5]
brillesjekk1(styrke1)
print(styrke1[0])

#1.5
#bruker ikke det som returneres fra brillesjekk1

styrke2 = [1.5, 1.5]
brillesjekk2(styrke2)
print(styrke2[0])

#1.75