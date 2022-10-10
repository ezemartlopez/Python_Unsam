import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


def principal():
    """dados una lista de superficies y una lista de precios aproximados, obtiene la ecuacion de la 
    regresion lineal y lo grafica"""
    #listas para la regresion, alquiler en base a superficie
    superficie = np.array([150.0, 120.0, 170.0, 80.0])
    alquiler = np.array([35.0, 29.6, 37.4, 21.0])

    a, b = ajuste_lineal_simple(superficie,alquiler)
    print(f"ecuacion de la regresion: {a} * X + {b}")
    
    #Seccion para el grafico de la ecuacion
    maximo_x = superficie.max()
    x = np.arange(int(maximo_x))
    y = a*x + b
    plt.plot(x,y,c = 'green')
    plt.xlabel('superficie')
    plt.ylabel('alquiler')
    #Seccion para los puntos representativos
    plt.scatter(superficie, alquiler)

    plt.show()

    errores = alquiler - (a*superficie + b)
    print(f"Los errores son: {errores}")
    print("ECM:", (errores**2).mean())

if __name__=='__main__':
    principal()
