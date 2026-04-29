from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(grafo, inicio):
    cola = deque([inicio])
    nl = set()
    nl.add(inicio)

    resultado = [] 
    
    print(f"Nodo inicial: {inicio}")

    while cola:
        nodo = cola.popleft()
        resultado.append(nodo)
        
        for vecino in grafo[nodo]:
            if vecino not in nl:
                nl.add(vecino)
                cola.append(vecino)
                print(f"agregando nodo: {list(cola)}")

    print(" ".join(resultado))

bfs(grafo, 'A')
    

























