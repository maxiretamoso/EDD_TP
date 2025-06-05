class Liga:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __str__(self):
        return f'Nombre = {self.nombre}'
    
    def __eq__(self, otraLiga):
        if isinstance(otraLiga, Liga):
            return self.nombre == otraLiga.nombre
        return False
    
    def __hash__(self) -> int:
        return hash(self.nombre)