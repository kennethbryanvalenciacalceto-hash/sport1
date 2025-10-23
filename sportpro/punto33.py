positivos = 0
negativos = 0
while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
