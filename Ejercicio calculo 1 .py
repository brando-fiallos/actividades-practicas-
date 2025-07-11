# 1. Función multiplicar
def multiplicar(x, y):
    """Retorna el producto de dos números"""
    return x * y

# Prueba
print(multiplicar(5, 3))  # Debería mostrar 15

# 2. Función es_par
def es_par(numero):
    """Determina si un número es par"""
    return numero % 2 == 0

# Prueba
print(es_par(4))  # Debería mostrar True
print(es_par(5))  # Debería mostrar False

# 3. Función presentarse
def presentarse(nombre, edad):
    """Muestra un mensaje de presentación"""
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# Prueba
presentarse("Ana", 25)  # Debería mostrar: Hola, me llamo Ana y tengo 25 años.