class Tramite:
    def __init__(self, numero:int, nombre:str, apellido:str, requerimiento:str, terminada:bool):
        self.numero : int = numero
        self.nombre : str = nombre
        self.apellido : str = apellido
        self.requerimiento : str = requerimiento
        self.terminada : bool = terminada

    def __str__(self):
        return f"Número: {self.numero}\nNombre: {self.nombre}\nApellido: {self.apellido}\nRequerimiento: {self.requerimiento}\nTerminada: {self.terminada}\n"
    
    def __eq__(self, other):
        return self.numero == other.numero
    
    def __repr__(self):
        return str(self)
