def factorial(n):
    if n < 0:
        return "El número debe ser no negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i #* porque no se sabe cuantos datos se tendra
        return resultado
numero = int(input("Ingrese un número entero no negativo: "))
print(f"El factorial de {numero} es: {factorial(numero)}")
