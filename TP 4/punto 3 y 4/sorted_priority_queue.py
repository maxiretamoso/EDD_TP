from typing import Any, List, Tuple
from sorted_priority_queue_abstract import SortedPriorityQueueAbstract
from data_structures import PriorityQueueBase

class SortedPriorityQueue(SortedPriorityQueueAbstract, PriorityQueueBase):
    
    def __init__(self):
        self._elements: List[PriorityQueueBase._Item] = [] 


    def __len__(self) -> int:
        return len(self._elements) 


    def __str__(self) -> str:
        return f'Queue = [{", ".join(f"{item._key}: {item._value}" for item in self._elements)}]'


    def is_empty(self) -> bool:
        return len(self) == 0


    def add(self, k: Any, v: Any) -> None:
        elementos = self._Item(k, v) 
        inserted = False
        
        for i in range(len(self._elements)):
            
            if elementos < self._elements[i]:
                self._elements.insert(i, elementos)
                inserted = True
                break
        
        if not inserted:
            self._elements.append(elementos)


    def min(self) -> Tuple[Any]:
        if self.is_empty(): 
            raise Exception("Cola vacía!")
        
        elementos = self._elements[0]  
        return (elementos._key, elementos._value) 
    
    
    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("Cola vacia!")
        
        elementos = self._elements.pop(0)  
        return elementos._key, elementos._value