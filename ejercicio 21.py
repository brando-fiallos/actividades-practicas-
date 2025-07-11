#Ejercicio 1: Conteo Regresivo con while
#•	Escribe un programa que use un bucle while para imprimir números desde el 10 hasta el 1.
contador = 10
while contador > 0:
    print(contador)
    contador -= 1

#•	Después de que el bucle termine, imprime el mensaje "¡Despegue!".
print("¡Despegue!")

#Ejercicio 2: Adivina la Palabra Secreta (while y break)
#•	Escribe un programa que defina una palabra secreta (por ejemplo, puedes usar "python").
#•	Utiliza un bucle while True para solicitar continuamente al usuario que ingrese una palabra.
palabra_secreta = "python"
#•	Si la palabra ingresada por el usuario coincide con la palabra secreta, el programa debe imprimir "¡Has adivinado la palabra!" y luego terminar el bucle usando la sentencia break. 
#•	Si la palabra ingresada no es correcta, el programa debe imprimir "Inténtalo de nuevo." y continuar pidiendo otra palabra.
while True:
    palabra_ingresada = input("Ingresa la palabra secreta: ")
    if palabra_ingresada == palabra_secreta:
        print("¡Adivinaste!")
        break
    else:
        print("Inténtalo de nuevo.")

#Ejercicio 3: Procesador de Entradas con continue
#•	Escribe un programa que pida al usuario que ingrese texto repetidamente usando un bucle while True.
while True:
    entrada = input("Ingresa un texto (o 'listo' para terminar): ")
    
    #•	Si el usuario ingresa el carácter "#", el programa debe ignorar completamente esa entrada (es decir, no hacer nada con ella y no imprimir nada) y pasar a la siguiente iteración para pedir una nueva entrada. Para esto, utiliza la sentencia continue. 
    if entrada == "#":
        continue
    
    #•	Si el usuario ingresa la palabra "listo" (en minúsculas), el programa debe imprimir el mensaje "¡Procesamiento terminado!" y luego finalizar.
    elif entrada == "listo":
        print("¡Procesamiento terminado!")
        break
    
    #•	Para cualquier otra entrada de texto que no sea "#" ni "listo", el programa debe imprimir esa misma entrada pero convertida a mayúsculas.
    else:
        print(entrada.upper())

#Ejercicio 4: Lista de Invitados con for
#•	Define una lista de nombres de amigos. Por ejemplo: invitados = ['Ana', 'Luis', 'Carla', 'Pedro'].
invitados = ['Ana', 'Luis', 'Carla', 'Pedro', 'Marta', 'Javier']
#•	Utiliza un bucle for para iterar sobre cada nombre en la lista invitados.
for amigo in invitados:
    #•	Dentro del bucle, para cada amigo, imprime un saludo personalizado. Por ejemplo, si el nombre es "Ana", debe imprimir "Hola Ana, ¡bienvenida a la fiesta!".
    print(f"Hola {amigo}, ¡bienvenida a la fiesta!")
  
#Ejercicio 5: Encontrando el Número Mayor (for)
#•	Se proporciona la siguiente lista de números: numeros = [3, 41, 12, 9, 74, 15, 1, 55].
numeros = [3, 41, 12, 9, 74, 15, 1, 55]
#•	Escribe un programa que utilice un bucle for para recorrer esta lista y encontrar cuál es el número más grande.
#•	Antes de comenzar el bucle, inicializa una variable, por ejemplo mayor_hasta_ahora, con un valor muy pequeño (o con el primer elemento de la lista, o con -1 como se sugiere en la presentación si se asume que todos los números serán positivos).
#•	Dentro del bucle, compara cada número de la lista con tu variable mayor_hasta_ahora. Si el número actual es mayor, actualiza mayor_hasta_ahora con este número. 
#•	Al finalizar el bucle, imprime el valor de mayor_hasta_ahora, que será el número más grande encontrado.
mayor_hasta_ahora = -1  
for numero in numeros:
    if numero > mayor_hasta_ahora:
        mayor_hasta_ahora = numero
print(f"El número mayor es: {mayor_hasta_ahora}")

#Ejercicio 6: Conteo de Elementos Pares (for y condicional)
#•	Se proporciona la siguiente lista de números: numeros = [2, 5, 8, 11, 14, 17, 20, 23].
numeros = [2, 5, 8, 11, 14, 17, 20, 23]
#•	Escribe un programa que utilice un bucle for para contar cuántos de los números en esta lista son pares.
contador_pares = 0
for numero in numeros:
#•	Inicializa una variable contador a 0 antes del bucle. 
#•	Dentro del bucle, verifica si cada número es par (puedes usar el operador módulo %: un número es par si numero % 2 == 0).
    if numero % 2 == 0:
#•	Si un número es par, incrementa tu variable contador.
        contador_pares += 1
#•	Al finalizar el bucle, imprime el valor total del contador.
print(f"Cantidad de números pares: {contador_pares}")

#Ejercicio 7: Suma de Todos los Números (for)
#•	Se proporciona la siguiente lista de números: numeros = [10, 20, 30, 40, 50].
numeros = [10, 20, 30, 40, 50]
#•	Escribe un programa que utilice un bucle for para calcular la suma de todos los números presentes en la lista.
suma_total = 0
for numero in numeros:
#•	Inicializa una variable, por ejemplo suma_total, a 0 antes de comenzar el bucle. 
#•	Dentro del bucle, acumula la suma de cada número en suma_total. 
    suma_total += numero
#•	Al finalizar el bucle, imprime el valor de suma_total.
print(f"La suma total es: {suma_total}")

#Ejercicio 8: Cálculo del Promedio (for)
#•	Se proporciona la siguiente lista de números: numeros = [10, 15, 20, 25, 30].
numeros = [10, 15, 20, 25, 30]
#•	Escribe un programa que utilice un bucle for para calcular el promedio de los números en esta lista.
suma_total = 0
#•	Para calcular el promedio, necesitarás dos cosas: la suma de todos los números y la cantidad total de números. 
cantidad_numeros = len(numeros) 
for numero in numeros:
#•	Puedes usar una variable para la suma (inicializada en 0) y otra para el conteo (inicializada en 0), actualizándolas en cada iteración del bucle. 
    suma_total += numero
#•	Al finalizar el bucle, calcula el promedio dividiendo la suma total entre la cantidad total de números.
promedio = suma_total / cantidad_numeros
#•	Imprime el promedio calculado.
print(f"El promedio es: {promedio}")

#Ejercicio 9: Filtrando Números Mayores que un Valor (for)
#•	Se proporciona la siguiente lista de números: numeros = [5, 25, 12, 33, 18, 45, 7].
numeros = [5, 25, 12, 33, 18, 45, 7]
#•	Escribe un programa que primero solicite al usuario que ingrese un número umbral (este será el valor con el cual comparar).
umbral = int(input("Ingresa un número umbral: "))
#•	Luego, utiliza un bucle for para iterar sobre la lista numeros.
for numero in numeros:
    #•	Dentro del bucle, si un número de la lista es estrictamente mayor que el número umbral ingresado por el usuario, imprime ese número. 
    if numero > umbral:
        print(numero)
#•	Dentro del bucle, si un número de la lista es estrictamente mayor que el número umbral ingresado por el usuario, imprime ese número.
 
#Ejercicio 10: Búsqueda de un Valor Específico (for y booleano)
#•	Se proporciona la siguiente lista de números: numeros = [9, 41, 12, 3, 74, 15].
numeros = [9, 41, 12, 3, 74, 15]
#•	Escribe un programa que verifique si el número 3 está presente en esta lista.
#•	Utiliza una variable booleana, por ejemplo encontrado, e inicialízala en False antes del bucle. 
encontrado = False
#•	Recorre la lista con un bucle for. Si encuentras el número 3, cambia el valor de la variable encontrado a True. Puedes optar por usar break para salir del bucle una vez encontrado, aunque no es estrictamente necesario para este ejercicio.
for numero in numeros:
    if numero == 3:
        encontrado = True
        break 
#•	Después del bucle, imprime un mensaje que indique si el valor fue encontrado o no, basándote en el estado final de la variable encontrado. Por ejemplo: "El valor 3 fue encontrado: True" o "El valor 3 fue encontrado: False".
if encontrado:
    print("El valor 3 fue encontrado: True")
else:
    print("El valor 3 fue encontrado: False")

#Ejercicio 11: Encontrando el Número Menor (for y None)
#•	Se proporciona la siguiente lista de números: numeros = [30, 10, 5, 25, 50, 2].
numeros = [30, 10, 5, 25, 50, 2]
#•	Escribe un programa que utilice un bucle for para encontrar el número más pequeño en la lista.
#•	Inicializa una variable, por ejemplo menor_hasta_ahora, con el valor especial None antes de comenzar el bucle.
menor_hasta_ahora = None 
#•	Dentro del bucle, en cada iteración: 
#o	Si menor_hasta_ahora es None (lo cual será cierto en la primera iteración), asigna el número actual de la lista a menor_hasta_ahora. 
#o	Si no, compara el número actual de la lista con menor_hasta_ahora. Si el número actual es menor, actualiza menor_hasta_ahora con este número. 
#•	Para verificar si menor_hasta_ahora es None, utiliza el operador is (ej. if menor_hasta_ahora is None:). 
#•	Al finalizar el bucle, imprime el valor de menor_hasta_ahora, que 
#será el número más pequeño encontrado en la lista.
for numero in numeros:
    if menor_hasta_ahora is None:
        menor_hasta_ahora = numero
    elif numero < menor_hasta_ahora:
        menor_hasta_ahora = numero
print(f"El número menor es: {menor_hasta_ahora}")



