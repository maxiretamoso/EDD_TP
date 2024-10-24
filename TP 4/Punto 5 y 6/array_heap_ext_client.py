from array_heap_ext import ArrayHeapExt

heap = ArrayHeapExt()
otro_heap = ArrayHeapExt()
    
heap.add(2,'B')
heap.add(4,'C')
heap.add(5,'A')
heap.add(6,'Z')
heap.add(7,'Q')
heap.add(8,'W')
heap.add(9,'F')
heap.add(10,'L')
heap.add(11,'S')
heap.add(12,'H')
heap.add(14,'E')
heap.add(15,'K')
heap.add(16,'X')
heap.add(20,'B')
heap.add(25,'J')

otro_heap.add(1, 'A')
otro_heap.add(2, 'E')
otro_heap.add(3, 'I')
otro_heap.add(4, 'O')
otro_heap.add(5, 'U')

print(f'\nHeap antes de los metodos: \n{heap}\n')

print(f'otro_heap antes de los metodos: \n{otro_heap}\n')

{heap.fusionar(otro_heap)}
print(f'Heap despues de fusionarlo con otro_heap: \n{heap}\n')

{heap.eliminar_por_prioridad(5)}
print(f'Heap despues de borrar los elementos de prioridad "5": \n{heap}\n')

{heap.cambiar_prioridad(14, 20)}
print(f'Heap despues de cambiar la prioridad de "14" a "20": \n{heap}\n')

{heap.vaciar()}
print(f'Heap despues de vaciarlo: \n{heap}\n')