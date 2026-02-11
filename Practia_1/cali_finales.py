calificaciones = [8, 8, 7, 5, 10, 9, 9, 5, 6, 10]
alum_aprob = 0
alum_reprob = 0
mayoresIgual_8 = 0


suma = 0
for i in calificaciones:
    suma += i

promedio = suma / len(calificaciones)

print("El promedio general del grupo es: ", promedio)

for i in calificaciones:
    if i >= 6:
        alum_aprob += 1
    else:
        alum_reprob += 1

print("Alumnos aprobados: ", alum_aprob)
print("Alumnos reprobados: ", alum_reprob)

porcentajeAprob = (alum_aprob / len(calificaciones))*100
porcentajeReprob = (alum_reprob / len(calificaciones))*100

print("Alumnos aprobados: ", porcentajeAprob, "%")
print("Alumnos reprobados: ", porcentajeReprob, "%")

for i in calificaciones:
    if i >= 8:
        mayoresIgual_8 += 1
print("Alumnos mayores o iguales a 8: ", mayoresIgual_8)

