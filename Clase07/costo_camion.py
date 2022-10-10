from informe_final import leer_camion
#preferi solo traer leer_camion()
def costo_camion(nombre_archivo):
    camion = leer_camion(nombre_archivo)
    costos_frutas = [empaque['cajones']*empaque['precio'] for empaque in camion]
    return sum(costos_frutas)
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
    import sys
    f_principal(sys.argv)