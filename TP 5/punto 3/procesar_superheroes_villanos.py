import re
from data_structures import ProbeHashMap

class Personaje:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.heroes_cantidad = 0
        self.villano_cantidad = 0
        self.hash_map = ProbeHashMap()
        
    def procesar_archivo(self):
        pattern = r"(superheroe|villano)\((\w+)\)"
        with open (self.filename, 'r') as file:
            for line in file:
                match = re.match(pattern, line.strip())
                if match:
                    entity_type, name = match.groups()
                    self.agregar(entity_type, name)
    
    def agregar(self, entity_type, name):
        
        if entity_type == "super_heroe":
            self.heroes_cantidad += 1
            self.hash_map[name] = "Heroe"
        elif entity_type == "villano":
            self.villano_cantidad +=1
            self.hash_map[name] = "Villano"
        
    def cantidad(self):
        return self.heroes_cantidad, self.villano_cantidad

