# Modificar nombres en archivo
archivo = "nombres.txt"

# Mostrar contenido actual
print("\nNombres actuales:")
with open(archivo, "r") as f:
    print(f.read())

# Pedir datos para modificar
viejo_nombre = input("\nNombre a modificar: ").strip().title()
nuevo_nombre = input("Nuevo nombre: ").strip().title()

# Realizar el cambio
with open(archivo, "r") as f:
    lineas = f.readlines()

with open(archivo, "w") as f:
    for linea in lineas:
        if linea.strip() == viejo_nombre:
            f.write(nuevo_nombre + "\n")
            print(f"\n✔ Se cambió: {viejo_nombre} → {nuevo_nombre}")
        else:
            f.write(linea)