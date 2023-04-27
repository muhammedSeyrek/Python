
import numpy as np
import pandas as pd
#%% Operasyonlar
import numpy as np
import pandas as pd

sozlukVerisi = {"Istanbul" : [30, 29, np.nan], "Ankara" : [20, np.nan, 25], "Izmir" : [40, 39, 38]}

havaDurumuDataFrame = pd.DataFrame(sozlukVerisi)
havaDurumuDataFrame

#nan varsa sil
havaDurumuDataFrame.dropna()

#sadece sutununda nan olmayani tut
havaDurumuDataFrame.dropna(axis = 1)

yeniVeri = {"Istanbul" : [30, 29, np.nan], 
            "Ankara" : [20, np.nan, 25], 
            "Izmir" : [40, 39, 38], 
            "Antalya" : [45, np.nan, np.nan]}
yeniDataFrame = pd.DataFrame(yeniVeri)
yeniDataFrame

#2 ve uzeri nan olanlari atiyor
yeniDataFrame.dropna(axis = 1, thresh = 2)
yeniDataFrame

#bos olanlari doldur
yeniDataFrame.fillna(20)


# %%Group by metodu kullanimi

maasSozlugu = {"Departman" : ["Yazilim", "Satis", "Pazarlama", "Pazarlama", "Hukuk", "Hukuk"],
               "Calisan Ismi" : ["Muhammed", "Merve", "Ahmet", "Abdullah", "Meral", "Yusuf"],
               "Maas" : [100, 150, 200, 300, 400, 500]}
maasDataFrame = pd.DataFrame(maasSozlugu)
maasDataFrame

grupObjesi = maasDataFrame.groupby("Departman")
grupObjesi.count()
#maas ortalama
grupObjesi.mean()
grupObjesi.max()
#herseyi hesapliyor
grupObjesi.describe()

# %%Concat - birlestirmek
import numpy as np
import pandas as pd

sozluk1 = {"Isim" : ["Muhammed", "Merve", "Ahmet", "Abdullah"],
           "Spor" : ["Kosu", "Yuzme", "Kosu", "Basketbol"],
           "Kalori" : [100, 200, 300, 400]}
dataFrame1 = pd.DataFrame(sozluk1, index = [0, 1, 2, 3])

sozluk2 = {"Isim" : ["Osman", "Levent", "Atlas", "Fatma"],
           "Spor" : ["Kosu", "Yuzme", "Kosu", "Basketbol"],
           "Kalori" : [200, 100, 50, 300]}
dataFrame2 = pd.DataFrame(sozluk2, index = [4, 5, 6, 7])

sozluk3 = {"Isim" : ["Ayse", "Mahmut", "Duygu", "Nur"],
           "Spor" : ["Kosu", "Yuzme", "Badminton", "Tenis"],
           "Kalori" : [300, 400, 500, 250]}  
dataFrame3 = pd.DataFrame(sozluk3, index = [8, 9, 10, 11])

dataFrameAll = pd.concat([dataFrame1, dataFrame2, dataFrame3], axis = 0)
dataFrameAll

# %%
