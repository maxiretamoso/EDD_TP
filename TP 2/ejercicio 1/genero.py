class Genero:
    def __init__(self, genero: str):
        self.genero = genero
       
    def __str__(self):
       return f'Genero: {self.genero}'
    
    def __eq__(self, otro_genero):
       if isinstance(otro_genero, Genero):
           return self.genero == otro_genero.genero
       return False

    def __repr__(self) -> str:
        return self.__str__()