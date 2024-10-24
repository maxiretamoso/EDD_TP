from linked_list import LinkedList
from linked_list_ext_abstract import LinkedListExtAbstract
from data_structures import ListNode
from data_structures import LinkedStack
from typing import Any, List

class LinkedListExt(LinkedList, LinkedListExtAbstract):
    
    def __reversed__(self) -> None: 
        """Invierte el orden de los elementos en la lista utilizando un LinkedStack:"""
        
        if self.is_empty():
            raise Exception("La lista esta vacia")
        
        stack = LinkedStack()
        current = self._header.next
        
        while current is not None:
            stack.push(current.element)
            current = current.next
        
        self._header.next = None
        self._size = 0
        while not stack.is_empty():
            self.append(stack.pop())  
        
    def pop(self) -> None: 
        """Quita el último elemento de la estructura:"""
        
        if self.is_empty():
            raise Exception("La  lista esta vacia")
        
        previous = None
        current = self._header

        while current.next:
            previous = current
            current = current.next
            
        if previous:
            previous.next = None

        self._size -= 1
        
    def add_first(self, other: Any) -> None: 
        """Agrega el elemento al principio de la estructura:"""
        
        if other is None:
            raise ValueError("Se debe ingresar datos")
        
        if self.is_empty():
            raise Exception("La lista esta vacia")
        
        if other is None:
             raise ValueError("Se debe ingresar datos")
         
        nuevo_elemento = ListNode(other,self._header.next)
        self._header.next = nuevo_elemento
        self._size += 1
    
    def __iadd__(self, other: List[Any]) -> None:
        """Agrega todos los elementos de other en la estructura actual:"""
        
        if other is None:
            raise ValueError("Se debe ingresar datos")
        
        if self.is_empty():
            raise Exception("La lista esta vacia")
        
        for i in other:
            self.append(i)
        
        return self