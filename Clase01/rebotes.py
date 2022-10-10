altura=100 #Altura inicial de la pelota

rebotes=10 #Numero de rebotes que se realizan

contador_rebotes=1 # Contador para comparar en el while
print("rebote"," altura")
while contador_rebotes <= rebotes:
    
    altura=(3/5)*altura

    print("> ",contador_rebotes," : ",round(altura,4))

    contador_rebotes=contador_rebotes+1
    