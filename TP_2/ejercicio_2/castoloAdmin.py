from typing import List, Dict 
from camiseta import Camiseta
from liga import Liga
from castoloAdminAbstract import CastoloAdminAbstract
from camisetaTipoEnum import CamisetaTipoEnum

class castoloAdmin(CastoloAdminAbstract):
    
    def __init__(self, camisetas: list = None):
        super().__init__()
        self.lista: List[Camiseta] = []
        
    def __str__(self):
        return f"Camiseta {self.nombre}"
        
    def __eq__(self, otraLista):
        if isinstance(otraLista, castoloAdmin):
            return self.lista == otraLista
    
    # Filtra camisetas por tipo de equipacion:
    def filtrar_por_equipacion_tipo(self, equipacion_tipo: CamisetaTipoEnum) -> List[Camiseta]: 
        return [camiseta for camiseta in self.lista if camiseta.equipacion_tipo == equipacion_tipo]
        
    # Filtra camisetas por liga:
    def filtrar_por_liga(self, liga: Liga) -> List[Camiseta]:
        return [camiseta for camiseta in self.lista if camiseta.liga == liga]

    # Filtra camisetas por temporada actual:
    def filtrar_temporada_actual(self, solo_clubes: bool) -> List[Camiseta]: 
        lista_temp : list[Camiseta]=[]
        t_act = 2024
        
        for camiseta in self.lista:
            if t_act == camiseta.temporada:
                if solo_clubes == True:
                    if camiseta.camiseta_tipo == 'Club':
                        lista_temp.append(camiseta)
                    else:
                        lista_temp.append(camiseta)
        return lista_temp

    # Filtra camisetas con stock agotado:
    def stock_agotado(self) -> List[Camiseta]: 
        return [camiseta for camiseta in self.lista if camiseta.agotado]
    
    # Filtra la camiseta mas costosa:
    def mas_costosa(self) -> Camiseta:
        camisa_costosa=self.lista[0]
      
        for camiseta in self.lista:
            if camiseta._precio >= camisa_costosa._precio:
              camisa_costosa = camiseta
        return camisa_costosa
    
    #Filtra la cantidad total de camisetas por liga:
    def totales_por_liga(self) -> Dict[Liga, int]:
        diccionario:dict[Liga,int]={} 
        
        for camiseta in self.lista:
            liga = camiseta.liga
            if liga in diccionario:
                diccionario[liga] += 1
            else:
                diccionario[liga] = 1
        return diccionario      