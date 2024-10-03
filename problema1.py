numeros_pedidos=[]
for rango in range(1500,2700):
    if rango % 7 == 0 and rango % 5 == 0: 
        numeros_pedidos.append(rango)
print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:",numeros_pedidos)
