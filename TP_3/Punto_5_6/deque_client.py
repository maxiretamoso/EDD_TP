from abstractQueue import DequeAbstractQueue

lista = DequeAbstractQueue()

for numeros in [10,9,8,7,6,5]:
    lista.add_first(numeros)

for numeros in [11,12,13,14,15,16]:
    lista.add_last(numeros)

#Devuelve la deque con los numeros agregados:
print(f'\nDeque original: {lista}\n')

#Devuelve la longitud de la deque:
tamañoDeLaLista = lista.__len__()
print(f'Total de elementos: {tamañoDeLaLista}\n')

#Devuelve el primer elemento de la deque:
primerElemento = lista.first()
print(f'Primer elemento de la lista: {primerElemento}\n')

#Devuelve el ultimo elemento de la deque:
ultimoElemento = lista.last()
print(f'Ultimo elemento de la lista: {ultimoElemento}\n')

#Elimina el primer y ultimo elemento de la deque:
lista.delete_first()
lista.delete_last()
print(f'Deque despues de la eliminacion: {lista}\n')

#La deque esta esta vacia: True o False
print(f'La deque esta vacia: {lista.is_empty()}\n')