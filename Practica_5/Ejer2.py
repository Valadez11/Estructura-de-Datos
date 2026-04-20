class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Error: La pila está vacía"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

datos_dulces = [12500.5, 11890.0, 13010.35, 14100.0, 13650.8, 14999.99, 15800.0, 16250.25, 15120.0, 14780.4, 13999.0, 15550.75]

datos_dulces.sort()

pil = Pila()

print("Introduciendo valores")
for valor in datos_dulces:
    pil.push(valor)
    print(f"Push: {valor}")

print("\nComprobando pila")
print(f"¿La pila está vacía?: {pil.is_empty()}")
print(f"El tope actual es: {pil.peek()}")

print(Pila)

print("\nVaciando la pila....")
while not pil.is_empty():
    valor_extraido = pil.pop()

print(f"\n¿Pila vacía?: {pil.is_empty()}")