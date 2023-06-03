import json as js


class Bebida:
    def __init__(self, id, nombre, clasificacion, marca, precio):
        self.id = id
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.marca = marca
        self.precio = precio


def almacenar():
    try:
        with open("productos.json", "r") as archivo:
            datos = js.load(archivo)
            lista = []

            for producto in datos:
                bebida = Bebida(
                    producto["id"],
                    producto["nombre"],
                    producto["clasificacion"],
                    producto["marca"],
                    producto["precio"]
                )
                lista.append(bebida)

            return lista

    except FileNotFoundError:
        return []

def guardar(lista):
    datos = []

    for producto in lista:
        datos.append({
            "id": producto.id,
            "nombre": producto.nombre,
            "clasificacion": producto.clasificacion,
            "marca": producto.marca,
            "precio": producto.precio
        })

    with open("productos.json", "w") as archivo:
        js.dump(datos, archivo)

def alta():
    id = input("Ingrese el ID del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    clasificacion = input("Ingrese la clasificación del producto: ")
    marca = input("Ingrese la marca del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    nueva_bebida = Bebida(id, nombre, clasificacion, marca, precio)
    lista.append(nueva_bebida)

    print("Nuevo producto ingresado con éxito.")

def baja():
    id_baja = input("Ingrese el ID del producto a dar de baja: ")
    eliminado = False

    for producto in lista:
        if producto.id == id_baja:
            lista.remove(producto)
            eliminado = True
            break

    if eliminado:
        print("Producto eliminado con éxito.")
    else:
        print("No se encontró un producto con ese ID.")

def actualizar():
    id_actualizar = input("Ingrese el ID del producto a actualizar: ")
    encontrado = False

    for producto in lista:
        if producto.id == id_actualizar:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_clasificacion = input("Ingrese la nueva clasificación del producto: ")
            nuevo_marca = input("Ingrese la nueva marca del producto: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))

            producto.nombre = nuevo_nombre
            producto.clasificacion = nuevo_clasificacion
            producto.marca = nuevo_marca
            producto.precio = nuevo_precio

            encontrado = True
            print("Producto actualizado con éxito.")
            break

    if not encontrado:
        print("No se encontró un producto con ese ID.")

def mostrar():
    print("Productos en el almacén")
    for producto in lista:
        print(f"ID: {producto.id}, Nombre: {producto.nombre}, Clasificación: {producto.clasificacion}, Marca: {producto.marca}, Precio: {producto.precio}")
    print("")

def promedio():
    if len(lista) == 0:
        print("No hay productos en el almacén.")
    else:
        total_precios = sum(producto.precio for producto in lista)
        precio_promedio = total_precios / len(lista)
        print(f"El precio promedio de los productos es: {precio_promedio}")

def bebidas_marca():
    marca = input("Ingrese la marca de las bebidas a contar: ")
    cantidad = sum(1 for producto in lista if producto.marca.lower() == marca.lower())
    print(f"La cantidad de bebidas de la marca {marca} es: {cantidad}")

def bebidas_clasificacion():
    clasificacion = input("Ingrese la clasificación de las bebidas a contar: ")
    cantidad = sum(1 for producto in lista if producto.clasificacion.lower() == clasificacion.lower())
    print(f"La cantidad de bebidas de la clasificación {clasificacion} es: {cantidad}")

def menu():
    while True:
        print("Menú de operaciones")
        print("1. Dar de alta un producto")
        print("2. Dar de baja un producto")
        print("3. Actualizar un producto")
        print("4. Mostrar todos los productos")
        print("5. Calcular precio promedio de los productos")
        print("6. Contar bebidas de una marca")
        print("7. Contar bebidas por clasificación")
        print("8. Salir")

        eleccion = input("Ingrese la opción que desea realizar: ")

        if eleccion == "1":
            alta()
            guardar(lista)
        elif eleccion == "2":
            baja()
            guardar(lista)
        elif eleccion == "3":
            actualizar()
            guardar(lista)
        elif eleccion == "4":
            mostrar()
        elif eleccion == "5":
            promedio()
        elif eleccion == "6":
            bebidas_marca()
        elif eleccion == "7":
            bebidas_clasificacion()
        elif eleccion == "8":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

lista = almacenar()

menu()
