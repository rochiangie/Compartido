def saludar_persona():
    nombre = input("Por favor, ingresa tu nombre: ")
    
    if nombre.lower() == "juan":
        print("¡Hola Juan! ¡Qué bueno verte!")
    else:
        print(f"¿{nombre.capitalize()}? Bueno, hola, supongo...")

saludar_persona()
