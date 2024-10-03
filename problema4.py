alumnos = []
n = int(input("¿Cuántos alumnos desea ingresar?: ")) #int=entero


for i in range(n): #i empieza de 0
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = int(input(f"Ingrese la nota {j+1} de {nombre}: ")) #int=entero
        notas.append(nota)
    
    alumno = {
        'Nombre del Alumno': nombre,
        'Notas obtenidas': notas
    }
    
    alumnos.append(alumno)

print("\nListado de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")