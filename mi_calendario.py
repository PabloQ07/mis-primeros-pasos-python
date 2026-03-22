# Un diccionario para guardar: { "Fecha": "Evento" }
calendario = {}

print("--- MI AGENDA DE PROGRAMADOR ---")

while True:
    print("\n1. Agregar recordatorio")
    print("2. Ver mi agenda")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        fecha = input("Introduce la fecha (ej. 25/03): ")
        evento = input("¿Qué tienes que hacer?: ")
        # Guardamos en el diccionario
        calendario[fecha] = evento
        print(f"¡Guardado! El {fecha} tienes: {evento}")

    elif opcion == "2":
        print("\n--- EVENTOS PROGRAMADOS ---")
        if not calendario:
            print("Tu agenda está vacía.")
        else:
            # Recorremos el diccionario para mostrar fecha y evento
            for fecha, evento in calendario.items():
                print(f"📅 {fecha}: {evento}")

    elif opcion == "3":
        print("¡No olvides tus tareas! Adiós.")
        break
    else:
        print("Opción no válida.")