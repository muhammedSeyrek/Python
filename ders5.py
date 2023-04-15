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
import pandas as pd
import numpy as np
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
import pandas as pd
import numpy as np
birlestirAd['ad']
birlestirAd[['ad', 'ders']]
tlb = birlestirAd

tlb[tlb.ad.isin('Ahmet', 'Utku')]
#%% Siralama
import pandas as pd
import numpy as np
df = tlb.copy()
df.yas.sort_values()
df.sort_values(by = "yas")
df.sort_values(by = "yas", ascending = False)
df.sort_values(by = ['ders', 'ad'])

# %%Istatistikler ve gruplama
import pandas as pd
import numpy as np
print(df.describe())

print(df.groupby('ders').mean)
print(df.groupby('ders')['notlar'].mean)


# %% Tekrar verilerin giderilmesi
print(df.ders.duplicated().sum())


# %%  Kayip veriler
df.cinsiyet.isnull()
df.cinsiyet.notnull()
df[df.cinsiyet.notnull()]
df.cinsiyet.isnull().sum()

df.isnull().sum()

df.dropna() #kayip degerli olan satirlari cikar

df.loc[df.cinsiyet.isnull(), 'cinsiyet'] = 'E'



#%% File I/O
import os.path, tempfile
tmpFolder = tempfile.gettempdir()
excDosyaAd = os.path.join(tmpFolder, "Ogrenciler.xlsx")
df.to_excel(excDosyaAd, sheet_name = 'Ogrenciler', index = False)
#Excel dosyasini import et
veri = pd.read_excel("C:\Users\Muhammed\Desktop\PythonTraining\Ogrenciler.xlsx")

