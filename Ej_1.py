total_compra_desc = 0
total_compra_sin_desc = 0
ahorro = 0

nombre = input("Ingrese su nombre: ")
while (nombre.isalpha() == False) or (nombre == " "):
    print("Error")
    nombre = input("Ingrese su nombre: ")

cant_prod = input("Ingrese la cantidad de productos a comprar: ")
while cant_prod.isdigit() == False or cant_prod <= 0:
    print("Error")
    cant_prod = input("Ingrese la cantidad de productos a comprar: ")

for i in range(int(cant_prod)):
    precio = input("Ingrese precio del articulo: ")
    while precio.isdigit() == False:
        print("Error")
        precio = input("Ingrese precio del articulo: ")

    desc = input("Tiene descuento? (S/N): ")
    while desc.isalpha() == False:
        print("Error")
        desc = input("Tiene descuento? (S/N): ")
    desc = desc.lower()
    total_compra_sin_desc += float(precio)
    if desc == "s":
        descuento = (float(precio) * 0.10)
        precio = float(precio) - descuento
        ahorro += descuento
    total_compra_desc += float(precio)

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cant_prod}")
print(f"Total a pagar sin descuentos: {total_compra_sin_desc}")
print(f"Total a pagar con descuentos: {total_compra_desc}")
print(f"Cantidad de dinero ahorrado: {ahorro}")
print(f"Promedio por producto {(total_compra_sin_desc / float(cant_prod)):.2f}")