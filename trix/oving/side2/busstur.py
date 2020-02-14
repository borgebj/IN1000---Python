
total = 0

s1 = int(input("\nStasjon 1! Hvor mange gaar paa bussen?: "))
total += s1
if total == 30:
    print("Bussen er naa full\n")
elif total > 30:
    print("Bussen er full!",total-30,"person/er maa gaa til fots\n")

else:
    s2 = int(input("\nStasjon 2! Hvor mange gaar paa bussen?: "))
    total += s2
    if total == 30:
        print("Bussen er naa full\n")
    elif total > 30:
        print("Bussen er full!",total-30,"person/er maa gaa til fots\n")

    else:
        s3 = int(input("\nStasjon 3! Hvor mange gaar paa bussen?: "))
        total += s3
        if total == 30:
            print("Bussen er naa full\n")
            print(total,"antall passassjerer kom til endestasjon\n")
        elif total > 30:
            print("Bussen er full!",total-30,"person/er maa gaa til fots\n")
        else:
            print(total,"antall passassjerer kom til endestasjon\n")