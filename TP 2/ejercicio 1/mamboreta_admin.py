from typing import List
from mamboretaAdminAbstract import MamboretaAdminAbstract
import csv
from pelicula import Pelicula
from persona import Persona
from genero import Genero

class mamboretaAdmin(MamboretaAdminAbstract):
    def procesar_archivo(self, ruta : str) -> None:
        with open(ruta,mode = 'r', encoding = "utf-8", newline = '') as file:
            reader = csv.DictReader(file)
            for row in reader:           
                ID = row['id']     
                titulo = row['title']
                fecha = row['release_date']
                retorno = float(row['revenue'])
                duracion_minutos = int(row['runtime'])
                presupuesto = float(row['budget'])
                sitio_web = row['homepage']
                idioma_original = row['original_language']
                Poster_Link = row['Poster_Link']
                IMDB_Rating = (row['IMDB_Rating'])
                star1 = str(row['Star1'])
                star2 = str(row['Star2'])
                star3 = str(row['Star3'])
                star4 = str(row['Star4'])
                lista_famosos = [star1, star2, star3, star4]
                genres_list = [Genero(genero.strip("[]'")) for genero in row.get('genres_list', '').split(', ')]

                # self.lista.append(Pelicula)
                self.lista.append(Pelicula(ID, titulo, fecha, retorno, duracion_minutos, presupuesto, sitio_web, idioma_original, Poster_Link, IMDB_Rating,star1,star2,star3,star4, genres_list))
    
    def __str__(self) -> str:#Conversion a str
        pel_str = [str(Pelicula) for pelicula in self.lista]
        
        return f"Lista de películas:\n" + "\n".join(pel_str)
    
    def filtrar_por_genero(self, genero: Genero) -> List[Pelicula]:
        lista_de_genero: List[Pelicula] = []
        for pelicula in self.lista:
            if genero in pelicula.genres_list:
                lista_de_genero.append(pelicula)
        return lista_de_genero
   
    def filtrar_por_persona(self, persona: Persona) -> List[Pelicula]:
        lista_de_personas: List[Pelicula] = []
        for pelicula in self.lista:
            if persona in pelicula.star_list:
                lista_de_personas.append(pelicula)
        return lista_de_personas

    def filtrar_companieros(self, persona1: Persona, persona2: Persona) -> List[Pelicula]:
        lista_de_companieros: List[Pelicula] = []
        for pelicula in self.lista:
            if persona1 in pelicula.star_list and persona2 in pelicula.star_list:
                lista_de_companieros.append(pelicula)
        
        return lista_de_companieros
    
    def top_n(self, n: int = 50) -> List[Pelicula]:
        lista_ordenada = sorted(self.lista, key = lambda pelicula: pelicula.rating, reverse = True)
        return lista_ordenada[:n]
    def fracasos_comerciales(self, umbral: float = 0.0) -> List[Pelicula]:
        lista_de_fracasos = []    
        
        for pelicula in self.lista:
            if (pelicula.retorno - pelicula.presupuesto) < umbral:
               lista_de_fracasos.append(pelicula)
        return lista_de_fracasos