class Persona:
    def __init__(self,nombre:str ):
        self.nombre = nombre
    
    def __repr__(self):
        return f' {self.nombre}'

    def __str__(self):
        return f' {self.nombre}'
    
    def __eq__(self, otro_nombre):
        if isinstance(otro_nombre, Persona):
           return self.nombre == otro_nombre.nombre
        return False