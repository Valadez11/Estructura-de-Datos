from collections import deque

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class Arbol:
    def __init__(self, datos=None):
        self.raiz = None
        if datos:
            for valor in datos:
                self.insertar(valor)

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
            return

        cola = deque([self.raiz])
        while cola:
            nodo = cola.popleft()

            if nodo.izquierdo is None:
                nodo.izquierdo = nuevo_nodo
                break
            else:
                cola.append(nodo.izquierdo)

            if nodo.derecho is None:
                nodo.derecho = nuevo_nodo
                break
            else:
                cola.append(nodo.derecho)


def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)
    else:
        print("none", end=" ") 

def inorden(nodo):
    if nodo:
        inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        inorden(nodo.derecho)

def postorden(nodo):
    if nodo:
        postorden(nodo.izquierdo)
        postorden(nodo.derecho)
        print(nodo.valor, end=" ")


mi_arbol = Arbol([1, 2, 3, 4, 5])

print("Preorden: "); preorden(mi_arbol.raiz)    
print("\nInorden: "); inorden(mi_arbol.raiz)     
print("\nPostorden: "); postorden(mi_arbol.raiz) 