# Crear un simple juego de adivinanza donde la computadora elige un número al azar y el usuario debe adivinarlo. 
# Practicarás el uso de funciones, bucles, bifurcaciones y el manejo de variables globales y locales.

import random

# Variables globales
intentos_max = 5
numero_secreto = random.randint(1, 100)

# Función para pedir una adivinanza
def pedir_adivinanza():
    try:
        return int(input("Adivina el número (entre 1 y 100): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return pedir_adivinanza()

# Función principal del juego
def juego_adivinanza():
    intentos = 0
    while intentos < intentos_max:  # Bucle while
        adivinanza = pedir_adivinanza()
        intentos += 1
        
        if adivinanza < numero_secreto:  # Bifurcación doble
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
    else:
        print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")

# Función principal para iniciar el juego
def main():
    juego_adivinanza()

# Llamamos a la función principal
main()