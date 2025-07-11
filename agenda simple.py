contactos = []

def agregar_contacto(nombre, telefono):
    """Agrega un nuevo contacto a la agenda"""
    contactos.append({"nombre": nombre, "telefono": telefono})
    print(f"Contacto {nombre} agregado.")

def mostrar_contactos():
    """Muestra todos los contactos"""
    if not contactos:
        print("No hay contactos en la agenda.")
    else:
        print("\nLista de contactos:")
        for i, contacto in enumerate(contactos, 1):
            print(f"{i}. {contacto['nombre']}: {contacto['telefono']}")

def buscar_contacto(nombre):
    """Busca un contacto por nombre"""
    encontrados = [c for c in contactos if nombre.lower() in c['nombre'].lower()]
    
    if not encontrados:
        print("No se encontraron contactos.")
    else:
        print("\nContactos encontrados:")
        for contacto in encontrados:
            print(f"{contacto['nombre']}: {contacto['telefono']}")

# Menú principal
while True:
    print("\nAgenda Simple")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Salir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion == '1':
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono del contacto: ")
        agregar_contacto(nombre, telefono)
    elif opcion == '2':
        mostrar_contactos()
    elif opcion == '3':
        nombre = input("Nombre a buscar: ")
        buscar_contacto(nombre)
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Intente de nuevo.")