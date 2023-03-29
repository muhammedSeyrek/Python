

#%%
import numpy as np

benimListem = [20, 30, 40]

type(benimListem)

np.array(benimListem)

matrixListesi = [[10, 20, 30], [40, 50, 60]]

np.array(matrixListesi)



#%% arange
import numpy as np

list(range(0, 10))

np.arange(0, 10)

np.arange(0, 20, 2)

#%% zeros
import numpy as np

np.zeros(5)

np.zeros((9, 9))


#%% ones
np.ones(5)

np.ones((9, 9))


#%% linspace 

np.linspace(0, 20, 6)


#%% eye

np.eye(10)

#%%random

np.random.randn(3,4)

np.random.randint(1, 100, 5)

benimNumpyDizim = np.arange(30)
benimNumpyDizim

benimRandomDizim = np.random.randint(0, 100, 30)
benimRandomDizim

#%%Numpy dizi metotlari

reshapeArray = benimNumpyDizim.reshape(6, 5)

benimNumpyDizim.argmax()

benimRandomDizim.max()
benimRandomDizim.min()

benimRandomDizim.argmax()
benimRandomDizim.argmin()

reshapeArray.shape

#%%
