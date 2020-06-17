# Python OOP 3. Ders
# Kalıtım(Inheritance)
# overriding
# Super anahtar kelimesi

class Calisan():

	def __init__(self, isim, mass, departman):

		self.isim = isim
		self.mass = mass
		self.departman = departman


	def bilgileri_göster(self):

		print("""

  Isim       : {}

  Mass       : {}

  Departman  : {}

			""".format(self.isim, self.mass, self.departman))


	def departman_degistir(self, yeni_departman):

		self.yeni_departman = yeni_departman

		self.departman = self.yeni_departman

		print(" Yeni Departman {} olarak degistirilmistir. ".format(self.departman))



# Calisan sinifindan miras alır
# Calisan sınıfına ait olan herseyi kullanabilir.
class Yönetici(Calisan):
	
	# artık yönetici sınıfının kendi init fonksiyonu var.
	def __init__(self, isim, mass, departman, kisi_sayisi):

		self.isim = isim
		self.mass = mass
		self.departman = departman
		self.kisi_sayisi = kisi_sayisi

	# Yönetici sınıfına özgü fonksiyonumuz.
	def zam_yap(self,zam_miktarı):

		self.zam_miktarı = zam_miktarı

		self.mass += self.zam_miktarı

		print("\n Maasiniz {} TL olarak güncellenmiştir.".format(self.mass))


	def bilgileri_göster(self):

		print("""

  Isim                : {}

  Mass                : {}

  Departman           : {}

  Sorumlu Kişi sayisi : {}

			""".format(self.isim, self.mass, self.departman, self.kisi_sayisi))

	# overriding
	def departman_degistir(self, yeni_departman):

		self.yeni_departman = yeni_departman

		self.departman = self.yeni_departman

		print(" Yeni Departman {} olarak degistirilmistir. ".format(self.departman))

calisan1 = Yönetici("Mehmet SONMEZ", 45000, "Temizlik",20)

print(calisan1.bilgileri_göster())

calisan1.departman_degistir("Insan kaynaklari")


print(dir(Yönetici)) # yönetici sınıfının fonksiyonları

print(calisan1.zam_yap(200))

yönetici999 =  Yönetici("mehmed ali", 50000, "saglik", 10)

print(yönetici999.bilgileri_göster())


class Patron(Yönetici):

	def __init__(self, isim, mass, departman, kisi_sayisi, sirket_adi):

		# aynı değişkenleri tekrar tanımlamamıza gerek kalmaz, Yönetici sınıfındaki init fonksiyonunu miras aldık.
		super().__init__(isim, mass, departman, kisi_sayisi)

		self.sirket_adi = sirket_adi



	def maas_guncelle(self,yeni_maas):

		self.yeni_maas = yeni_maas

		self.mass = self.yeni_maas

		print("maasiniz {} olarak güncellenmiştir.".format(self.mass))



patron1 = Patron("Ahmet Furkan DEMIR", 100000, "Yazılım", 300, "demira.ai")

patron1.maas_guncelle(150000)


