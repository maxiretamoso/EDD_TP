# Programe la función es_multiplo(n, m) que tome dos valores enteros como argumento y 
# retorne True si n es múltiplo de m, esto es, si n = m * i para algún entero i, y False en caso contrario
def es_multiplo(n, m):
    i = n//m           # // operador de division entera (Divide entre dos numeros y redondea el resultado)
    if n == m * i:
        return True
    else: 
        return False
    
# Demuestre el correcto funcionamiento de la función es_multiplo invocándola a través de una aplicación 
# de consola donde el usuario pueda ingresar datos y visualizar los resultados
n = int(input("Ingresar valor de n:"))
m = int(input("Ingresar valor de m:"))

if es_multiplo(n, m):
    print(n, "Es multiplo de", m)
else:
    print(n, "No es multiplo de", m)