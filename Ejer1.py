#ALGORITMO
#Iniciar el programa.
#Solicitar al usuario su nombre.
#Solicitar al usuario su edad.
#Solicitar al usuario su ciudad de residencia.
#Mostrar un mensaje de presentación con los datos ingresados.
#Comparar si la edad es mayor o igual a 18.
#Mostrar el resultado de la comparación (True o False).
#Finalizar el programa.
#PSEUDOCOGIDO
#Escribir "Ingrese su nombre:"
#Leer nombre
#Escribir "Ingrese su edad:"
#Leer edad
#Escribir "Ingrese su ciudad de residencia:"
#Leer ciudad
#Escribir "Hola, mi nombre es ", nombre, ", tengo ", edad, " años y vivo en ", ciudad
#esaMyorEdad <- edad >= 18
#Escribir esMayorEdad
#Fin

nombre =input("Ingresa tu nombre:")

edad = int(input("Ingresa tu edad: "))

ciudad = input("Ingresa tu Ciudad: ")

print("tu nombre es", nombre)

print("tu edad es", edad)

print("tu ciudad es", ciudad)

print("¿Es mayor de edad?", edad >18)