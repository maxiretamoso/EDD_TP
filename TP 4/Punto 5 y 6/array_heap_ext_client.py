from array_heap_ext import ArrayHeapExt


heap1 = ArrayHeapExt()
heap2 = ArrayHeapExt()
    
heap1.add(2,'B')
heap1.add(5,'A')
heap1.add(4,'C')
heap1.add(15,'K')
heap1.add(9,'F')
heap1.add(7,'Q')
heap1.add(6,'Z')
heap1.add(16,'X')
heap1.add(25,'J')
heap1.add(14,'E')
heap1.add(12,'H')
heap1.add(11,'S')
heap1.add(8,'W')
heap1.add(20,'B')
heap1.add(10,'L')
    
heap2.add(1, 'A')
heap2.add(2, 'B')
heap2.add(3, 'C')
heap2.add(4, 'D')
heap2.add(5, 'E')
heap2.add(6, 'F')
heap2.add(7, 'G')
heap2.add(8, 'H')
heap2.add(9, 'I')
    

print(f'\nprimer heap: {heap1}\nSegundo heap: {heap2}\n')

print(f'El elemento minimo es: {heap1.min()}\n')

print(f'Eliminando elemento minimo {heap1.remove_min()}\n')

print(f'Cambiando la prioridad de "25" a "14": {heap1.cambiar_prioridad(25, 14)}\n')

print(f'Borrando los elementos con prioridad "5": {heap1.eliminar_por_prioridad(5)}\n')

print(f'Vaciar el arbol: {heap1.vaciar()}\n')

print(f'El arbol esta vacio? {heap1.is_empty()}\n')

print(f'Heap11: {heap1}\nHeap11: {heap2}\n')

print(f'Fusionando el heap11 con el heap12 {heap1.fusionar(heap2)}\n')
    
print(f'Arbol despues de los metodos: {heap1}\n')