# 1. Crear una función que imprima un mensaje
def saludo():
    print("¡Hola, mundo!")

# 2. Función con un argumento
def saludar(nombre):
    print(f"Hola, {nombre}")

# 3. Suma de dos números
def sumar(a, b):
    return a + b

# 4. Calcular el salario
def computepay(horas, tarifa):
    if horas > 40:
        extra = (horas - 40) * (tarifa * 1.5)
        return (40 * tarifa) + extra
    else:
        return horas * tarifa

# 5. Función para determinar el mayor carácter
def mayor_caracter(cadena):
    return max(cadena)

# 6. Conversión de tipo
def convertir_a_flotante(valor):
    try:
        return float(valor)
    except ValueError:
        return None

# 7. Función que retorna un saludo en diferentes idiomas
def saludo_idioma(lang):
    idiomas = {"es": "Hola", "fr": "Bonjour", "en": "Hello"}
    return idiomas.get(lang, "Hello")

# 8. Comprobar si un número es par
def es_par(numero):
    return numero % 2 == 0

# 9. Concatenar cadenas
def concatenar(cad1, cad2):
    return cad1 + cad2

# 10. Calcular promedio
def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

# 11. Contar vocales
def contar_vocales(cadena):
    return sum(1 for letra in cadena if letra.lower() in "aeiou")

# 12. Revertir cadena
def invertir(cadena):
    return cadena[::-1]

# 13. Tabla de multiplicar
def tabla(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 14. Función sin parámetros
def mensaje():
    print("Primera línea")
    print("Segunda línea")
    print("Tercera línea")

# 15. Función que retorne el número más pequeño
def menor_valor(lista):
    return min(lista)

# 16. Calcular factorial
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# 17. Determinar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# 18. Repetir una cadena n veces
def repetir(cadena, n):
    return cadena * n

# 19. Función con múltiples parámetros
def descripcion(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# 20. Verificar palíndromo
def es_palindromo(cadena):
    return cadena.lower() == cadena.lower()[::-1]