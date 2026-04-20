def organizar_cola_a_pila(datos_lista):
    cola = list(datos_lista)  
    pila = []                
    print(f"Estado inicial de la COLA: {cola}\n")
    print("-" * 50)

    while len(cola) > 0:
        menor_valor = min(cola) 
        cola.remove(menor_valor)
        
        pila.append(menor_valor)
        
        print(f"Elemento menor encontrado: {menor_valor} -> Movido a la PILA")
        print(f"Cola restante: {len(cola)} elementos")


    print("-" * 50)
    print("\nPROCESO FINALIZADO")
    print(f"Pila resultante (Tope es el mayor): {pila}")
    print(f"¿La cola quedó vacía?: {len(cola) == 0}")


datos_dulces = [
    12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 
    15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75
]

organizar_cola_a_pila(datos_dulces)