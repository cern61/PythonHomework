class Animal():
def __init__(self):
print("hayvan s�n�f�n�n yap�c� metotum")
def sesCikar(self):
print("hav,miyav,vak....")
def hareket(self):
print("z�plar,ko�ar,y�r�r..")
#cocuk s�n�f ----child
class kedi(Animal):
def __init__(self):
super().__init__() # yazmasakta olur ata s�n�f�n init metodunu ezeriz metot overriding!!
print("kedi s�n�f� olu�turuldu")
def sesCikar(self):
print("miyav")
def DokuzCan(self): #di�er hayvanlardan ayr�lan bir fonksiyon :D
print("Bu sevimli hayvanlar hep d�rt ayak �st�ne d��er")

k1=kedi()
k1.sesCikar() #ata s�n�f� ezer
k1.hareket()
k1.DokuzCan()

class kus(Animal):
def __init__(self):
print("kus s�n�f� olu�turldu")
def ucma(self):
print("kanatlar� vard�r u�arlar")
kus1=kus()
kus1.ucma()
kus1.hareket()
