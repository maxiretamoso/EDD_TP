from datetime import datetime
from genero import Genero
from typing import List

class Pelicula:
    def __init__(self, ID: int, title: str, release_date: datetime, revenue: float,
                 runtime: int, budget: float, homepage: str, original_language: str, 
                 Poster_Link: str, IMDB_Rating: float,star1:str,star2:str,star3:str,star4:str, 
                 genres_list: List[Genero]):
        self.ID = ID
        self.titulo = title
        self.fecha_publicacion = release_date
        self.retorno = revenue
        self.duracion_minutos = runtime
        self.presupuesto = budget
        self.sitio_web = homepage
        self.idioma_original = original_language
        self.poster = Poster_Link
        self.rating = IMDB_Rating
        self.star_list = [star1, star2, star3, star4]
        self.genres_list = genres_list
    
    def __str__(self):
            return '\n' f"""    
                                Titulo={self.titulo} 
                                Rating={self.rating} 
                                Retorno={self.retorno}
                                Presupuesto={self.presupuesto}
                                Sitio web={self.sitio_web}
                                Idioma original={self.idioma_original} 
                                Poster={self.poster
                                                    }
                                Duracion_minutos={self.duracion_minutos} 
                                Fecha de publicacion={self.fecha_publicacion}
                                Lista de generos={self.genres_list}
                                Lista de estrellas= {self.star_list
                                                            }"""'\n'

    def __eq__(self, otra_pelicula):
     if isinstance(otra_pelicula, Pelicula):
        return self.titulo == otra_pelicula.titulo
     return False

    def __repr__(self):
        return self.__str__()