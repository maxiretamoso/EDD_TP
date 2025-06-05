def es_multiplo(n,m):
    i = 0
    while i < n:
        i += m
        
    if i == n:
        return True
    else:
        return False

while True:
    try:
        n = int(input("Ingrese el primer numero entero: "))
        m = int(input("Ingrese el segundo numero entero: "))
        break
    except ValueError:
        print("No ha ingresado un numero entero, vuelva a ingresar")    
    
if es_multiplo(n,m):
    print(f'{n} es multiplo de {m}')
else:
    print(f'{n} no es multiplo de {m}')