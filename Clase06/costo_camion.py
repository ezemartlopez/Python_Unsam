from informe_funciones import leer_camion
#preferi solo traer leer_camion()
def costo_camion(nombre_archivo):
    camion = leer_camion(nombre_archivo)
    costos_frutas = [empaque['cajones']*empaque['precio'] for empaque in camion]
    return sum(costos_frutas)

if __name__=="__main__":
    #Preferi usar missing.csv ya que tiene que manejar excepciones.
    print(costo_camion('../Data/missing.csv'))