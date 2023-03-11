benimListem = list()
type(benimListem)
##instance & attribute
class SuperKahraman():

    ozelGuc = "Gorunmezlik"


    def __init__(self, isimInput, yasInputu, meslekInputu):
        print("init cagrildi")
        self.isim = isimInput
        self.yas = yasInputu
        self.meslek = meslekInputu

    def ornekMethod(self):
        print(f"Ben bir superkahramanim meslegim : {self.meslek}")

superman = SuperKahraman("Superman", 33, "Gazeteci")
superman.isim = "Clark Kent"
print(superman.ozelGuc)
superman.ornekMethod()

##default deger icin fonksiyonun calismasi

class Kopek():
    
    yilCarpani = 7

    def __init__(self, yas = 5, kopekYasi = 5 * 7):
        self.yas = yas
        self.kopekYasi = yas * 7

    def kopekYasHesapla(self):
        return Kopek.yilCarpani * self.yas #Kopek.yilCarpani = self.yilCarpani


benimKopek = Kopek()
print(benimKopek.kopekYasi)

print(benimKopek.kopekYasHesapla())








