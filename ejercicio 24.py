
archivo_nombres = "nombres.txt"

def buscar_nombre():
    nombre_buscado = input("Ingresa el nombre a buscar: ").strip().title()
    
    try:
        with open(archivo_nombres, "r") as archivo:
            nombres = archivo.readlines()
            encontrado = False
            
            for linea in nombres:
                if nombre_buscado == linea.strip():
                    encontrado = True
                    break
            
            if encontrado:
                print(f"\n✅ ¡{nombre_buscado} está en la lista!")
            else:
                print(f"\n❌ {nombre_buscado} no se encontró en el archivo.")
    
    except FileNotFoundError:
        print("\n⚠️ Error: El archivo 'nombres.txt' no existe. Crea el archivo primero.")

# Llamar a la función
print("=== BUSCADOR DE NOMBRES ===")
buscar_nombre()