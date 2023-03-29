
#%% 
import numpy as np

benimDizim = np.arange(0, 15)

benimDizim

benimDizim[5]
benimDizim[3:8]

benimDizim[3:8] = -5
benimDizim

baskaDizi = np.arange(0, 24)
slicingDizisi = baskaDizi[4:9]
slicingDizisi[:] = 700
slicingDizisi
##bunuda degistirecek o araliktaki sayilar 700 olacak
baskaDizi

ornekDizi = np.arange(0, 24)
ornekDizi

ornekDiziKopyasi = ornekDizi.copy()

ornekDiziKopyasiSlising = ornekDiziKopyasi[3:6]
ornekDiziKopyasiSlising[:] = 800
##bu yine degisir
ornekDiziKopyasi
##ama kopyaladigimiz listedeki kisimlar degismeyecek.
ornekDizi

#%%Matrix
import numpy as np

benimListem = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]
benimMatrixDizim = np.array(benimListem)
benimMatrixDizim[1][2]
##usteki ile ayni alttaki
benimMatrixDizim[0:, :1]



#%%
