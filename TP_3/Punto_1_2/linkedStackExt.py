from linked_stack_ext_abstract import LinkedStackExtAbstract
from typing import Any, List
from data_structures import LinkedStack

class linkedStackExt(LinkedStackExtAbstract, LinkedStack):

    def multi_pop(self, num: int) -> List[Any]:
        if self.is_empty():
            raise Exception ("la pila esta vacia")

        if num>self._size:
            raise Exception (f"No se pueden hacer {num} porque la pila tiene {self._size} elementos")

        elementos_pop = []
        for __ in range(num):
            elementos_pop.append(self.pop())
        
        return elementos_pop

    def replace_all(self, param1: Any, param2: Any) -> None:
        pila = []
        
        while not self.is_empty(): 
            contenido = self.pop()  
            
            if contenido == param1:
                pila.append(param2) 
            else:
                pila.append(contenido)  
        
        while pila:
            self.push(pila.pop())
    
    def __imul__(self, other: int) -> None:
        if self._head is None:
            raise ValueError("La pila está vacía, no se pueden repetir elementos.")
        
        elementosActual = self._head
        repetirElemento = []
        
        if other < 0:
            raise ValueError("No se puede seguir repitiendo, 'other' llego a 0")
        
        while elementosActual is not None:
            repetirElemento.append(elementosActual.element)
            elementosActual = elementosActual.next

        for _ in range(other):
            for contenido in repetirElemento:
                self.push(contenido)