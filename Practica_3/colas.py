def enque(saldos, elemento):
    saldos.append(elemento) 

def deque(saldos, retiro):
    enque(retiro,(saldos[0]))
    saldos.pop(0)


def retiros(saldos, retiro):
    r = saldos[0] - retiro[0]
    deque(saldos, retiro)
    enque(saldos, r)

def depositos(saldos, retiro):
    r = saldos[0] + retiro[0]
    deque(saldos, retiro)
    enque(saldos, r)




saldos = []
retiro = []
deposito = []
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
enque(saldos, 1000)
print(saldos)

enque(retiro, 500)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
print(saldos)

enque(deposito, 300)
depositos(saldos, deposito)
depositos(saldos,deposito )
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
print(saldos)




