#ALGORITMO
#Iniciar el programa.
#Solicitar al usuario el nombre del producto.
#olicitar el precio unitario del producto.
#Solicitar la cantidad de unidades.
#Calcular el subtotal (precio × cantidad).
#Calcular el IVA del 19% sobre el subtotal.
#Calcular el total a pagar (subtotal + IVA).
#Mostrar el nombre del producto, el subtotal, el IVA y el total.
#Comparar si el total es mayor que 50000.
#Mostrar el resultado (True o False).
#Finalizar el programa.
#PSEUDOCODIGO
#Inicio
#Escribir "Ingrese el nombre del producto:"
#Leer producto
#Escribir "Ingrese el precio unitario:"
#Leer precio
#Escribir "Ingrese la cantidad:"
#Leer cantidad
#subtotal <- precio * cantidad
#iva <- subtotal * 0.19
#total <- subtotal + iva
#Escribir "Producto:", producto
#Escribir "Subtotal:", subtotal
#Escribir "IVA (19%):", iva
#Escribir "Total a pagar:", total
#Escribir "¿El total supera $50.000 para descuento especial?: ", total > 50000
#Fin

producto = input("Ingrese el nombre del producto: ")

precio = float(input("Ingrese el precio unitario: "))

cantidad = int(input("Ingrese la cantidad: "))

subtotal = precio * cantidad

iva = subtotal * 0.19

total = subtotal + iva

print("Producto:", producto)

print("Subtotal:", subtotal)

print("IVA (19%):", iva)

print("Total a pagar:", total)

print("¿El total supera $50.000 para descuento especial?", total > 50000)
