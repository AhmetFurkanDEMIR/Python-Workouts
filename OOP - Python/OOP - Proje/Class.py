
class Ogrenci():

	def __init__(self, ad_soyad, tc_no, okul_no, ders_sayisi, bolum, dersler):

		self.ad_soyad = ad_soyad
		self.tc_no = tc_no
		self.okul_no = okul_no
		self.ders_sayisi = ders_sayisi
		self.bolum = bolum
		self.dersler = dersler

	def ogrenci_bilgi(self):

		print(""" 

  İsim Soyisim              : {}

  T.C No                    : {}

  Okul No                   : {}

  Okuduğu Bölüm             : {}

  Aldığı Ders Sayısı        : {}

  """.format(self.ad_soyad, self.tc_no, self.okul_no, self.bolum, self.ders_sayisi))

	def __str__():

		self.strr = """\n  Üniversite Otomasyonu, Öğrenci Bölümü. Ogrenci bilgileri : Ad-Soyad, T.C No, Okul No, Bolum, Aldığı Ders sayisi, """

		return 


	def __len__(self):

		return self.ders_sayisi



	def __del__(self):

		print("\n Öğrenci silinmiştir.")


class Dersler():

	def __init__(self,ders_adi, ders_kodu, vize_orani,final_orani, final, vize):

		self.ders_adi = ders_adi
		self.ders_kodu = ders_kodu
		self.final_orani = final_orani
		self.vize_orani = vize_orani
		self.vize = vize
		self.final = final


	def vize_guncelle(self,vize):

		self.vize = vize

	def final_guncele(self,final):

		self.final = final



	def __len__(self):

		return (self.final * float(self.final_orani)) + (self.vize * float(self.vize_orani))


	def __str__(self):

		self.a = self.final
		self.b = self.vize

		self.sonuc = float(self.final) * float(self.final_orani) + float(self.vize) * float(self.vize_orani)

		if int(self.final) == -1:

			self.a = "Vize Notu Girilmemiştir"

		if int(self.vize) == -1:

			self.b = "Final Notu Girilmemiştir"


		if (int(self.vize) == -1) | (int(self.final) == -1):

			self.sonuc = "Ders Sonuçlandırılmadı"

		self.verii =	""" 


    Ders adi         : {}

    Ders kodu        : {}

    Ders Final       : {}

    Ders Vize        : {}

    Ders Final oran  : {}

    Ders Vize oran   : {}

    Ders Ortalaması  : {}


		""".format(self.ders_adi, self.ders_kodu, self.a, self.b, self.final_orani, self.vize_orani, self.sonuc)
		
		return self.verii


