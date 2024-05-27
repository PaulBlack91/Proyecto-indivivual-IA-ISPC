cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

#suma de notas
suma_notas = 0

# Pedir las notas de cada estudiante
for i in range(cantidad_estudiantes):
    while True:
        nota = float(input(f"Ingrese la nota del estudiante {i + 1} (0 a 10): "))
        if 0 <= nota <= 10:
            suma_notas += nota
            break
        else:
            print("Nota inválida. Debe estar entre 0 y 10.")

# Calcular el promedio
promedio = suma_notas / cantidad_estudiantes

# Determinar el rendimiento
if promedio > 8:
    rendimiento = "elevado"
elif 6 <= promedio <= 8:
    rendimiento = "aceptable"
else:
    rendimiento = "bajo"

# Mostrar el promedio y el rendimiento
print(f"El promedio de notas es: {promedio:.2f}")
print(f"El rendimiento del curso es: {rendimiento}")