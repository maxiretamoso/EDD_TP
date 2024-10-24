from typing import Any
from data_structures import ArrayHeap
from array_heap_ext_abstract import ArrayHeapExtAbstract

class ArrayHeapExt(ArrayHeap, ArrayHeapExtAbstract):
    
    #metodo __str__ para que se lean mejor los elementos del heap al imprimirlo en el cliente
    def __str__(self):
        return "[" + ", ".join(f"({item._key}, {item._value})" for item in self._data) + "]"


    def fusionar(self, otro: ArrayHeap) -> None:
        for i in range(len(otro)):
            k, v = otro.remove_min()
            self.add(k, v)


    def vaciar(self) -> None:
        self._data.clear()


    def eliminar_por_prioridad(self, k: Any) -> None:        
        for i in range(len(self._data)):
            
            if self._data[i]._key == k:
                indice = i
                break
        
        if indice is None:
            raise ValueError("No existe elemento con ese indice!")
        
        self._data[indice], self._data[-1] = self._data[-1], self._data[indice]   
        self._data.pop()

        if indice < len(self._data):
            self._downheap(indice)
            self._upheap(indice)
            

    def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
        for i in range(len(self._data)):
            
            if self._data[i]._key == k_actual:
                self._data[i]._key = k_nueva
                self._upheap(i)
                self._downheap(i)