caracter = input("Ingrese un carácter: ").lower()
if len(caracter) == 1 and caracter.isalpha():
    if caracter in "aeiou":
        print("Es una vocal.")
    else:
        print("Es una consonante.")

else:
    print("Debe ingresar solo una letra.")