numero = int(input("Ingrese un número (1 a 10): "))

# Verifica que el número esté en el rango adecuado
if 1 <= numero <= 10:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número fuera de rango. Debe ser entre 1 y 10.")