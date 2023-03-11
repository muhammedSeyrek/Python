
class Elma():
    def __init__(self, isim):
        self.isim = isim
    
    def bilgiVer(self):
        return self.isim + " 100 kaloridir. "
    
class Muz():
    def __init__(self, isim):
        self.isim = isim
    
    def bilgiVer(self):
        return self.isim + " 150 kaloridir. "

elma = Elma("Elma")

muz = Muz("Muz")

meyveSepeti = [elma, muz]

for meyve in meyveSepeti:
    print(meyve.bilgiVer())

def bilgiAl(meyve):
    print(meyve.bilgiVer())

bilgiAl(elma)