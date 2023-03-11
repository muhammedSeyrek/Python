
#inheritance

class Hayvan():
    
    def __init__(self):
        print("Bu method init")

    def method1(self):
        print("Bu method1")

    def method2(self):
        print("Bu method2")
    

class Kedi(Hayvan):
    
    def __init__(self):
        super().__init__()
        print("Kedi sinifi init cagrildi.")

    def method1(self):
        print("Kedi sinifindaki method1 cagrildi.")

    def miyavla(self):
        print("Miyav")

benimKedim = Kedi()

print(benimKedim.miyavla()) 

