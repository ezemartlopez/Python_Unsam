from camion import Camion
from informe_final import leer_camion
#preferi solo traer leer_camion()
def costo_camion(nombre_archivo):
    '''
    Computa el precio total (cantidad * precio) de un archivo camion
    '''
    camion = leer_camion(nombre_archivo)
    
    un_camion = Camion(camion) 
    return un_camion.precio_total()

def f_principal(lista):
    try:
        if len(lista)!= 2:
            raise SystemExit(f'Uso adecuado: {lista[0]} archivo_camion')
        costo = costo_camion(lista[1])
        print(f"Costo total: {costo}")
    except Exception as e:
        print(e)
if __name__=="__main__":
    #Preferi usar missing.csv ya que tiene que manejar excepciones.
    #import sys
    #f_principal(sys.argv)
    f_principal(['hola.py','../Data/camion.csv'])