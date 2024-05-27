numero = int(input("Ingrese un número (1 a 10): "))

# Verifica que el número esté en el rango adecuado
if 1 <= numero <= 10:
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
else:
    print("Número fuera de rango. Debe ser entre 1 y 10.")