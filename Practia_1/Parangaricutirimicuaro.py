cadena = "Parangaricutirimicuaro"

conteoMin = [0] * 26
conteoMayus = [0] * 26

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

for l in cadena:    
    for i in range(26):
        if l == minus[i]:
            conteoMin[i] += 1

for i in range(26):
    if conteoMin[i] > 0:
        print(minus[i], ":", conteoMin[i])







    






