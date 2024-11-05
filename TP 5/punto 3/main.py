import re
from data_structures import ProbeHashMap

ruta_archivo = 'C:/Users/Maxi/Desktop/M/Licenciatura en Sistemas/Segundo año 2024 (plan 2012)/Estructura de datos/EDD-TP/TP 5/punto 3/superheroes_villanos.txt'


def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.readlines()

def procesar_datos(datos):
    patron = re.compile(r'(\w+)\(([\w_]+)\)')
    conteo_bando = ProbeHashMap()
    conteo_bando['super_heroe'] = 0
    conteo_bando['villano'] = 0
    personajes = []

    for linea in datos:
        match = patron.match(linea.strip())
        if match:
            bando, nombre = match.groups()
            personajes.append((bando, nombre))
            if bando in conteo_bando:
                conteo_bando[bando] += 1
            else:
                conteo_bando[bando] = 1

    return personajes, conteo_bando

def mostrar_resultados(personajes, conteo_bando):
    print("Listado de personajes:")
    for bando, nombre in personajes:
        print(f"{bando.capitalize()}: {nombre}")

    print("\nConteo total:")
    print(f"Superhéroes: {conteo_bando['super_heroe']}")
    print(f"Villanos: {conteo_bando['villano']}")

if __name__ == "__main__":
    ruta_archivo = 'superheroes_villanos.txt'
    datos = leer_archivo(ruta_archivo)
    personajes, conteo_bando = procesar_datos(datos)
    mostrar_resultados(personajes, conteo_bando)
