numeros = []
pares = 0
impares = 0

while True:
    print("¿Desea ingresar un número?")
    
    opcion = input()
    if opcion == 'SI':
        numero=int(input("Ingrese el número: ")) #INT=ENTERO
        numeros.append(numero)  #append=generar la lista
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    elif opcion =='NO':
        break

print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
