from data_structures import MapBase
from sorted_table_map_abstract import SortedTableMapAbstract
from typing import List, Any, Generator

class SortedTableMap(SortedTableMapAbstract):
    
    def __init__(self) -> None:
        self._table = []
        
        
    def __len__(self) -> int:
        return len(self._table)
    
    
    def __str__ (self) -> str:
        for item in self._table:
            return ", ".join(str(item))
    
    
    def __repr__(self) -> str:
        return str(self)
    
    
    def __getitem__(self, k: Any) -> Any:
        low, high = 0, len(self._table) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self._table[mid]._key == k:
                return self._table[mid]._value
            elif self._table[mid]._key < k:
                low = mid + 1
            else:
                high = mid - 1
                
        raise KeyError(f"Clave {k} no encontrada.")
    
    
    def __setitem__(self, k: Any, v: Any) -> None:
        low, high = 0, len(self._table) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self._table[mid]._key == k:
                self._table[mid]._value = v
                return
            elif self._table[mid]._key < k:
                low = mid + 1
            else:
                high = mid - 1
                
        self._table.insert(low, self._Item(k, v))     
    
    
    def __delitem__(self, k: Any) -> None:
        low, high = 0, len(self._table) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if self._table[mid]._key == k:
                self._table.pop(mid)
                return
            elif self._table[mid]._key < k:
                low = mid + 1
            else:
                high = mid - 1
                
        raise KeyError(f"Clave {k} no encontrada.")
        
        
    def __iter__(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key


    def iter_items(self) -> Generator[MapBase._Item, None, None]:
        for item in self._table:
            yield item