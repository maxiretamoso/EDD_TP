import os
from mamboreta_admin import mamboretaAdmin

#interfaz del usuario
ejecutar = mamboretaAdmin()

# Busca la ruta del archivo 'imdb.csv' para luego procesarlo:
ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imdb.csv')
ejecutar.procesar_archivo(ruta)                                    

# Filtra el archivo csv por genero(Ciencia ficcion):
filtrar_Genero = ejecutar.filtrar_por_genero('Action')
print('lista por genero:')
print(filtrar_Genero)

# peliculas donde hayan trabajado juntos:
filtrar_compañeros = ejecutar.filtrar_companieros('Daniel Craig','Javier Bardem')
print('Lista por compañeros:')
print(filtrar_compañeros)

# por persona
por_persona = ejecutar.filtrar_por_persona('Leonardo DiCaprio')
print('LISTA FILTRADA POR PERSONA:')
print(por_persona)

# fracasos comerciales:
fracasos = ejecutar.fracasos_comerciales()
print('FRACASOS COMERCIALES:')
print(fracasos)

# top 50 peliculas mas destacadas:
top_50 = ejecutar.top_n()
print('TOP 50:')
print(top_50)