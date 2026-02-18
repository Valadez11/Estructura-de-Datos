import pandas as pd

def calcular_media(lista):
    suma = 0
    for i in lista:
        suma += i
    media = suma / len(lista)
    print(media)
    return media


def calcular_moda(lista):
    frecuencias = {}
    for x in lista:
        frecuencias[x] = frecuencias.get(x, 0) + 1
    moda = max(frecuencias, key=frecuencias.get)
    return print(moda)


def calcular_desviacion_estandar(lista):
    varianza = calcular_varianza(lista)
    desviacion = varianza ** 0.5
    return print(desviacion)


def analizar_columna(ruta_csv, nombre_columna):
    df = pd.read_csv(ruta_csv)
    datos = list(df[nombre_columna])

    calcular_media(datos)
    calcular_moda(datos)
    calcular_varianza(datos)
  

def calcular_varianza(lista):
    media = calcular_media(lista)
    suma_cuadrados = 0
    for i in lista:
        suma_cuadrados += (i-media) ** 2
        print(suma_cuadrados)
        return suma_cuadrados / len(lista)
    





analizar_columna('Practica_2/Housing.csv', 'price')

    





'''
def calcular_desviacion(lista):
    return calcular_varianza(lista) ** 0.5
'''

'''
df = pd.read_csv('Practica_2/Housing.csv') 
lista = list(df['price'])
'''