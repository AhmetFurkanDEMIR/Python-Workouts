# Python OOP 3. Ders
#Özel metodlar

class Kitap0():

	pass


kitap = Kitap0() # __init__() methodu otomatik çağrılır.

print(kitap) # __str__() methodu kendi kendine tanımlandı

# len(kitap) # hata verir __len__() methodunu kendinizin tanımlamasını ister.

del kitap # __del__() methodunu çağırır ve kitap objesini siler

class Kitap():

	def __init__(self, isim, yazar, sayfa_sayisi, tur): # kendi init methodumuz

		self.isim = isim
		self.yazar = yazar
		self.sayfa_sayisi = sayfa_sayisi
		self.tur = tur

	def __str__(self): # kendi str methodumuz

		return "Kitap classı"

	def __len__(self): # kendi len methodumuz

		return self.sayfa_sayisi

	def __del__(self): # del fonksiyonuna ekstra özellik ekledik.

		print("kitap siliniyor ......")


kitap = Kitap("suç ve ceza", "dostovayeski", 1600, "polisiye")

print(kitap) # __str__() methodu bizim tanımladığımız.

print(len(kitap)) # __len__() methodu bizim tanımladığımız.

del kitap # kitap silinir



# --- Daha detaylı incelemek için : https://diveintopython3.net/special-method-names.html