# Modifica el programa para que, además de calcular el promedio, 
# muestre cuántas notas fueron excluidas por estar por debajo del umbral.

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
    notas_excluidas = []
    for nota in notas:
        if nota >= umbral:
            notas_filtradas.append(nota)
        else:
            notas_excluidas.append(nota)
    return notas_filtradas, len(notas_excluidas)

# Función para calcular el promedio
def calcular_promedio(notas):
    if len(notas) == 0:  # Bifurcación doble
        return 0
    suma = sum(notas)  # Uso de la función sum() para simplificar
    promedio = suma / len(notas)
    return promedio

# Función principal
def main():
    global umbral
    notas = pedir_notas()
    notas_filtradas, cantidad_excluidas = filtrar_notas(notas)
    promedio = calcular_promedio(notas_filtradas)
    print(f"Notas introducidas: {notas}")
    print(f"Notas que están por encima del umbral ({umbral}): {notas_filtradas}")
    print(f"El promedio de las notas que están por encima del umbral ({umbral}) es: {promedio:.2f}")
    print(f"Cantidad de notas excluidas por estar por debajo del umbral: {cantidad_excluidas}")

# Llamamos a la función principal
main()