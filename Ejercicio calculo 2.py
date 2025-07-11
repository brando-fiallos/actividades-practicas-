import random

def generar_numero_secreto():
    """Genera un número aleatorio entre 1 y 10"""
    return random.randint(1, 10)

def adivinar_numero():
    secreto = generar_numero_secreto()
    intentos = 3
    
    print("Adivina el número secreto (1-10). Tienes 3 intentos.")
    
    while intentos > 0:
        try:
            guess = int(input("Tu intento: "))
            
            if guess == secreto:
                print("¡Correcto! Has adivinado.")
                return
            elif guess < secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
                
            intentos -= 1
            print(f"Te quedan {intentos} intentos.")
            
        except ValueError:
            print("Por favor ingresa un número válido.")
    
    print(f"¡Agotaste tus intentos! El número era {secreto}.")

# Iniciar juego
adivinar_numero()