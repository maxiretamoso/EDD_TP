def continente():
    tot_hab, tot_sup = 0, 0
    paises = []

    while True:
        try:
            can_paises = int(input("\nIngrese la cantidad de países: "))
            break
        except ValueError:
            print("\nLa cantidad de paises debe ser un numero entero, vuelva a intentarlo")
    
    for i in range(can_paises):
        while True:
            pais = input(f'Ingrese el nombre del pais {i+1}/{can_paises}: ')
            if pais.isalpha():
                break
            else:
                print("El nombre del pais solo deben ser letras, vuelva a ingresar")
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
    print(f'\nLa superficie total es: {round(tot_sup,2)}')
    print(f'\nEl promedio de habitantes es: {round(prom_hab,2)}')
    for pais in paises:
        print(f'\nLa densidad poblacional de {pais["pais"]} es: {round(densidad,2)}')


continente()