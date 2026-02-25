asientos =[ [0,0,0,0,0,0,],
            [0,0,0,0,0,0,],
            [0,0,0,0,0,0,],
            [0,0,0,0,0,0,],
            [0,0,0,0,0,0,],
            [0,0,0,0,0,0,]
]    

def reservar(i, j):
    fila = i - 1
    columna = j - 1
    if asientos[fila][columna] == 1:
        return "El asiento ya fue reservado anteriormente\n"
    else:
        asientos[fila][columna] = 1
        return "Asiento reservado\n"

def liberar(i, j):
    fila = i - 1
    columna = j - 1
    if asientos[fila][columna] == 0:
        return "El asiento ya habia sido liberado con anterioridado\n"
    
    asientos[fila][columna] = 0
    return "Asiento liberado\n"

def consultar(i, j):
    fila = i - 1
    columna = j - 1
    if asientos[fila][columna] == 1:
        return "Estado: Reservado\n"
    else: 
        return "Estado: Libre\n"
    

def total_reservados():
    return sum(sum(fila) for fila in asientos)

def fila_mas_reservada():
    conteo_filas = [sum(fila) for fila in asientos]
    fila_mayor = conteo_filas.index(max(conteo_filas)) + 1
    return fila_mayor



operaciones = [ ("Reservar", 1, 1),
               ("Reservar", 1, 2),
               ("Reservar", 1, 1), 
               ("Consultar", 1, 1), 
               ("Liberar",1, 1),
               ("Liberar", 1, 1),
               ("Reservar", 3, 4), 
               ("Reservar", 6, 6,),
               ("Consultar",6, 6), 
               ("Reservar", 2, 5)
]


for op, i, j in operaciones:
    if op == "Reservar":
        print(reservar(i, j))
    elif op == "Liberar":
        print(liberar(i, j))
    elif op == "Consultar":
        print(consultar(i, j))




print("\nTotal de asientos reservados:", total_reservados())
print("\nFila con más reservados:", fila_mas_reservada())

