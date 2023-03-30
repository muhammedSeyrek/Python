#%% Veri Yapilari
#Seriler(Series) : 1D Array
#Veri Cercevesi(DataFrame) : 2D Array

import pandas as pd
import numpy as np

sutunlar = ['ad', 'yas', 'cinsiyet', 'ders']

ogr1 = pd.DataFrame([['Ahmet', 19, "E", "Veri Bilimi"],
                     ['Alican', 22, "E", "Veritabani Sistemleri"]],
                     columns = sutunlar)
print(ogr1)

ogr2 = pd.DataFrame([["Azize", 18, "K", "AR/VR"],
                     ["Muhammed", 22, "E", "CyberSecurity"]],
                     columns = sutunlar)
print(ogr2)

#%% Concatenate (Birlestirme)
ogr = pd.concat([ogr1, ogr2])
print(ogr)

ogr3 = pd.DataFrame(dict(ad = ["Meral", "Yusuf", "Yakup", "Elif"],
                         notlar = [90, 21, 43, 67]))
print(ogr3)

birlestirAd = pd.merge(ogr, ogr3, on = 'ad', how = 'outher')
print(birlestirAd)

type(ogr)
ogr.head() #ilk 5 satir 
birlestirAd.head()
birlestirAd.tail() #son 5 satir
birlestirAd.index
birlestirAd.columns
birlestirAd.dtypes
birlestirAd.shape
birlestirAd.values
birlestirAd.info()

#%% Sutun Secimi    
birlestirAd['ad']
birlestirAd[['ad', 'ders']]

# %%
