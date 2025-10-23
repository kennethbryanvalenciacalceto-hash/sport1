base = float(input("Sueldo base: "))
extras = float(input("Horas extras: "))
bonos = float(input("Bonos: "))
neto = (base + extras + bonos) * 0.92  # Descuento del 8%
print("Tu salario neto es:", neto)