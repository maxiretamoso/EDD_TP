from camiseta import Camiseta
from castoloAdmin import castoloAdmin

ejecutar = castoloAdmin()

camiseta1 = Camiseta(1, "San lorenzo", "Liga Argentina", "Club", "Local", True, 2024, 10, 90000)
camiseta2 = Camiseta(9, "Belgrano", "Liga Argentina", "Club", "Visitante", True, 2024, 15, 79000.50)
camiseta3 = Camiseta(10, "Botafogo", "Brasileirao", "Club", "Alternativa", True, 2024, 0, 80000)
camiseta4 = Camiseta(13, "Palmeiras", "Brasileirao", "Club", "Visitante", True, 2010, 10, 34000.90)
camiseta5 = Camiseta(14, "Aucas", "Chile", "Club", "Local", True, 2022, 15, 20000.99)

ejecutar.append(camiseta1)
ejecutar.append(camiseta2)
ejecutar.append(camiseta3)
ejecutar.append(camiseta4)
ejecutar.append(camiseta5)

# Filtra las camisetas por tipo de equipación:
equip = ejecutar.filtrar_por_equipacion_tipo('Local')
print(f"Camisetas con equipacion Local:\n{equip}\n")

# Filtra las camisetas por liga:
lig = ejecutar.filtrar_por_liga('Liga Argentina')
print(f"Camisetas de la Liga Argentina:\n{lig}\n")

# Filtrado por temporada actual:
t_actual = ejecutar.filtrar_temporada_actual(True)
print(f"Camisetas de la temporada actual:\n{t_actual}\n")

# Camisetas sin stock:
sin_stock = ejecutar.stock_agotado()
print(f"Camisetas agotadas de:\n{sin_stock}\n")

# La camiseta más costosa de la lista:
mas_costosa = ejecutar.mas_costosa()
print(f"La camiseta mas costosa es la de {mas_costosa.equipo}: ${mas_costosa._precio}\n")

# Devuelve un diccionario con el número total de camisetas por liga:
tot_liga = ejecutar.totales_por_liga()
print(f"Camisetas totales por liga: {tot_liga}\n")
