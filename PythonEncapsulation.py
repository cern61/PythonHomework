class Banka():
def __init__(self,isim,para,adres):
self.isim=isim
self.para=para
self.adres=adres
hesap1=Banka("Sinan",1000,"istanbul")
hesap2=Banka("Ay�e",5000,"Erzurum")
hesap1.para
hesap2.para=hesap2.para+hesap1.para #sinan'�n paras� kalmad�
hesap2.para
hesap1.para=0
hesap1.para
#bunu engellemek i�in public de�i�kenleri private yapmal�y�z

#%% encapsulation
class Banka2():
def __init__(self,isim,para,adres):
self.__isim=isim
self.__para=para
self.__adres=adres
#get ve set metotlar�
def getPara(self):
return self.__para
def setPara(self,miktar):
self.__para=miktar
def islemSayisi(self):
self.__para=self.__para-10
hes1=Banka2("Sinan",1000,"istanbul")
hes2=Banka2("Ay�e",5000,"Erzurum")
print("1. hesaptaki para: ",hes1.getPara())
hes1.setPara(100)
print("set i�lemi sonras� 1. hesaptaki para de�i�imi :",hes1.getPara())
#hes1.islemSayisi()
#print("i�lem �creti :",hes1.getPara())