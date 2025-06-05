from sorted_priority_queue import SortedPriorityQueue

cola = SortedPriorityQueue()

cola.add(1, "Estructura")
cola.add(2, "Arquitectura")
cola.add(3, "Organizacion")
  
print(f'\nCola antes de los metodos: \n{cola}\n')

print(f'El tamaño de la cola es de: {len(cola)}\n')

cola.add(4, "Analisis II")
print(f'Cola despues de añadir un nuevo elemento: \n{cola}\n')

print(f'El elemento minimo es: {cola.min()}\n')  

{cola.remove_min()}
print(f'Cola despues de eliminar el elemento minimo: \n{cola}\n')

print(f'La cola esta vacia? {cola.is_empty()}\n')  

print(f'Cola despues de los metodos: \n{cola}\n')