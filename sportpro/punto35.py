saldo = 1000  # Saldo inicial
while True:
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")

    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print(f"Su saldo actual es: ${saldo}")
    elif opcion == "2":
        deposito = float(input("Ingrese la cantidad a depositar: "))
        saldo += deposito
        print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
    elif opcion == "3":
        retiro = float(input("Ingrese la cantidad a retirar: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
    elif opcion == "4":
        print("Gracias por usar el cajero automático.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
