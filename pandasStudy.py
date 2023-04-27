
import numpy as np
import pandas as pd


#%%Seriler
import pandas as pd

benimSozlugum = {"Muhammed" : 22, "Merve" : 20, "Apocan" : 26}

pd.Series(benimSozlugum)

benimYaslarim = [22, 20, 26]
benimIsimlerim = ["Muhammed", "Merve", "Abdullah"]


pd.Series(benimYaslarim, benimIsimlerim)
#karismamasi icin asagidaki gibi kullanalim

pd.Series(data = benimYaslarim, index = benimIsimlerim)

# %%numpy dizisi ile yapalim

numpyDizisi = ([22, 20, 26])

pd.Series(numpyDizisi, benimIsimlerim)

#%% Series ozellikleri

pd.Series(["Muhammed", "Atlas", "Osman"], [1, 2, 3])

yarismaSonucu1 = pd.Series([10, 5, 1], ["Muhammed", "Atlas", "Ali"])
yarismaSonucu1
yarismaSonucu2 = pd.Series([20, 10, 8], ["Muhammed", "Atlas", "Ali"])
yarismaSonucu2
yarismaSonucu2["Atlas"]
sonSonuc = yarismaSonucu1 + yarismaSonucu2
sonSonuc

farkliSeries = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"])
farkliSeries2 = pd.Series([10, 5, 3, 1], ["a", "c", "f", "g"])
farkliSeries + farkliSeries2

#%%
