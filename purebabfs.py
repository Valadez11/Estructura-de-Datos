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
    visitados = {inicio}
    recorrido_final = []

    while cola:
        nodo_actual = cola.popleft()
        print(f"Saca: {nodo_actual}")
        recorrido_final.append(nodo_actual)

        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
        
        if cola:
            estado = "".join(list(cola)).capitalize()
            print(f"Cola: {estado}")


    print(f"RECORRIDO FINAL: {' -> '.join(recorrido_final)}")


bfs(grafo, 'A')