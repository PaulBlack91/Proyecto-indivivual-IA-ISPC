EJERCICO 5.1

Algoritmo TablaMultiplicarMientras
    Definir numero, i Como Entero

    Escribir "Ingrese un número (1 a 10): "
    Leer numero

    Si numero >= 1 Y numero <= 10 Entonces
        i <- 1
        Mientras i <= 10 Hacer
            Escribir numero, " x ", i, " = ", numero * i
            i <- i + 1
        FinMientras
    Sino
        Escribir "Número fuera de rango. Debe ser entre 1 y 10."
    FinSi
FinAlgoritmo

EJERCICIO 5.2

Algoritmo TablaMultiplicarPara
    Definir numero, i Como Entero

    Escribir "Ingrese un número (1 a 10): "
    Leer numero

    Si numero >= 1 Y numero <= 10 Entonces
        Para i <- 1 Hasta 10 Hacer
            Escribir numero, " x ", i, " = ", numero * i
        FinPara
    Sino
        Escribir "Número fuera de rango. Debe ser entre 1 y 10."
    FinSi
FinAlgoritmo
