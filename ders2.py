import math
import matplotlib
bosListe = []
bosListe2 = list()

dersler = ['Java', "DBMS", "Veri Bilimi"]

print(dersler[0])

print("dersler listesinin uzunlugu", len(dersler))

dersler.append("CLang")

print(dersler[3])

dersler.extend(["Makine Ogrenmesi", "Yapay Zeka", "Otomata"])

dersler.insert(2, "DelphiLang")

dersler.remove("DBMS")

silinenDers = dersler.pop(2)

a = "Muhammed "
b = "Seyrek"
a += b
print(a)

secmeliDersler = ["ARVR", "Game Prog"]
dersler = dersler + secmeliDersler

dersler[0]
dersler[2:5] #5 haric
dersler[:5] #0'dan 5(haric) e kadar
dersler[5:]
dersler[-1]
dersler[::2] #her 2.elemani sec

#sort
dersler.sort()#a'dan z'ye siralar
#siralamayi tersine cevirir
dersler.sort(reverse=True)

#%%
haftalar = (0, 1, "Carsamba", "Persembe", "Cuma", 6, 7)
len(haftalar)
haftalar[4]
haftalar = haftalar + (0, 1, 2, 3, 4, 5, 6, 7)

haftalar2 = (0, 1, 2, 3, 4, 5, 6, 7) * 2 #cogaltir. carpmaz!


#%%Strings
str1 = '25'
str2 = str(25)#convert to string 
str3 = 'Erzurum Teknik Üniversitesi'

str3[:14]
str3[15:]
str3[-7]

str3.lower()
str3.upper()
str3.startswith('E') #True olur
str3.endswith('Universitesi') #True olur
str3.isdigit()
str1.isdigit()

str3.endswith('i')
str3.find("Teknik")
str3.find("25")

str3 = str3.replace("Üniversitesi", "Enstitüsü")

str3.split(' ')
str3.split('i')

str4 = "Yakutiye"

print("Okulumuz " + str3 + " dir")

print("Okulumuz {}, konumu {} ve {} plaka no'ya sahiptir.".format(str3, str4, str1))

print("AGNO = {:.2f}".format(3.4132))

print("Okulumuz {},\n konumu {} ve\n {} plaka no'ya sahiptir.".format(str3, str4, str1))

print(r'G:\Drive\nDers\tDataScience\Codes')

#%%Dictionaries

bosSozluk1 = {}
bosSozluk2 = dict()

okul1 = {'okul' : 'etu', 'konum' : 'Erzurum', 'bolum' : 'Bilgisayar Muh'}
okul2 = dict(okul = 'Etu', konum = 'Erzurum')

okul1['konum']
okul1.keys()
okul1.values()
okul1.items()

'konum' in okul1

okul1['ulke'] = "Turkiye"

#%%Setler
bosSet = set()
progDil = {'Python', 'Java', 'C#'}

progDil.add('Sql')
progDil.remove('Java')
progDil.clear()


#%%Gorsellestirme(Visualization)
from numpy import sin
from matplotlib import pyplot
x = [x * 0.1 for x in range(100)]
y = sin(x)
pyplot.plot(x, y)
pyplot.show()



#%%Radial Bar
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

notDers = {"Dersler" : ['Java', 'Python', 'DBMS', 'Veri Bilimi', 'Matematik', 'Yapay Zeka', 'Otomata'],
            "Notlar" : [40, 60, 85, 90, 50, 35, 30]}
df = pd.DataFrame.from_dict(notDers)

maksimum = max(df['Notlar'])

uzunluk = len(df)

ringRenkler = ['#354fa', '#345fb', '#134cd', '#872fd', '#434de', '#432aa', '#765ff']

ringEtiketler = [f'{x} ({v})' for x, v in zip(list(df['Dersler']), list(df['Notlar']))]

fig = plt.figure(figsize = (10, 10), linewidth = 10, edgecolor = '#345adc', facecolor = '#5adad5')

rect = [0.1, 0.1, 0.8, 0.8]

axPolarBg = fig.add_axes(rect, polar = True, frameon = False)
#barlarin baslangici
axPolarBg.set_theta_zero_location('N')
axPolarBg.set_theta_direction(1)

for i in range(uzunluk):
    axPolarBg.barh(i, maksimum * np.pi * 1.5 / maksimum, color = 'grey', alpha = 0.1)

axPolarBg.axis('off')

axPolar = fig.add_axes(rect, polar = True, frameon = False)
axPolar.set_theta_zero_location('N')
axPolar.set_theta_direction(1)
axPolar.set_rgrids([0, 1, 2, 3, 4, 5, 6],
                   labels = ringEtiketler, angle = 0, fontSize = 14, fontWeight = 'bold',
                   color = 'white', verticalAlignment = 'center')
for i in range(uzunluk):
    axPolar.barh(i, list(df['notlar'])[i] * np.pi * 1.5 / maksimum, color = ringRenkler[i])

axPolar.grid(False)
axPolar.tick_params(axis = 'both', left = False, bottom = False, labelButtom = False, labelLeft = True)
plt.show()































# %%
