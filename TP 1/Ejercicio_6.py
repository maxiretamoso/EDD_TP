#Escriba un programa Python que solicite al usuario el nombre de cada país del continente, su nombre, superficie y cantidad de habitantes
def componentes_paises():
    tot_hab, tot_sup = 0, 0 # Inicializo en 0 los acumuladores del total de habitantes y superficie
    paises = []
    
    can_paises = int(input("Ingrese la cantidad de países: "))
    
    # Se solicita el nombre de cada país, su superficie y cantidad de habitantes:
    for i in range(can_paises):
        pais = input(f"Ingrese el nombre del país:")
        sup = float(input(f"Ingrese la superficie de {pais}:"))
        hab = int(input(f"Ingrese la cantidad de habitantes de {pais}:"))
        
        paises.append({"pais": pais, "superficie": sup, "habitantes": hab})
        
    # Calcular el total de habitantes, total de superficie, y la densidad:
    for pais in paises:
        tot_hab += pais["habitantes"]
        tot_sup += pais["superficie"]
        pais["densidad"] = pais["habitantes"] / pais["superficie"]

    # promedio de habitantes:
    prom_hab = tot_hab / can_paises

    print("El total de habitantes es:", tot_hab)
    print("La superficie total es:", tot_sup)
    print("El promedio de habitantes es:", prom_hab)
    for pais in paises:
        print(f"La densidad poblacional de {pais["pais"]} es: {pais["densidad"]}")
        
componentes_paises()