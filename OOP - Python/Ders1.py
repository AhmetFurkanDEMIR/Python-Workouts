# Python OOP 1. Ders
# giriş, class, self, __init__()

class Araba():

	# özellikler herhangi bir objeye özgü değildir, classa özgüdür.(Bu örnek için.)

	model = "opel astra"

	renk = "gümüş"

	beygir_gücü = 110

	silindir_sayisi = 4

araba1 = Araba()

print(araba1.model)
print(araba1.beygir_gücü)

araba2 = Araba()

print(araba2.silindir_sayisi)

print(Araba.model)


# __init__() fonksiyonu

print(dir(Araba)) # default fonksiyonlar, python otomatik tanımlar.
# istersek kendi fonksiyonlarımızı yazarız veya değistitiriz.

# init fonksiyonu yapıcı bir fonksiyondur ve otomatik olarak çağırılır.

# --- kendi __init__() fonksiyonumuzu tanımlayalım 


class Araba1():

	def __init__(self,model="bilgi yok",renk="bilgi yok",silindir="bilgi yok"): # 3 parametre alır.
		# varsayılan değerler atanabilir
		# self anahtar kelimesi, objeyi oluşturduğumuzda o objenin referansıdır.
		# mutlaka her bir methodun en başında bulunur.

		print("\n\n  init fonksiyonu çağırıldı")

		# artık özelllikler objeye özgüdür. classa özgü değildir.
		self.model = model
		self.renk = renk
		self.silindir = silindir


araba1 = Araba1("megan","mavi",4)

print(araba1.model)

araba99 = Araba1("opel","mavi")

print("aracın silindiri = {}".format(araba99.silindir))
