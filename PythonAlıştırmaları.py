class Animal():
def __init__(self):
print("hayvan sýnýfýnýn yapýcý metotum")
def sesCikar(self):
print("hav,miyav,vak....")
def hareket(self):
print("zýplar,koþar,yürür..")
#cocuk sýnýf ----child
class kedi(Animal):
def __init__(self):
super().__init__() # yazmasakta olur ata sýnýfýn init metodunu ezeriz metot overriding!!
print("kedi sýnýfý oluþturuldu")
def sesCikar(self):
print("miyav")
def DokuzCan(self): #diðer hayvanlardan ayrýlan bir fonksiyon :D
print("Bu sevimli hayvanlar hep dört ayak üstüne düþer")

k1=kedi()
k1.sesCikar() #ata sýnýfý ezer
k1.hareket()
k1.DokuzCan()

class kus(Animal):
def __init__(self):
print("kus sýnýfý oluþturldu")
def ucma(self):
print("kanatlarý vardýr uçarlar")
kus1=kus()
kus1.ucma()
kus1.hareket()
