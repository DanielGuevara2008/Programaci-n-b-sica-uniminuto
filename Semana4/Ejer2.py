#ALGORITMO
#Iniciar el programa.
#Solicitar al usuario el primer número entero.
#Solicitar al usuario el segundo número entero.
#Calcular la suma de los dos números.
#Calcular la resta del primer número menos el segundo.
#Calcular la multiplicación de los dos números.
#Calcular la división del primer número entre el segundo.
#Calcular la división entera del primer número entre el segundo.
#Calcular el residuo de la división.
#Calcular la potencia del primer número elevado al segundo.
#Mostrar cada resultado con un mensaje descriptivo.
#Comparar si la suma de los dos números es mayor que 100.
#Mostrar el resultado de la comparación (True o False).
#Finalizar el programa.
#PSEUDOCODIGO
#Inicio
#Definir num1
#Definir num2 
#Definir suma 
#Definir resta 
#Definir multiplicacion 
#Definir division 
#Definir divisionEntera 
#Definir residuo 
#Definir potencia 
#Escribir "Ingrese el primer numero:"
#Leer num1
#Escribir "Ingrese el segundo numero:"
#Leer num2
#suma <- num1 + num2
#resta <- num1 - num2
#multiplicacion <- num1 * num2
#division <- num1 / num2
#divisionEntera <- num1 // num2
#residuo <- num1 % num2
#potencia <- num1 ** num2
#Escribir "La suma es: ", suma
#Escribir "La resta es: ", resta
#Escribir "La multiplicacion es: ", multiplicacion
#Escribir "La division es: ", division
#Escribir "La division entera es: ", divisionEntera
#Escribir "El residuo es: ", residuo
#Escribir "La potencia es: ", potencia
#Escribir "¿La suma es mayor que 100?: ", suma > 100
#Fin

numero1=int(input("Ingrese un número entero"))

numero2=int(input("Ingrese un número entero"))

print("la suma entre",numero1, "y",numero2 ,"es=", numero1+numero2)

print("la resta entre",numero1, "y",numero2 ,"es=", numero1-numero2)

print("la multiplicación entre",numero1, "y",numero2 ,"es=", numero1*numero2)

print("la división entre",numero1, "y",numero2 ,"es=", numero1/numero2)

print("la división entera entre",numero1, "y",numero2 ,"es=", numero1//numero2)

print("el residuo de la división",numero1, "y",numero2 ,"es=", numero1%numero2)

print("la potencia entre",numero1, "y",numero2 ,"es=", numero1**numero2)

print("¿la suma es mayor que 100?", numero1+numero2>100)
