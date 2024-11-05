from sorted_table_map import SortedTableMap

map = SortedTableMap()

# metodo __setitem__ 
map['a'] = 1
map['c'] = 3
map['b'] = 2
print(f'Map despues de agregar elementos:  {map}')

# metodo __getitem__
try:
    print(f'Valor para la clave {'b'}: {map['b']}')
except KeyError as e:
    print(e)
    
# metodo __setitem__
map['a'] = 10
print(f'Map después de actualizar la clave {'a'}: {map}')

# metodo __delitem__
try:
    del map['b']
    print(f'Map después de eliminar la clave {'b'}: {map}')
except KeyError as e:
    print(e)
    
# metodo __len__
print(f'Longitud del map: {len(map)}')

# metodo iter_items()
print("Elementos en el map:")
for item in map.iter_items():
    print(item)