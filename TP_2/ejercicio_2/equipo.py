class Equipo:
    def __init__(self, nombre, liga):
        self.nombre = nombre
        self.liga = liga
        
    def __str__(self):
        return f'Nombre = {self.nombre}, Liga = {self.liga}'
    
    def __eq__(self, otroEquipo):
        if isinstance(otroEquipo, Equipo):
            return self.nombre == otroEquipo.nombre
        return False