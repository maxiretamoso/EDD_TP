def tabla_multiplicar():
    while True:
        try:
            
            num = int(input("Ingrese un numero entre 1 y 20: "))

            if 1 <= num <= 20:
                print(f'\nTabla de multiplicar de {num} del 1 al 10:')
                for i in range(1, 11):
                    print(f'{num} * {i} = {num * i}')
                break 
            print("El numero ingresado no está entre 1 y 20. Vuelva a ingresar")
            
        except ValueError:
            print("No ha ingresado un numero entero. Vuelva a ingresar")


tabla_multiplicar()