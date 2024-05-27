Algoritmo CalcularPromedioNotas
    Definir cantidad_estudiantes, i Como Entero
    Definir nota, suma_notas, promedio Como Real

    suma_notas <- 0

    Escribir "Ingrese la cantidad de estudiantes: "
    Leer cantidad_estudiantes

    Para i <- 1 Hasta cantidad_estudiantes Hacer
        Repetir
            Escribir "Ingrese la nota del estudiante ", i, " (0 a 10): "
            Leer nota
            Si nota >= 0 Y nota <= 10 Entonces
                suma_notas <- suma_notas + nota
                Salir
            Sino
                Escribir "Nota inválida. Debe estar entre 0 y 10."
            FinSi
        Hasta Que nota >= 0 Y nota <= 10
    FinPara

    promedio <- suma_notas / cantidad_estudiantes

    Si promedio > 8 Entonces
        rendimiento <- "elevado"
    Sino
        Si promedio >= 6 Entonces
            rendimiento <- "aceptable"
        Sino
            rendimiento <- "bajo"
        FinSi
    FinSi

    Escribir "El promedio de notas es: ", promedio
    Escribir "El rendimiento del curso es: ", rendimiento
FinAlgoritmo