def div_propios(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0: #si un numero es divisible entre si mismo se considerara 0
            divisores.append(i) #Agregar a la lista q se generara
    return divisores

def es_perfecto(num):
    return sum(div_propios(num)) == num #si la sum de sus divisores es igual al numero

numeros_perfectos = []
for num in range(1, 1000): #poner rango
    if es_perfecto(num):
        numeros_perfectos.append(num)

print("Números perfectos menores que 1000:", numeros_perfectos)
