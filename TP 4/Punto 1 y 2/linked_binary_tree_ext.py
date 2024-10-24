from data_structures import LinkedBinaryTree, BinaryTreeNode, LinkedQueue
from linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract

class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):
    def ancestro_mas_inmediato(self, nodo_actual1: BinaryTreeNode, nodo_actual2: BinaryTreeNode):
        camino_nodo_actual1 = []
        camino_nodo_actual2 = []

        actual = nodo_actual1
        while actual:
            camino_nodo_actual1.append(actual)
            actual = self._search_parent(actual)

        actual = nodo_actual2
        while actual:
            camino_nodo_actual2.append(actual)
            actual = self._search_parent(actual)

        ancestro_comun = None
        for ancestro1, ancestro2 in zip(reversed(camino_nodo_actual1), reversed(camino_nodo_actual2)):
            if ancestro1 == ancestro2:
                ancestro_comun = ancestro1
            else:
                break

        return ancestro_comun

    def hojas(self) -> list:
        hojas = []
        stack = [self._root] 
        
        while stack:
            nodo_actual = stack.pop() 
            
            if nodo_actual is not None and nodo_actual.children_count == 0:
                hojas.append(nodo_actual.element)
            
            if nodo_actual is not None: 
                if nodo_actual.right_child:
                    stack.append(nodo_actual.right_child)
                if nodo_actual.left_child:
                    stack.append(nodo_actual.left_child)

        return hojas


    def nivel(self, nodo: BinaryTreeNode) -> int:
        queue = LinkedQueue() 
        queue.enqueue(self._root)
        nodo_actual = queue.dequeue()
        nivel = 0
        
        if self._root is None:
            return 0 


        for _ in range(len(queue)):

            if nodo_actual == nodo: 
                return nivel


    def diametro(self) -> int:
        diametro = 0
        queue = LinkedQueue()  
        queue.enqueue(self._root)
        
        if self._root is None:
            return True
        
        while not queue.is_empty():
            diametro = max(diametro, len(queue))  

            for _ in range(len(queue)):  
                actual = queue.dequeue() 
                
                if actual.left_child:  
                    queue.enqueue(actual.left_child)  
                        
                if actual.right_child:  
                    queue.enqueue(actual.right_child)  

        return diametro


    def es_balanceado(self) -> bool:
        altura = {None: 0}
        stack = [(self._root, 0)]
        
        if self._root is None:
            return True

        while stack:
            nodo_actual, posicion = stack.pop()

            if posicion == 0:
                stack.append((nodo_actual, 1))
                    
                if nodo_actual.left_child:
                    stack.append((nodo_actual.left_child, 0))
                
                if nodo_actual.right_child:
                    stack.append((nodo_actual.right_child, 0))
            
            else:
                izquierda = altura.get(id(nodo_actual.left_child), 0)
                derecha = altura.get(id(nodo_actual.right_child), 0)
                
                if abs(izquierda - derecha) > 1:
                    return False
                        
                altura[id(nodo_actual)] = max(izquierda, derecha) + 1
                
        return True