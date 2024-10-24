# Programe la función min_max(data) que tome una secuencia de uno o más números y retorne el menor y 
# el mayor de ellos en una tupla de dos posiciones de longitud
def min_max(data):
    may, men = data[0], data[0] 

    for i in data:
        if i > may:
           may = i
        if i < men:
            men = i
    
    return(may, men)

sec = [80, 65, 15, 24]
result = min_max(sec)
print(result)