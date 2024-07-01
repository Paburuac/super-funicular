cincoKilos = quinceKilos = cuarentaycincoKilos = 0
cantidadCinco = cantidadQuince = cantidadCuarentaCinco = 0
lugares = ["Colina", "Centro", "Industrias"]
clientes = []
diccionario = {}

def menu():
    print("OPCIONES DISPONIBLES")
    print("1. Registrar Pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")

def datosPedido():
    print("Datos del pedido")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    comuna = input("Ingrese su comuna: ")
    try:
        cantidadCinco = int(input("Ingrese la cantidad de cilindros de 5 kg: "))
        cantidadQuince = int(input("Ingrese la cantidad de cilindros de 15 kg: "))
        cantidadCuarentaCinco = int(input("Ingrese la cantidad de cilindros de 45 kg: "))
    except:
        return
    
    if len(nombre) == 0 or len(apellido) == 0 or len(comuna) == 0:
        print("Ingrese un dato válido")
        return
    
    pedido = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Comuna": comuna,
        "Cilindro 5kg": cantidadCinco,
        "Cilindro 15kg": cantidadQuince,
        "Cilindro 45kg": cantidadCuarentaCinco
    }
    clientes.append(pedido)
    diccionario[nombre] = pedido
    print("Pedido registrado:", pedido)

def listar_pedidos():
    print("Lista de pedidos")
    if not clientes:
        print("No hay pedidos hechos")
    else:
        for cliente in clientes:
            print(f"Su nombre es: {cliente['Nombre']}\nSu apellido es: {cliente['Apellido']}\nSu comuna es: {cliente['Comuna']}\nUsted está comprando: {cliente['Cilindro 5kg']} cilindros de 5kg\nUsted está comprando: {cliente['Cilindro 15kg']} cilindros de 15 kg\nUsted está comprando: {cliente['Cilindro 45kg']} cilindros de 45 kg\n")

def hoja_de_ruta():
    print("HOJA DE RUTA")
    print("Sectores válidos para la hoja de ruta: ")
    print("1. Colina")
    print("2. Centro")
    print("3. Industrias")
    opcion = input("Ingrese una zona: ")
    
    zonas = {
        "1": "Colina",
        "2": "Centro",
        "3": "Industrias"
    }
    
    if opcion in zonas:
        zona = zonas[opcion]
        archivo_salida = f"hoja_de_ruta_{zona}.txt"
        with open(archivo_salida, "w") as archivo:
            for cliente in clientes:
                if cliente["Comuna"] == zona:
                    archivo.write(f"Su nombre es: {cliente['Nombre']}\n")
                    archivo.write(f"Su apellido es: {cliente['Apellido']}\n")
                    archivo.write(f"Su comuna es: {cliente['Comuna']}\n")
                    archivo.write(f"Usted esta comprando: {cliente['Cilindro 5kg']} cilindros de 5kg\n")
                    archivo.write(f"Usted esta comprando: {cliente['Cilindro 15kg']} cilindros de 15 kg\n")
                    archivo.write(f"Usted esta comprando: {cliente['Cilindro 45kg']} cilindros de 45 kg\n")
            print(f"Hoja de ruta para {zona} ha sido guardada en {archivo_salida}")

# CODIGO PRINCIPAL
while True:
    menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        datosPedido()
    elif opcion == "2":
        listar_pedidos()
    elif opcion == "3":
        hoja_de_ruta()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
