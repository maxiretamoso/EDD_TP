def secuencia(num):
    suma = sum(num)
    prom = suma / len(num)
    dif = len(num) == len(set(num))
    
    print(f'\nSecuencia de numeros: {num}')
    print(f'La sumatoria es: {suma}')
    print(f'El promedio es: {prom}')
    print(f'¿Los numeros son diferentes? {dif}')


num = (5,6,4)
secuencia(num)