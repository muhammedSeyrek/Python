import numpy as np
import pandas as pd

#%%
import numpy as np
import pandas as pd
data = np.random.randn(4, 3)

dataFrame = pd.DataFrame(data)
dataFrame

yeniDataFrame = pd.DataFrame(data, index = ["Muhammed", "Merve", "Ahmet", "Abdullah"],
                             columns = ["Maas", "Yas", "CalismaSaati"])
yeniDataFrame 
yeniDataFrame["Yas"]
yeniDataFrame["CalismaSaati"]

yeniDataFrame[["Maas", "Yas"]]
#yeniDataFrame["Muhammed"]#bu olmaz
yeniDataFrame.loc["Muhammed"]#bu sekil yapmak gerek
#index ile de cagirabiliriz
yeniDataFrame.iloc[1]

#kolon ekleme
yeniDataFrame["EmeklilikYasi"] = yeniDataFrame["Yas"] + yeniDataFrame["Yas"]
yeniDataFrame
#kolon silme
yeniDataFrame.drop("EmeklilikYasi", axis = 1)
#satir silme
yeniDataFrame.drop("Abdullah")
yeniDataFrame

yeniDataFrame.drop("EmeklilikYasi", axis = 1, inplace = True)

yeniDataFrame.loc["Merve"]["Yas"]
#bu sekilde olur
yeniDataFrame.loc["Ahmet", "Yas"]

booleanFrame = yeniDataFrame < 0
booleanFrame
yeniDataFrame[booleanFrame]

yeniDataFrame["Yas"] > 0

yeniDataFrame[yeniDataFrame["Yas"] > 0]

#index diye sutun aciyor
yeniDataFrame.reset_index()

yeniDataFrame
yeniIndexListesi = ["Muh", "Mev","Ahm", "Abd"]
yeniDataFrame["YeniIndex"] = yeniIndexListesi
yeniDataFrame.set_index("YeniIndex")

yeniDataFrame
#alttaki komu uygulanan komutu kalici kaydediyor.
yeniDataFrame.set_index("YeniIndex", inplace = True)
yeniDataFrame.loc["Abd"]



#%%Multi Indexler
import pandas as pd
import numpy as np
ilkIndeksler = ["Simpson", "Simpson", "Simpson", "SouthPark", "SouthPark", "SouthPark"]
icIndeksler = ["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kyle"]

birlesmisIndeks = list(zip(ilkIndeksler, icIndeksler))
birlesmisIndeks 
#bu daha iyi
birlesmisIndeks = pd.MultiIndex.from_tuples(birlesmisIndeks)
birlesmisIndeks

benimCizgiFilmListem = [[40, "A"], [10, "B"], [30, "C"], [9, "D"]
                        , [10, "E"], [11, "F"]]
cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListem)
cizgiFilmDataFrame = pd.DataFrame(benimCizgiFilmListem, index = birlesmisIndeks, 
                                  columns = ["Yas", "Meslek"])
cizgiFilmDataFrame
cizgiFilmDataFrame.loc["Simpson"]
cizgiFilmDataFrame.loc["SouthPark"].loc["Kenny"]

cizgiFilmDataFrame.index.names = ["Film Adi", "Isim"]
cizgiFilmDataFrame




# %%
