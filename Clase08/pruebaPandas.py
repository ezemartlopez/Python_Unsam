import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
vereda = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
fveredea = os.path.join(directorio,vereda)
df_parques= pd.read_csv(fname)
df_veredas = pd.read_csv(fveredea)
#print(df.head(5))
#print(df[['altura_tot', 'diametro', 'inclinacio']].describe())
#print(df['nombre_com'].unique())
#cols = ['altura_tot', 'diametro', 'inclinacio']
#df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()
#sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')
#plt.show()
print(df_veredas.head(2))