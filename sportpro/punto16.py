# Pedir al usuario que ingrese un año
año = int(input("Ingresa un año: "))

# Verificar si es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")

