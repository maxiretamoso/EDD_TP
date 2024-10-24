# Escriba una función Python que tome como argumento una secuencia de números enteros y determine:
def secuencia(num):
    # a) La sumatoria
    suma = sum(num)
    # b) El promedio
    prom = suma / len(num) 
    # c) Si todos los números son diferentes entre sí, es decir, si todos los números de la lista son distintos
    dif = len(num) == len(set(num))
    
    return suma, prom, dif

num = [2, 50, 35,]
suma, prom, dif = secuencia(num)

print("La sumatoria es:", suma)
print("El promedio es:", prom)
print("Todos los números son diferentes entre si:", dif)

suma, prom, dif = secuencia(num)