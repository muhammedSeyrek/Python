
#%%Stack arrays
import numpy as np
#dizileri sutun ve satir olarak birlestirir.
dizi1 = np.array([20, 40])
dizi2 = np.array([10, 30])
##T Transpose  ediyor
d = np.stack((dizi1, dizi2)).T

np.hstack((dizi1[:, None], dizi2 [:, None]))


#%%Selection
dizi1 = np.arange(10, dtype = float).reshape(2, 5)
#dizi elemanlarina erisim
#syntax1: dizi[satir] veya dizi[satir, sutun]
#syntax2: dizi[satir][sutun]

# %% Slice
import numpy as np
dizi1[0, :] #ilk satiri 1D dizi olarak keser
dizi1[:, 1] #1.sutunun tum satirlari
dizi1[:, :2]#2.sutundan onceki tum satirlar
dizi1[:, 2:]#2 ve 2 den sonraki satirlar

dizi1[:, 1 : 4]

dizi1[0, ::-1]#ilk satiri tertten dondurur






# %%
import numpy as np

dizi2 = dizi1[:, [1, 2, 3]] #1, 2, 3.satirlari kopyalar

dizi2 = dizi1[dizi1 < 5]

dizi2[dizi1 < 5]

dizi1[dizi1 < 5] = 44 #dizideki degeri 5 ten kucuk  elemanlara 55 sayisini atadik.

dizi1 * 10 #her bir elemani 10 ile carpar.

dizi3 = np.sqrt(dizi1)
np.ceil(dizi3)

mesafe = np.sqrt(np.sum((dizi1 - dizi2) ** 2))

ortalama = dizi1.mean() 
standartSapma = dizi1.std()

minNdx = dizi1.argmin() #en kucuk eleman
toplama = dizi1.sum()
topSutun = dizi1.sum(axis = 0)
topSatir = dizi1.sum(axis = 1)

#%%
