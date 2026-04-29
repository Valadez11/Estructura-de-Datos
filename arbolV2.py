class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def construir_arbol(lista):
    if not lista:
        return None
    
    raiz = Nodo(lista[0])
    
    if len(lista) > 1:
        raiz.izquierdo = Nodo(lista[1]) 
    if len(lista) > 2:
        raiz.izquierdo.derecho = Nodo(lista[2]) 
    if len(lista) > 3:
        raiz.derecho = Nodo(lista[3]) 
    if len(lista) > 4:
        raiz.derecho.derecho = Nodo(lista[4]) 
        
    return raiz


def preorden(nodo):
    if nodo:
        print(nodo.valor, end=", ")
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("none", end=", ")
        preorden(nodo.izquierdo)
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("none", end=", ")
        preorden(nodo.derecho)

def inorden(nodo):
    if nodo:
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("none", end=", ")
        inorden(nodo.izquierdo)
        print(nodo.valor, end=", ")
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("none", end=", ")
        inorden(nodo.derecho)

def postorden(nodo):
    if nodo:
        if nodo.izquierdo is None and nodo.derecho is not None:
            print("none", end=", ")
        postorden(nodo.izquierdo)
        if nodo.derecho is None and nodo.izquierdo is not None:
            print("none", end=", ")
        postorden(nodo.derecho)
        print(nodo.valor, end=", ")


valores = [3, 1, 2, 4, 5]

arbol_raiz = construir_arbol(valores)

print("preorden:", end=" ")
preorden(arbol_raiz)

print("\n\ninorden:", end=" ")
inorden(arbol_raiz)

print("\n\npostorden:", end=" ")
postorden(arbol_raiz)