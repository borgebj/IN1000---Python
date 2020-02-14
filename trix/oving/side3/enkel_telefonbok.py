
dict = {"Arne":22334455, "Lisa":95959595, "Jonas":97959795, "Peder":12345678}

inp = input("\nSkrv inn navn: ")

if inp.capitalize() in dict:
    print("Nummeret til",inp.capitalize()+":", dict[inp.capitalize()],"\n")
else:
    print(inp.capitalize(),"finnes ikke i telefonboken\n")