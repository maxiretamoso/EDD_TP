from procesar_superheroes_villanos import ProcesarSuperheroesVillanos

def main():
    processor = ProcesarSuperheroesVillanos('superheroes_villanos.txt')
    processor.process_file()
    processor.print_counts()

if __name__ == "__main__":
    main()