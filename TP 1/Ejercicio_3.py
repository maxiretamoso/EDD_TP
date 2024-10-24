# Escriba un programa que exija al usuario el ingreso de:
# a) 2 números enteros y determine el mayor.
def mayor_entre_dos():
    print("Ingrese 2 numeros enteros y se determinara el mayor")
    num1 = int(input("Ingrese el primer numero:"))
    num2 = int(input("Ingrese el segundo numero:"))
    
    if num1 > num2:
        print(num1, "Es mayor que", num2)
    elif num1 < num2:
        print(num2,"Es mayor que", num1)
    else:
        print("Ambos numeros son iguales")
    
# b) 3 números enteros y determine el mayor.
def mayor_entre_tres():
    print("Ingrese 3 numeros enteros y se determinara el mayor")
    n1 = int(input("Ingrese el primer numero:"))
    n2 = int(input("Ingrese el segundo numero:"))
    n3 = int(input("Ingrese el tercer numero:"))
    
    if n1 > n2 and n1 > n3:
        print(n1, "Es mayor que", n2, "y mayor que", n3)
    elif n2 > n1 and n2 > n3:
        print(n2, "Es mayor que", n1, "y mayor que", n3)
    elif n3 > n1 and n3 > n2:
        print(n3, "Es mayor que", n1, "y mayor que", n2)
    else:
        print("No hay un numero mayor")
        
# c) N números enteros y determine el mayor (no usar colecciones)
def mayor_entre_n():
    print("Ingrese N numeros enteros y se determinara el mayor")
    n = int(input("Ingrese la cantidad de numeros:"))
    mayor = 0

    for i in range(n):
        num = int(input(f"Ingrese el numero {i+1}: "))
        if num > mayor:
            mayor = num
            
    print("El numero mayor es:", mayor)
    
mayor_entre_dos()
mayor_entre_tres()
mayor_entre_n()