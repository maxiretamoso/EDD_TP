from data_structures import BinaryTreeNode
from linked_binary_tree_ext import LinkedBinaryTreeExt

arbol = LinkedBinaryTreeExt()

a = BinaryTreeNode('A')
b = BinaryTreeNode('B')
c = BinaryTreeNode('C')
d = BinaryTreeNode('D')
e = BinaryTreeNode('E')
f = BinaryTreeNode('F')
g = BinaryTreeNode('G')
h = BinaryTreeNode('H')
i = BinaryTreeNode('I')

arbol.add_root(a)
arbol.add_left_child(a,b)
arbol.add_right_child(a,c)
arbol.add_left_child(b,d)
arbol.add_right_child(b,e)
arbol.add_left_child(c,f)
arbol.add_right_child(c,g)
arbol.add_left_child(d,h)
arbol.add_right_child(d,i)

print(f'\nLas hojas del arbol son: {arbol.hojas()}\n')

print(f'El nivel del nodo D es: {arbol.nivel(d)}\n')

ancestro_inmediato = arbol.ancestro_mas_inmediato(h, i)
print(f'El ancestro mas inmediato entre H e I es: {ancestro_inmediato.element}\n')

print(f'El Diametro del árbol es: {arbol.diametro()}\n')

print(f'El arbol esta balanceado? {arbol.es_balanceado()}\n')