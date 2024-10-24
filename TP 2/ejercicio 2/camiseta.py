from liga import Liga
from equipo import Equipo
from camisetaTipoEnum import CamisetaTipoEnum
from equipacionTipoEnum import EquipacionTipoEnum
from temporada import Temporada

class Camiseta:
    def __init__(self, sku = int, equipo = Equipo, liga = Liga, camiseta_tipo = CamisetaTipoEnum, equipacion_tipo = EquipacionTipoEnum, mangas_cortas = bool, temporada = Temporada, cantidad = int, precio = float):
        self.sku = sku 
        self.equipo = equipo 
        self.liga = liga
        self.camiseta_tipo = camiseta_tipo
        self.equipacion_tipo = equipacion_tipo
        self.temporada = temporada
        self._cantidad = cantidad
        self._precio = precio
        self.mangas_cortas = mangas_cortas
        
    def __str__(self):
        return f"Sku = {self.sku}, Equipo = {self.equipo}, liga = {self.liga}, Tipo_camiseta = {self.camiseta_tipo}, Tipo_equipacion = {self.equipacion_tipo}, Temporada = {self.temporada}, Cantidad = {self._cantidad}, precio = {self._precio}, Mangas_cortas = {self.mangas_cortas}"
    
    def __eq__(self, otraCamiseta):
        if isinstance(otraCamiseta, Camiseta):
            return self.sku == otraCamiseta.sku
        return False
    
    def __repr__(self) -> str:
        return (
            f"\n- Numero: {self.sku}\n"
            f"- Equipo: {self.equipo}\n"
            f"- Liga: {self.liga}\n"
            f"- Camiseta: {self.camiseta_tipo}\n"
            f"- Equipacion: {self.equipacion_tipo}\n"
            f"- Temporada: {self.temporada}\n"
            f"- Cantidad: {self._cantidad}\n"
            f"- Precio: {self._precio}\n")
    
    @property
    def agotado(self):
        return self._cantidad == 0
    
    def get_cantidad(self):
        return self._cantidad