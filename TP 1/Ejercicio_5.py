def min_max(data):
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

    may, men = data[0], data[0]

    for i in data:
        if i > may:
           may = i
        if i < men:
            men = i
    
    return(may, men)

sec = [2,4,8,16,32]
print(f'Secuencia: {sec}')
print(f'Mayor y menor valor: {min_max(sec)}')