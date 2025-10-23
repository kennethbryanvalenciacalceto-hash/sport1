from datetime import date
fecha_nacimiento = int(input("Ingrese su año de nacimiento: "))
fecha_actual = date.today().year
edad = fecha_actual- fecha_nacimiento
print(f"Su edad es: {edad} años")
