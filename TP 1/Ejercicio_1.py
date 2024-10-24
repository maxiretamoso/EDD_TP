# Solicite al usuario el ingreso de un número entero entre 1 y 20
def tablas_de_multiplicar():
    numero = int(input("Ingrese un número entero entre 1 y 20:"))

    if 1 <= numero <= 20:
        print("tabla de multiplicacion del 1 al 10 de", numero)
        # Muestre por pantalla las tablas de multiplicación del 1 al 10 
        for i in range(1, 11):
            tabla = numero * i
            print(numero, "*", i, "=", tabla)   
    else:
        print("Ingreso invalido. No es un entero entre 1 y 20")  

tablas_de_multiplicar() 