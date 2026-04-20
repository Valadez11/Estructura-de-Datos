def transferir_cola_a_pila(datos_lista):
    # 1. Inicializamos las estructuras
    cola = list(datos_lista)  # Simulamos la cola original
    pila = []                 # Aquí guardaremos los datos ordenados
    
    print("--- INICIANDO TRANSFERENCIA ---")
    
    # 2. Mientras la cola no esté vacía (is_empty)
    while len(cola) > 0:
        # Encontramos el menor valor actual en la cola
        valor_menor = min(cola)
        
        # Extraemos ese valor de la cola (Dequeue)
        cola.remove(valor_menor)
        
        # Lo insertamos en la pila (Push)
        pila.append(valor_menor)
        
        print(f"Transferido: {valor_menor}")

    # 3. Mostrar la pila final ordenada
    print("\n--- RESULTADO FINAL ---")
    print(f"Pila ordenada (Base -> Tope): {pila}")
    
    if len(pila) > 0:
        print(f"Elemento en el TOPE: {pila[-1]}")
        print(f"Elemento en la BASE: {pila[0]}")

# --- DATOS DE LA COLUMNA 'DULCES' ---
datos_dulces = [
    12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 
    15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75
]

transferir_cola_a_pila(datos_dulces)