import re
from procesar_superheroes_villanos import Personaje

class Main():
    personajes = Personaje('TP 5\\Punto3\\superheroes_villanos.txt')
    personajes.procesar_archivo()
    personajes.mostrar_resultados()

if __name__ == '__main__':
    Main()