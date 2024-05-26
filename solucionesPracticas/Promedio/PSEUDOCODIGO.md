    Algoritmo CalcularPromedioNotas
    Definir notas Como Real[5]
    Definir nota, promedio, suma Como Real
    Definir i Como Entero

      suma <- 0

    Para i <- 1 Hasta 5 Hacer
        Repetir
            Escribir "Ingrese la nota de la Materia ", i, ": "
            Leer nota

            Si nota >= 0 Y nota <= 100 Entonces
                notas[i] <- nota
                suma <- suma + nota
                Salir
            Sino
                Escribir "La nota debe estar entre 0 y 100. Por favor, intente nuevamente."
            FinSi
        Hasta Que nota >= 0 Y nota <= 100
    FinPara

    promedio <- suma / 5

    Escribir "El promedio de las notas es: ", promedio

    FinAlgoritmo