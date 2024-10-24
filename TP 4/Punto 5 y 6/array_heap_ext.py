from typing import Any
from data_structures import ArrayHeap
from array_heap_ext_abstract import ArrayHeapExtAbstract

class ArrayHeapExt(ArrayHeap, ArrayHeapExtAbstract):

    def fusionar(self, otro: ArrayHeap) -> None:
        for i in range(len(otro)):
            key, value = otro.remove_min()
            self.add(key, value)


    def vaciar(self) -> None:
        self._data.clear()


    def eliminar_por_prioridad(self, k: Any) -> None:
        indices_a_eliminar = [i for i, item in enumerate(self._data) if item._key == k]
        
        for index in reversed(indices_a_eliminar):
            self._swap(index, len(self._data) - 1)  
            self._data.pop()  
            
            if index < len(self._data):
                self._downheap(index)


    def cambiar_prioridad(self, k_actual: Any, k_nueva: Any) -> None:
        for i, item in enumerate(self._data):
            
            if item._key == k_actual:
                self._data[i] = self._Item(k_nueva, item._value)  
                
                if k_nueva < k_actual:
                    self._upheap(i) 
                else:
                    self._downheap(i)