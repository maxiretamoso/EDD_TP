from tramites_admin import TramitesAdmin
from tramite import Tramite

def main():
    admin = TramitesAdmin()
    admin.load()  # Cargar trámites desde la base de datos

    while True:
        print("\nOpciones:")
        print("1. Agregar trámite")
        print("2. Quitar trámite")
        print("3. Listar trámites")
        print("4. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            numero = int(input("Número del trámite: "))
            apellido = input("Apellido del solicitante: ")
            nombre = input("Nombre del solicitante: ")
            requerimiento = input("Descripción del requerimiento: ")
            admin.add(Tramite(numero, apellido, nombre, requerimiento))
            print("Trámite agregado exitosamente.")
        elif choice == '2':
            try:
                removed = admin.remove()
                print(f"Trámite removido: {removed}")
            except IndexError as e:
                print(e)
        elif choice == '3':
            print("Lista de trámites:")
            for tramite in admin.list():
                print(tramite)
        elif choice == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "_main_":
    main()