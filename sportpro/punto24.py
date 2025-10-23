precio = float(input("Ingrese el precio del producto: "))
iva = float(input("Ingrese el porcentaje de IVA (%): "))
precio_total = precio + (precio * iva / 100)
print(f"El precio total con IVA es: {precio_total}")