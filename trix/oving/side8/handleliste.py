

def fjern_utsolgte(handleliste, utsolgte):
    for vare in handleliste:
        if vare in utsolgte:
            handleliste.remove(vare)
    return handleliste


handleliste = ["melk", "brus", "pasta", "loff", "rundstykker", "tannkrem"]
utsolgte = ["melk", "pasta", "tannkrem"]
ny = fjern_utsolgte(handleliste, utsolgte)
print(ny)