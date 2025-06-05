def secuencia(num):
    if not num:  
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
                    num.append(numeros)
                    break
                except ValueError:
                    print("No ha ingresado un numero entero, vuelva a ingresar")

    suma = sum(num)
    prom = suma / len(num)
    dif = len(num) == len(set(num))
    
    print(f'\nSecuencia: {num}')
    print(f'La sumatoria es: {suma}')
    print(f'El promedio es: {prom}')
    print(f'¿Todos los numeros son diferentes? {dif}')

num = [1,2,3,4,5]
secuencia(num)