def no_vocales(texto):
    vocales = "aeiou"
    resultado = ""
    for letra in texto:
        if letra not in vocales:
            resultado += letra
    return resultado

cadena = input("Ingrese el texto: ")

print("Texto sin vocales:", no_vocales(cadena))
