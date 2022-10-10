#modifique el codigo utilizado anteriormente a algo mas preciso y lo implemente como funcion
def geringoso(cadena):
    """Toma una cadena y la convierte al geringoso"""
    auxiliar = cadena.lower()#convierto la cadena en minusculas para no tener inconvenientes
    vocales = 'aeiou'
    #itera por cada vocal y si se encuentra en la palabra lo modifica por el prefijo del geringoso
    for vocal in vocales: 
        prefijo = vocal+'p'+vocal
        auxiliar = auxiliar.replace(vocal,prefijo)
    
    return auxiliar

def diccionario_geringoso(lista):
    """Toma un lista de palabras y las convierte al geringoso, devolviendo un diccionario con clave a la palabra leida y el valor la conversion"""
    diccionario={}

    for item in lista:
        item_conversion = geringoso(item)#convierto la palabra de la lista al geringoso con una funcion
        diccionario.update({item: item_conversion})
    return diccionario

if __name__=="__main__":
    print(diccionario_geringoso(['banana', 'manzana', 'mandarina']))