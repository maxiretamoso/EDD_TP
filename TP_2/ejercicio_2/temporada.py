from liga import Liga

class Temporada(Liga):
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
    
    def __str__(self):
        return f'Nombre = {self.nombre}, Anio = {self.anio}'
        
    def __eq__(self, otraTemporada):
        if isinstance(otraTemporada, Temporada):
            return self.nombre == otraTemporada.nombre    
        return False