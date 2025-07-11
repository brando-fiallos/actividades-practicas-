# Programa para añadir nombres a un archivo de texto
ARCHIVO = "nombres.txt"

def añadir_nombre():
    """Función para añadir nombres al archivo"""
    print("\n" + "="*40)
    print(" AÑADIR NOMBRES ".center(40, "~"))
    print("="*40)
    
    while True:
        nombre = input("\nIngresa un nombre (o 'salir' para terminar): ").strip()
        
        # Validar entrada
        if nombre.lower() == 'salir':
            break
            
        if not nombre.isalpha():
            print("⚠️ Error: Solo se permiten letras. Intenta nuevamente.")
            continue
            
        nombre = nombre.title()  # Formato: Primera letra mayúscula
        
        # Escribir en el archivo
        try:
            with open(ARCHIVO, "a") as archivo:
                archivo.write(nombre + "\n")
            print(f"✅ '{nombre}' añadido correctamente.")
        except Exception as e:
            print(f"❌ Error al escribir: {str(e)}")
    
    # Mostrar contenido actualizado
    print("\nContenido actual del archivo:")
    try:
        with open(ARCHIVO, "r") as archivo:
            print(archivo.read())
    except FileNotFoundError:
        print("(El archivo está vacío)")

# Ejecutar el programa
if __name__ == "__main__":
    # Crear archivo si no existe
    open(ARCHIVO, "a").close()
    
    añadir_nombre()
    
    print("\nPrograma terminado. Revisa el archivo 'nombres.txt'")