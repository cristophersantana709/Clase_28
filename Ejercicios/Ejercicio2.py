# Crear un pequeño sistema de inventario que permita agregar, eliminar y ver productos en una tienda. 
# Practicarás el uso de funciones, bucles for y while, bifurcaciones simples y dobles, y el manejo de un diccionario.

# Diccionario global para almacenar el inventario
inventario = {}

# Función para agregar productos
def agregar_producto():
    producto = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    if producto in inventario:  # Bifurcación doble
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto {producto} agregado con éxito!")

# Función para eliminar productos
def eliminar_producto():
    producto = input("Ingresa el nombre del producto a eliminar: ")
    if producto in inventario:  # Bifurcación simple
        del inventario[producto]
        print(f"Producto {producto} eliminado con éxito!")
    else:
        print(f"El producto {producto} no está en el inventario.")

# Función para mostrar el inventario
def mostrar_inventario():
    if len(inventario) == 0:  # Bifurcación doble
        print("El inventario está vacío.")
    else:
        print("Inventario de productos:")
        for producto, cantidad in inventario.items():  # Bucle for
            print(f"{producto}: {cantidad} unidades")

# Función principal que controla el menú
def main():
    while True:  # Bucle while
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Llamamos a la función principal
main()