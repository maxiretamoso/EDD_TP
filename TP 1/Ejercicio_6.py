def componentes_paises():
    tot_hab, tot_sup = 0, 0
    paises = []

    while True:
        try:
            can_paises = int(input("\nIngrese la cantidad de países: "))
            break
        except ValueError:
            print("\nLa cantidad de paises debe ser un numero entero, vuelva a intentarlo")
    
    for i in range(can_paises):
        pais = input(f'Ingrese el nombre del pais {i+1}/{can_paises}: ')
        while True:
            try:
                sup = float(input(f'Ingrese la superficie de {pais}: '))
                break
            except ValueError:
                print("\nLa superficie debe ser un numero, vuelva a ingresar")
        while True:
            try:
                hab = int(input(f'Ingrese la cantidad de habitantes de {pais}: '))
                break
            except ValueError:
                print("\nLa cantidad de habitantes debe ser un numero entero, vuelva a ingresar")
        paises.append({"pais": pais, "superficie": sup, "habitantes": hab})

    for pais in paises:
        tot_hab += pais["habitantes"]
        tot_sup += pais["superficie"]
        densidad = pais["habitantes"] / pais["superficie"]
    prom_hab = tot_hab / can_paises

    for pais in paises:
        print(f'\n{pais}')
    print(f'\nEl total de habitantes es: {tot_hab}')
    print(f'\nLa superficie total es: {tot_sup}')
    print(f'\nEl promedio de habitantes es: {prom_hab}')
    for pais in paises:
        print(f'\nLa densidad poblacional de {pais["pais"]} es: {densidad}')

        
componentes_paises()