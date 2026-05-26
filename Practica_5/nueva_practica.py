import heapq

grafo = {
    0: [(10, 1), (20, 2)],
    1: [(10, 0), (50, 3), (10, 4)],
    2: [(20, 0), (33, 4), (20, 3)],
    3: [(50, 1), (20, 2), (20, 4), (2, 5)],
    4: [(10, 1), (33, 2), (20, 3), (1, 5)],
    5: [(2, 3), (1, 4)]
}

def calcular_todos_los_caminos(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        for peso, vecino in grafo[nodo_actual]:
            if vecino == inicio:
                continue
                
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return distancias, predecesores

def formatear_ruta(grafo, predecesores, destino):
    ruta_tuplas = []
    actual = destino
    while actual is not None and predecesores[actual] is not None:
        padre = predecesores[actual]
        peso_arista = next(p for p, v in grafo[padre] if v == actual)
        ruta_tuplas.insert(0, (padre, actual, peso_arista))
        actual = padre
    return ruta_tuplas

nodo_raiz = 2
distancias, padres = calcular_todos_los_caminos(grafo, nodo_raiz)

print(f"--- RUTAS MÁS CORTAS DESDE EL NODO {nodo_raiz} (Formato: [origen, destino, peso]) ---")
print("-" * 70)

for nodo_destino in sorted(grafo.keys()):
    if nodo_destino == nodo_raiz:
        continue
        
    ruta = formatear_ruta(grafo, padres, nodo_destino)
    costo = distancias[nodo_destino]
    
    if costo == float('inf'):
        print(f"Hacia nodo {nodo_destino}: No hay camino posible.")
    else:
        print(f"Hacia nodo {nodo_destino}: {ruta} | Costo Total: {costo}")