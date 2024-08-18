#  Modifica el programa para que permita actualizar 
#  la cantidad de un producto existente sin necesidad de agregar uno nuevo.

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
            
def actualizar_producto():
    producto = input("Ingrese el nombre del producto que desea actualizar: ")
    if producto in inventario:
        cantidad = int(input("Ingresa la nueva cantidad del producto: "))
        inventario[producto] = cantidad
        print(f"Cantidad del producto '{producto}' actualizada a {cantidad} unidades.")
    else:
        print(f"El producto '{producto}' no está en el inventario. Primero agrégalo.")


# Función principal que controla el menú
def main():
    while True:  # Bucle while
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Actualizar producto")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            actualizar_producto()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Llamamos a la función principal
main()