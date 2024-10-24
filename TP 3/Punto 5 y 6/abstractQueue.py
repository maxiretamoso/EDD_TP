from typing import Any, Optional
from data_structures import ListNode
from Deque import DequeAbstract

class DequeAbstractQueue(DequeAbstract):
    def __init__(self) -> None:
        """Inicializa una deque vacía."""
        self._front: Optional[ListNode] = None
        self._rear: Optional[ListNode] = None
        self._size = 0

    def __len__(self) -> int:
        """Devuelve la cantidad actual de elementos en la deque."""
        return self._size
    
    def __str__(self) -> str:
        
        if self.is_empty():
            return DequeAbstractQueue
        
        elementos = []
        actual = self._front
        while actual is not None:
            elementos.append(str(actual.element))
            actual = actual.next
        return f'Deque({elementos})'

    def is_empty(self) -> bool:
        return self._size == 0
            
    def first(self) -> Any:
        if self.is_empty():
            raise Exception("Estructura vacia")
        return self._front.element

    def last(self) -> Any:
        if self.is_empty():
            raise Exception("Estructura vacia")
        return self._rear.element

    def add_first(self, element: Any) -> None:
        nodo = ListNode(element) 
        if self.is_empty():
            self._front = nodo
            self._rear = nodo
        else:
            nodo.next = self._front 
            self._front = nodo  
        self._size += 1
    
    def add_last(self, element: Any) -> None:
        nodo = ListNode(element)
        if self.is_empty():
            self._front = nodo
            self._rear = nodo
        else:
            self._rear.next = nodo
            self._rear = nodo
        
        self._size += 1
    
    def delete_first(self) -> None:
        if self.is_empty():
            raise Exception("La Estructura esta vacia")
        self._front = self._front.next
        
        if self._front is None:
            self._rear = None
        self._size -=1
    
    def delete_last(self) -> None:
        """Elimina el último elemento de la deque."""
        if self.is_empty():
            raise Exception("La deque está vacía")
        if self._front == self._rear:
            self._front = self._rear = None
        else:
            current = self._front
            while current.next != self._rear:
                current = current.next
            current.next = None
            self._rear = current
        self._size -= 1 