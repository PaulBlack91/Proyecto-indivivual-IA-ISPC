# EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada materia y quiere saber cuál es su promedio.


# Creamos un diccionario vacío para las notas

notas = {}

# Pedimos al usuario que ingrese las notas de las 5 materias
for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Ingrese la nota de la Materia {i}: "))
            if 0 <= nota <= 10:
                notas[f"Materia {i}"] = nota
                break
            else:
                print("La nota debe estar entre 0 y 10. Por favor, intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

# Calcular el promedio
promedio = sum(notas.values()) / len(notas)

# Mostrar el promedio
print(f"El promedio de las notas es: {promedio:.2f}")