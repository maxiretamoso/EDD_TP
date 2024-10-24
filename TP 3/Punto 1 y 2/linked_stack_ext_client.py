from linkedStackExt import linkedStackExt

class Linked_Stack_Ext_Client(linkedStackExt):
    pila_nueva = linkedStackExt()
    pila_nueva.push(1)
    pila_nueva.push(2)
    pila_nueva.push(2)
    pila_nueva.push(2)
    pila_nueva.push(5)
    pila_nueva.push(6)

    print(f'\nElementos eliminados de la pila: {pila_nueva.multi_pop(3)}\n')
    
    print(f'Pila luego de 3 pops y cambiando 2 por 6: {pila_nueva.replace_all(2,6)}\n')
  
    print(f'Pila nueva: {pila_nueva.__imul__(2)}\n')