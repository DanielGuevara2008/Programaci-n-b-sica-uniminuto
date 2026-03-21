#ALGORITMO
#Pedir al usuario que ingrese su nombre.
#Guardar esa información en una variable
#Pedir al usuario que ingrese su consumo mensual de agua en metros cúbicos (número entero).
#Guardar esa información en una variable
#Evaluar el consumo de agua
#1 a 15 metros cubicos=Bajo consumo
#16 a 30 metros cubicos=Consumo normal
#Más de 30 metros cubicos=Alto consumo
#0 o un valor negativo=Dato invalido
#Mostrar en la consola el nombre del usuario, la categoría y el mensaje correspondiente.
#Si el consumo es 0 o negativo, mostrar el mensaje de error correspondiente.

Nombre=input("Ingrese su nombre")
Consumo=int(input("Ingrese su consumo mensual de agua en metros cubicos"))
if Consumo >=1 and Consumo <=15:
    print(Nombre)
    print("Bajo consumo")
    print("¡Excelente! Eres un usuario responsable del agua")

elif Consumo >=16 and Consumo <=30:
    print(Nombre)
    print("Consumo normal")
    print("Tu consumo está dentro del promedio del hogar")

elif Consumo >30:
    print(Nombre)
    print("Alto consumo")
    print("Atención: tu consumo es alto, revisa posibles fugas")

else:
    print(Nombre)
    print("Dato inválido")
    print("Error: el consumo debe ser un número mayor a 0")
