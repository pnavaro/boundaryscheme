"""
This file aims at testing and plotting the DKL function
"""

import numpy as np
import matplotlib.pyplot as plt
import os
path_here = os. getcwd()
import sys
sys.path.insert(0,path_here+"/thesis")

from schemes import *


# scheme choice
scheme = BeamWarming
order = 5
lamb = 0.35


if __name__ == "__main__":
    fig = plt.figure(1, figsize=(6, 4))

    S = scheme(lamb,order = order)
    X,Y = S.symbol()
    T = np.linspace(0,7,1000)

    plt.ylim(-1,1)
    plt.xlim(-1,1)
    plt.plot(np.cos(T),np.sin(T), color = "black", label = "unit circle")
    plt.plot(X,Y, label = "symbol")
    plt.axis("equal")
    plt.legend(loc="best")
    plt.title("Symbol of "+ S.name(lambda_bool = True))
    plt.show()
