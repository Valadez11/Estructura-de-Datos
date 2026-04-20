class Pila:
    def __init__(self):
        self.items = []
        self.top_index = -1

    def push(self, numero):
        self.items.append(numero)
        self.top_index += 1
        print(f"Metiendo: {numero}")

    def pop(self):
        if self.is_empty():
            return "Error: Pila vacía"
        self.top_index -= 1
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Nada en el tope"
        return self.items[self.top_index]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.top_index == -1

mi_pila = Pila()

mi_pila.push(10)
mi_pila.push(20)
mi_pila.push(30)

print(f"El número de arriba es: {mi_pila.peek()}") 
print(f"Total de números: {mi_pila.size()}")      

sacado = mi_pila.pop()
print(f"Sacamos el: {sacado}")                   

print(f"Ahora el de arriba es: {mi_pila.peek()}") 
print(f"¿La pila está vacía?: {mi_pila.is_empty()}") 