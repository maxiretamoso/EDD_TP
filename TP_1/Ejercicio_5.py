def min_max(sec):
    if not sec:  
        print("\nLa secuencia esta vacia")
        while True:
            try:
                n = int(input("¿Cuantos numeros va a utilizar para armar la secuencia? "))
                break
            except ValueError:
                print("No ha ingresado un numero entero, vuelva a ingresar")
        
        for i in range(n):
            while True: 
                try:
                    numeros = int(input(f'Ingrese el numero {i+1}/{n}: '))
                    sec.append(numeros)
                    break
                except ValueError:
                    print("No ha ingresado un numero entero, vuelva a ingresar")

    print(f'\nSecuencia: {sec}')
    may, men = sec[0], sec[0]

    for i in sec:
        if i > may:
           may = i
        if i < men:
            men = i
    return(may, men)
    
sec = [32,10,5,16,50]
print(f'El mayor y menor valor de la secuencia es: {min_max(sec)}')