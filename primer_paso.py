# Lista para guardar los nombres de tus ideas de proyectos
proyectos = []

print("--- BIENVENIDO AL GESTOR DE IDEAS ---")

while True:
    print("\nOpciones:")
    print("1. Agregar una idea de proyecto")
    print("2. Ver mis proyectos guardados")
    print("3. Salir")
    
    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        nombre = input("¿Cómo se llama tu idea?: ")
        proyectos.append(nombre)
        print(f"¡excelente idea! '{nombre}' registrada con éxito.")
    
    elif opcion == "2":
        print("\n--- TUS PROYECTOS ACTUALES ---")
        if not proyectos:
            print("Aún no tienes proyectos guardados.")
        for i, p in enumerate(proyectos, 1):
            print(f"{i}. {p}")
            
    elif opcion == "3":
        print("¡Sigue programando! Adiós.")
        break
    
    else:
        print("Opción no válida, intenta de nuevo.")


