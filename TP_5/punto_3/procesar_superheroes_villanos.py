import re
from data_structures import ProbeHashMap

class Personaje:
    
    def __init__(self, archivo) -> None:
        self.archivo = archivo
        self.heroes_cantidad = 0
        self.villanos_cantidad = 0
        self.hash_map = ProbeHashMap()
        
        
    def procesar_archivo(self):
        pattern = r"(super_heroe|villano)\((\w+)\)"
        
        with open('superheroes_villanos.txt') as archivo:
            for line in archivo:
                match = re.match(pattern, line.strip())
                if match:
                    entity_type, name = match.groups()
                    self.agregar(entity_type, name)
    
    
    def agregar(self, entity_type, name):
        
        if entity_type == "super_heroe":
            self.heroes_cantidad += 1
            self.hash_map[name] = "super_heroe"
        elif entity_type == "villano":
            self.villanos_cantidad +=1
            self.hash_map[name] = "Villano"
        
        
    def cantidad(self):
        return self.heroes_cantidad, self.villanos_cantidad             
            
            
    def mostrar_resultados(self):
        print("\nListado de personajes:\n") 
        
        for name, tipo in self.hash_map.items():  
            print(f"{tipo}: {name}") 
            
        print("\nConteo total:\n") 
        print(f"Superheroes: {self.heroes_cantidad}") 
        print(f"Villanos: {self.villanos_cantidad}\n")