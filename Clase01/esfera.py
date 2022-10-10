import math

#obtengo el valor del radio de la esfera ingresado por el usuario
radio_esfera=input("ingrese el radio de la esfera\n")

#covierto al tipo float el valor obtenido en el input
radio=float(radio_esfera)

#calculo el volumen de la esfera
volumen_esfera=(4/3)*(math.pi)*(radio**3)

#muestro el volumen con una precision de 8 decimales
print("el volumen de la esfera de radio ",radio_esfera," es: ",round(volumen_esfera,8))