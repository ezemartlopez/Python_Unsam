import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
def view_datafrmae_selection(df_parque,df_veredas,diccionario):
    """esta funcion recibe 2 DataFrames (df_parque y df_veredas) e imprime un bloxpot comparandolos en base a las columnas
    establecidas en el diccionario. El diccionario tiene como estructura lo siguiente
    diccionario = {'parque':'columna especifica de dataframe','vereda':'columna semejante al parque'}"""
    df_tipas_parques = df_parque[[diccionario['parque']]].copy() #trabajo con una copia de la seleccion diccionaro clave parque
    df_tipas_veredas = df_veredas[[diccionario['vereda']]].copy() #trabjo con una copia de la seleccion diccionaro clave vereda

    cols = {diccionario['parque']:diccionario['vereda']} #creo un diccionario para que los df tengan el mismo nombre de columna
    df_tipas_parques = df_tipas_parques.rename(columns=cols) # por defecto voy usar el nombre de columna de df_vereda por lo qeu solo mofico la columna de df_parque
    
    df_tipas_parques.insert(1,'ambiente','parque') # en ambos df creo una columna en cada df especificando
    df_tipas_veredas.insert(1,'ambiente','vereda') # si provienen de un parque o vereda

    df_tipas = pd.concat([df_tipas_veredas,df_tipas_parques]) #concateno ambos DataFrame 
    df_tipas.boxplot(diccionario['vereda'],by = 'ambiente') #Creo un boxplot con la columna especifica
    plt.show()

def principal():
    directorio = '../Data'
    parques = 'arbolado-en-espacios-verdes.csv'
    veredas = 'arbolado-publico-lineal-2017-2018.csv'
    fparques = os.path.join(directorio,parques)
    fveredas = os.path.join(directorio,veredas)
    df_parques= pd.read_csv(fparques)
    df_veredas = pd.read_csv(fveredas)
    dic_diametros = {'parque':'diametro','vereda':'diametro_altura_pecho'}
    dic_alturas = {'parque':'altura_tot','vereda':'altura_arbol'}

    view_datafrmae_selection(df_parques,df_veredas,dic_diametros)
    view_datafrmae_selection(df_parques,df_veredas,dic_alturas)

if __name__=='__main__':
    principal()