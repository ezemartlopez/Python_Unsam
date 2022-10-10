import numpy as np
import matplotlib.pyplot as plt


def plotear_temperaturas():
    temperaturas = np.load('../Data/temperatura.npy')
    plt.hist(temperaturas,bins=15)
    plt.show()

    
if __name__=="__main__":   
    plotear_temperaturas()