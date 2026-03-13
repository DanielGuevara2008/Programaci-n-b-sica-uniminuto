#ALGORITMO
#Iniciar el programa.
#Solicitar al usuario la nota 1.
#Solicitar al usuario la nota 2.
#Solicitar al usuario la nota 3.
#Calcular el promedio de las tres notas.
#Mostrar las tres notas ingresadas.
#Mostrar el promedio obtenido.
#Comparar si el promedio es mayor o igual a 3.0.
#Mostrar el resultado (True o False).
#Finalizar el programa.
#PSEUDOCODIGO
#Inicio
#Definir nota1 Como Real
#Definir nota2 Como Real
#Definir nota3 Como Real
#Definir promedio Como Real
#Escribir "Ingrese la nota 1:"
#Leer nota1
#Escribir "Ingrese la nota 2:"
#Leer nota2
#Escribir "Ingrese la nota 3:"
#Leer nota3
#promedio <- (nota1 + nota2 + nota3) / 3
#Escribir "Nota 1:", nota1
#Escribir "Nota 2:", nota2
#Escribir "Nota 3:", nota3
#Escribir "Promedio:", promedio
#Escribir "¿El estudiante aprobó (nota mínima 3.0)? ", promedio >= 3.0
#Fin

nota1 = float(input("Ingresa la nota 1: "))

nota2 = float(input("Ingresa la nota 2: "))

nota3 = float(input("Ingresa la nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

print("Nota 1:", nota1)

print("Nota 2:", nota2)

print("Nota 3:", nota3)

print("Promedio:", promedio)

print("¿El estudiante aprobó?", promedio >= 3.0)
