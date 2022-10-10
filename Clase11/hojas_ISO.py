#
#   Mi funcion recursiva funciona de manera diferente al que pedia
#   pero funciona de igual manera
#   
#   @author: Martinez Ezequiel

def medidas_hoja_A(N):
    """Es una funcion recursiva que para una entrada N mayor que cero, devuelve
    el ancho y largo de la hoja A(N), en formato tupla."""
    def doblar_hoja(tupla,N):
        """Recibe una tupla con las medidas de una hoja (ancho y largo)
        y lo dobla si N aun lo permite"""
        if N == 0: #Caso Base: si ya no se puede doblar
            return tupla
        else:
            #obtengo los valores de la tupla
            ancho = tupla[0]
            largo = tupla[1]
            #Busca el lado mas largo y realiza el pliegue de la hoja
            if ancho > largo:
                return doblar_hoja((ancho//2,largo),N-1)
            else:
                return doblar_hoja((largo//2,ancho),N-1)

    tupla = doblar_hoja((841,1189),N)
    return tupla

if __name__=='__main__':
    for i in range(7):
        print(f"Hoja A{i}: {medidas_hoja_A(i)}")