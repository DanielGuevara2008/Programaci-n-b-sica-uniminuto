#ALGORITMO
#Iniciar el programa.
#Solicitar al usuario su nombre.
#Solicitar su peso en kilogramos.
#Solicitar su altura en metros.
#Calcular el IMC usando la fórmla:
#IMC = peso / (altura × altura).
#Mostrar el nombre, peso, altura y IMC calculado.
#Comparar si el IMC está entre 18.5 y 24.9.
#Mostrar el resultado (True o False).
#Finalizar el programa.
#PSEUDOCODIGO
#Inicio
#Definir nombre Como Cadena
#Definir peso Como Real
#Definir altura Como Real
#Definir imc Como Real
#Escribir "Ingrese su nombre:"
#Leer nombre
#Escribir "Ingrese su peso en kg:"
#Leer peso
#Escribir "Ingrese su altura en metros:"
#Leer altura
#imc <- peso / (altura * altura)
#Escribir "Nombre:", nombre
#Escribir "Peso:", peso
#Escribir "Altura:", altura
#Escribir "IMC:", imc
#Escribir "¿El IMC está en rango normal (18.5 - 24.9)? ", imc >= 18.5 Y imc <= 24.9
#Fin

nombre = input("Ingrese su nombre: ")

peso = float(input("Ingrese su peso en kg: "))

altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura * altura)

print("Nombre:", nombre)

print("Peso:", peso)

print("Altura:", altura)

print("IMC:", imc)

print("¿El IMC está en rango normal (18.5 - 24.9)?", imc >= 18.5 and imc <= 24.9)
