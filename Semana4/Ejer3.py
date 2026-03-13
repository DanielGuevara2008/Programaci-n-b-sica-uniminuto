#ALGORITMO
#Iniciar el programa.
#Solicitar al usuario la temperatura en grados Celsius.
#Convertir la temperatura a Fahrenheit.
#Convertir la temperatura a Kelvin.
#Mostrar la temperatura en Celsius, Fahrenheit y Kelvin.
#Comparar si la temperatura en Celsius es mayor que 37.
#Mostrar el resultado de la comparación (True o False).
#Finalizar el programa.
#PSEUDOCODIGO
#Inicio
#Definir celsius Como Real
#Definir fahrenheit Como Real
#Definir kelvin Como Real
#Escribir "Ingrese la temperatura en grados Celsius:"
#Leer celsius
#fahrenheit <- (celsius * 9/5) + 32
#kelvin <- celsius + 273.15
#Escribir "Temperatura en Celsius: ", celsius
#Escribir "Temperatura en Fahrenheit: ", fahrenheit
#Escribir "Temperatura en Kelvin: ", kelvin
#Escribir "¿Supera la temperatura de fiebre (37C)?: ", celsius > 37

celsius=float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit=(celsius * 9/5) + 32

kelvin=celsius + 273.15

print("Temperatura en Celsius:", celsius)

print("Temperatura en Fahrenheit:", fahrenheit)

print("Temperatura en Kelvin:", kelvin)

print("¿Supera la temperatura de fiebre (37C)?", celsius > 37)
