def mayor_entre_dos():
    print("\nCalcular el numero mayor entre 2 enteros")
    while True:
        try:
            n1 = int(input("Ingrese el primer numero entero: "))
            n2 = int(input("Ingrese el segundo numero entero: "))
            break
        except ValueError:
            print("El numero ingresado no es un entero, vuelva a ingresar")

    if n1 > n2:
        print(f'{n1} es mayor que {n2}')
    elif n1 < n2:
        print(f'{n2} es mayor que {n1}')
    else:
        print("Los numeros son iguales")

def mayor_entre_tres():
    print("\nCalcular el numero mayor entre 3 enteros")
    while True:
        try:
            num1 = int(input("Ingrese el primer numero entero: "))
            num2 = int(input("Ingrese el segundo numero entero: "))
            num3 = int(input("Ingrese el tercer numero entero: "))
            break
        except ValueError:
            print("El numero ingresado no es un entero, vuelva a ingresar")

    if num2 < num1 > num3:
        print(f'{num1} es mayor que {num2} y {num3}')
    elif num1 < num2 > num3:
        print(f'{num2} es mayor que {num1} y {num3}')
    elif num1 < num3 > num2:
        print(f'{num3} es mayor que {num1} y {num2}')
    elif num1 & num2 > num3:
        print(f'{num1} y {num2} son iguales y son mayores que {num3}')
    elif num1 & num3 > num2:
        print(f'{num1} y {num3} son iguales y son mayores que {num2}')
    elif num2 & num3 > num1:
        print(f'{num2} y {num3} son iguales y son mayores que {num1}')
    else:
        print("Los numeros son iguales")

def mayor_entre_n():
    print("\nCalcular el numero mayor entre n enteros")
    while True:
        try:
            n = int(input("Ingrese la cantidad de numeros que va a usar: "))
            break
        except ValueError:
            print("El numero ingresado no es un entero, vuelva a ingresar")

    mayor = 0
    for i in range(n):
        while True:
            try:
                num = int(input(f'Ingrese el numero {i+1}/{n}: '))
                if mayor < num:
                    mayor = num
                print(f'El numero mayor es: {mayor}')
                break
            except ValueError:
                print("El numero ingresado no es un entero, vuelva a ingresar")
          

mayor_entre_dos()
mayor_entre_tres()
mayor_entre_n()