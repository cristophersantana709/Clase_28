# Crear un sistema que permita registrar estudiantes, sus calificaciones y 
# mostrar un informe completo de los estudiantes registrados. T
# rabajarás con funciones, diccionarios, bucles y bifurcaciones.

# Diccionario global para almacenar estudiantes y sus calificaciones
estudiantes = {}

# Función para agregar un estudiante
def agregar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    notas = []
    while True:
        entrada = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            nota = float(entrada)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    estudiantes[nombre] = notas
    print(f"Estudiante {nombre} agregado con éxito!")

# Función para mostrar todos los estudiantes y sus notas
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return
    
    print("Estudiantes registrados:")
    for nombre, notas in estudiantes.items():
        print(f"{nombre}: {notas} (Promedio: {sum(notas)/len(notas) if len(notas) > 0 else 0})")

# Función para calcular el promedio general de todas las notas
def promedio_general():
    total_notas = 0
    total_estudiantes = 0
    for notas in estudiantes.values():
        total_notas += sum(notas)
        total_estudiantes += len(notas)
    
    if total_estudiantes == 0:
        return 0
    
    return total_notas / total_estudiantes

# Función principal
def main():
    while True:
        print("\nMenú del Sistema de Registro")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar promedio general")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            promedio = promedio_general()
            print(f"El promedio general de todas las calificaciones es: {promedio}")
        elif opcion == '4':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Llamamos a la función principal
main()