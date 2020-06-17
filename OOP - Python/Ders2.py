# Python OOP 2. Ders
# Örnek proje, kendi fonksiyonlarımız.

class Yazilimci():

	def __init__(self, isim, soyisim, numara, maas, programlama_dilleri):

		# objenin parametreleri
		self.isim = isim
		self.soyisim = soyisim
		self.numara = numara
		self.maas = maas
		self.programlama_dilleri = programlama_dilleri


	# kendi yazdığımız fonksiyonumuz. Yaratılacak yazılımcı objeleri hakkında bilgi verir
	# bizim methodumuz
	def bilgileri_göster(self):

		print("""


  Isim                 : {}

  Soyisim              : {}	

  Numara               : {}

  Maas                 : {}

  Programlama dilleri  : {}
""".format(self.isim, self.soyisim, self.numara, self.maas, self.programlama_dilleri))

	# yöneticiden zam miktarı alınır, daha sonra maas değiskenindeki değerle toplanır.
	# zam fonksiyonu
	def zam_yap(self, zam_miktarı):

		self.zam_miktarı = zam_miktarı

		self.maas += self.zam_miktarı

		print("\n Zam başarıyla yapılmıştır \n")


	# yazılımcı yeni bir dil öğrenirse, bildiği dillerin arasına yeni dil eklenir.
	def yeni_Programlama_dili(self, yeni_dil):

		self.yeni_dil = yeni_dil

		self.programlama_dilleri.append(yeni_dil)

		print("\n Basariyla güncellenmistir. \n")



# yeni bir obje yarattık
yazilimci1 = Yazilimci("Ahmet Furkan", "DEMIR", "01093579854", 20000, ["Python", "C", "C++", "Java"])

# yaratılan objeden bilgileri göster fonksiyonu çağrılır.
print(yazilimci1.bilgileri_göster())

# 5000 dolarlık bir zam yaptık
yazilimci1.zam_yap(5000)

#yeni maasimiz
print(yazilimci1.maas)

# yeni programlama dili eklenir.
yazilimci1.yeni_Programlama_dili("R")

# son hali
print(yazilimci1.programlama_dilleri)










