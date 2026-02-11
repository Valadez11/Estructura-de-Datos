toneladas_cereal = [12, 24, 16, 15, 20, 18, 6, 10, 12, 11, 15, 12]
superior = []
inferior =[]

suma = 0 
for i in toneladas_cereal:
    suma += i

promedio = suma / len(toneladas_cereal)

for i in toneladas_cereal:
    if i > promedio:
        superior.append(i)
    else:
        inferior.append(i)

print("El promedio de las toneladas es: ", promedio)
print("Toneladas superiores al promedio: ", superior)
print("Toneladas inferiores al promedio: ", inferior)