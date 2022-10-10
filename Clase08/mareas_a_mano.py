import pandas as pd
import matplotlib.pyplot as plt
def principal():
    """Lee el archivo csv en la ubicacion '../Data/OBS_SHN_SF-BA.csv' """
    df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)
    dh = df['12-25-2014':].copy() # obtengo una copia de las lecturas a partir del '25-12-2014'
    delta_t = -1 # tiempo que tarda la marea entre ambos puertos
    delta_h = 19 # diferencia de los ceros de escala entre ambos puertos
    pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
    plt.show()

if __name__=='__main__':
    principal()