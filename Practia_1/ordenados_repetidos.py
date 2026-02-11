x = [1, 2, 3, 4, 4, 4, 5, 7, 8, 9, 11, 11, 13, 14, 15, 16, 16]

no_repetidos = []

for i in x:
    if i not in no_repetidos:
        no_repetidos.append(i)

print(no_repetidos)



