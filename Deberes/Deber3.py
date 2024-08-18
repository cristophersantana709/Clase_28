# Modifica el juego para que el usuario pueda elegir el rango del 
# número secreto (por ejemplo, entre 1 y 1000) y también cambiar el número máximo de intentos.

import random

# Variables globales (se definirán en función de la entrada del usuario)
intentos_max = 5
rango_min = 1
rango_max = 100

def obtener_rango():
    """Solicita al usuario que ingrese el rango mínimo y máximo para el número secreto."""
    while True:
        try:
            global rango_min, rango_max
            rango_min = int(input("Ingresa el valor mínimo del rango: "))
            rango_max = int(input("Ingresa el valor máximo del rango: "))
            if rango_min < rango_max:
                return
            else:
                print("El valor máximo debe ser mayor que el valor mínimo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa números enteros.")

def obtener_maximo_intentos():
    """Solicita al usuario que ingrese el número máximo de intentos permitidos."""
    global intentos_max
    while True:
        try:
            intentos_max = int(input("Ingresa el número máximo de intentos: "))
            if intentos_max > 0:
                return
            else:
                print("El número máximo de intentos debe ser mayor que 0.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def generar_numero_aleatorio():
    """Genera un número aleatorio dentro del rango especificado."""
    return random.randint(rango_min, rango_max)

def pedir_adivinanza():
    """Solicita al usuario una adivinanza y valida la entrada."""
    while True:
        try:
            adivinanza = int(input(f"Adivina el número (entre {rango_min} y {rango_max}): "))
            if rango_min <= adivinanza <= rango_max:
                return adivinanza
            else:
                print(f"Por favor, ingresa un número dentro del rango {rango_min} - {rango_max}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def juego_adivinanza():
    """Función principal del juego de adivinanza con rango y número máximo de intentos definidos por el usuario."""
    numero_secreto = generar_numero_aleatorio()
    intentos = 0
    print(f"¡Bienvenido al juego de adivinanza! Tienes {intentos_max} intentos para adivinar el número.")
    
    while intentos < intentos_max:
        adivinanza = pedir_adivinanza()
        intentos += 1
        
        if adivinanza < numero_secreto:
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
    else:
        print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")

def main():
    """Función principal para iniciar el juego y solicitar configuraciones iniciales."""
    obtener_rango()
    obtener_maximo_intentos()
    juego_adivinanza()

# Llamamos a la función principal
if __name__ == "__main__":
    main()