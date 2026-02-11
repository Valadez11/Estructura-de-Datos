cadena = "Parangaricutirimicuaro"

conteo = {}

for i in cadena:
    if i in conteo:
        conteo[i] += 1
    else:
        conteo[i] = 1

for i, cantidad in conteo.items():
    print(i, ":", cantidad)