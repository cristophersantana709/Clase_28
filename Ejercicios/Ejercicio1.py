# Crear una calculadora que pida al usuario una serie de notas y luego calcule el promedio,
# excluyendo aquellas notas que estén por debajo de un cierto umbral.
# Este ejercicio te ayudará a practicar el uso de funciones, bifurcaciones, bucles y tipos de datos estructurados.

# Definimos una variable global para el umbral
umbral = 5.0

# Función para pedir las notas
def pedir_notas():
    notas = []
    while True:
        nota = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return notas

# Función para filtrar notas por el umbral
def filtrar_notas(notas):
    notas_filtradas = []
    for nota in notas:
        if nota >= umbral:  # Bifurcación simple
            notas_filtradas.append(nota)
    return notas_filtradas

# Función para calcular el promedio
def calcular_promedio(notas):
    if len(notas) == 0:  # Bifurcación doble
        return 0
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    return promedio

# Función principal
def main():
    notas = pedir_notas()
    notas_filtradas = filtrar_notas(notas)
    promedio = calcular_promedio(notas_filtradas)
    print(f"El promedio de las notas que están por encima del umbral ({umbral}) es: {promedio}")

# Llamamos a la función principal
main()