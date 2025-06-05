from typing import Iterator, List, Any, Generator
from data_structures import MapBase

class SortedTableMap(MapBase):
    
    def __init__(self) -> None:
        self._table: List[MapBase._Item] = []
        
        
    def __len__(self) -> int:
        return len(self._table)
    
    
    def __repr__(self) -> str:
        return self.__str__()
    
    
    def __str__(self) -> str:
        return ', '.join(str(item) for item in self._table)
    
    
    def __getitem__(self, k: Any) -> Any:
        for item in self._table:
            if item._key == k:
                return item._value
        raise KeyError(f'Key {k} no encontrada.')
    
    
    def __setitem__(self, k: Any, v: Any) -> None:
        for item in self._table:
            if item._key  == k:
                item._value = v
                return
        self._table.append(MapBase._Item(k, v))
        self._table.sort(key = lambda x: x._key )
    
    
    def __delitem__(self, k: Any) -> None:
        for item in self._table:
            if item._key == k:
                self._table.remove(item)
                return
        raise KeyError("La clave no se encontro")
    
    
    def __iter__(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key
    
    
    def iter_items(self) -> Generator[Any, None, None]:
        for item in self._table:
            yield item._key, item._value