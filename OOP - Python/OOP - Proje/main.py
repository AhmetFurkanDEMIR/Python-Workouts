import os
from time import sleep as sl
import Class

global Ogrenciler

Ogrenciler = []

def ogrenci_ekle():

	os.system('cls' if os.name == 'nt' else 'clear')

	print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci ekle")

	ad_soyad = input("\n\n  Öğrenci adı, soyadı : ")
	tc_no = input("\n\n  Öğrenci T.C no : ")
	okul_no = input("\n\n  Öğrenci okul no : ")
	bolum = input("\n\n  Öğrenci Bölümü : ")
	ders_sayi = input("\n\n  Öğrenci aldığı ders sayısı : ")

	ders = []

	if int(ders_sayi) > 0:

		az = 1

		for i in range(0,int(ders_sayi)):

			print("\n\n --- Ders Ekle {} ---".format(az))

			ders_adi = input("\n\n    Ders adi : ")
			ders_kodu = input("\n\n    Ders kodu : ")
			ders_final_oran = input("\n\n    Ders final oranı (örn: 0.6) : ")
			ders_vize_oran = input("\n\n    Ders vize oranı (örn: 0.4) : ")

			ders.append(Class.Dersler(ders_adi, ders_kodu, ders_vize_oran, ders_final_oran, -1, -1))

	Ogrenciler.append(Class.Ogrenci(ad_soyad, tc_no, okul_no, int(ders_sayi), bolum, ders))

	input("\n\n   Ogrenci başarıyla eklenmiştir... Ana menü için Entere basınız.")


def ogrenci_sil():

	while True:

		os.system('cls' if os.name == 'nt' else 'clear')

		print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci sil")

		tc_no = input("\n\n  Silinecek öğrenci T.C No : ")

		kontrol = None

		for i in range(0,len(Ogrenciler)):

			if Ogrenciler[i].tc_no == tc_no:

				kontrol = True

				break


		if kontrol == None:

			son = input("\n\n   İstenilen ogrenci bulunamadi. Yeni bir arama için Y' harfine\n   Ana menüye dönmek için Enter'e basınız : ")

			if son == "Y" or son == "y":

				continue

			else:

				break

		elif kontrol == True:

			del Ogrenciler[i]

			input("\n\n   Ana menüye dönmek için Enter'e basınız. ")

			break

def ogrenci_listele():

	os.system('cls' if os.name == 'nt' else 'clear')

	print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Tüm Öğrenciler")

	print("\n\n Üniversitedeki toplam öğrenci sayiyi : {}".format(len(Ogrenciler)))

	for i in range(0, len(Ogrenciler)):

		Ogrenciler[i].ogrenci_bilgi()


	input("\n   Ana menüye dönmek için Enter'e basınız. ")


def ogrenci_bilgi():

	while True:

		os.system('cls' if os.name == 'nt' else 'clear')

		print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci bilgi")

		tc_no = input("\n\n  Öğrenci T.C No : ")

		kontrol = None

		for i in range(0,len(Ogrenciler)):

			if Ogrenciler[i].tc_no == tc_no:

				kontrol = True

				break


		if kontrol == None:

			son = input("\n\n   İstenilen ogrenci bulunamadi. Yeni bir arama için Y' harfine\n   Ana menüye dönmek için Enter'e basınız : ")

			if son == "Y" or son == "y":

				continue

			else:

				break

		elif kontrol == True:


			os.system('cls' if os.name == 'nt' else 'clear')

			print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci bilgi")

			Ogrenciler[i].ogrenci_bilgi()

			input("\n   Ana menüye dönmek için Enter'e basınız. ")

			break

				
def ogrenci_ders_bilgi():

	while True:

		os.system('cls' if os.name == 'nt' else 'clear')

		print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci ders bilgi")

		tc_no = input("\n\n  Öğrenci T.C No : ")

		kontrol = None

		for i in range(0,len(Ogrenciler)):

			if Ogrenciler[i].tc_no == tc_no:

				kontrol = True

				break


		if kontrol == None:

			son = input("\n\n   İstenilen ogrenci bulunamadi. Yeni bir arama için Y' harfine\n   Ana menüye dönmek için Enter'e basınız : ")

			if son == "Y" or son == "y":

				continue

			else:

				break

		elif kontrol == True:


			os.system('cls' if os.name == 'nt' else 'clear')

			print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci ders bilgi")

			print("\n\n   Öğrenci Adı, Soyadi : {}".format(Ogrenciler[i].ad_soyad))

			for z in range(0,Ogrenciler[i].ders_sayisi):

				print(Ogrenciler[i].dersler[z])

			input("\n   Ana menüye dönmek için Enter'e basınız. ")

			break


def final_vize():

	while True:

		os.system('cls' if os.name == 'nt' else 'clear')

		print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci Vize,Final")

		tc_no = input("\n\n  Öğrenci T.C No : ")

		kontrol = None

		for i in range(0,len(Ogrenciler)):

			if Ogrenciler[i].tc_no == tc_no:

				kontrol = True

				break


		if kontrol == None:

			son = input("\n\n   İstenilen ogrenci bulunamadi. Yeni bir arama için Y' harfine\n   Ana menüye dönmek için Enter'e basınız : ")

			if son == "Y" or son == "y":

				continue

			else:

				break

		elif kontrol == True:

			os.system('cls' if os.name == 'nt' else 'clear')

			print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci Vize,Final")

			kod = input("\n\n   Ders kodu = ")

			kontrol = None

			for z in range(0, int(Ogrenciler[i].ders_sayisi)):

				if Ogrenciler[i].dersler[z].ders_kodu == kod:

					kontrol = True
					break


			if kontrol == None:

				son = input("\n\n   İstenilen Ders bulunamadi. Yeni bir arama için Y' harfine\n   Ana menüye dönmek için Enter'e basınız : ")

				if son == "Y" or son == "y":

					continue

				else:

					break

			else:

				os.system('cls' if os.name == 'nt' else 'clear')

				print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi - Öğrenci Vize,Final")

				vizee = input("\n\n  Vize Notu (Vize Notu yok ise -1 giriniz)= ")

				finall = input("\n\n  Final Notu (Final Notu yok ise -1 giriniz)= ")

				Ogrenciler[i].dersler[z].vize_guncelle(vizee)
				Ogrenciler[i].dersler[z].final_guncele(finall)

				input("\n   Vize-Final notu değiştirilmiştir. Ana menüye dönmek için Enter'e basınız. ")

				break



def main():

	while True:

		os.system('cls' if os.name == 'nt' else 'clear')

		print("\n Necmettin Erbakan Üniversitesi Öğrenci Bilgi Sistemi")

		print("""

	1-) Öğrenci ekle

	2-) Öğrenci sil

	3-) Tüm Öğrenciler

	4-) Öğrenci bilgi

	5-) Öğrenci Vize-Final Ekle

	6-) Öğrenci ders sorgula

	Q-) Çıkış

	""")

		secim = input("    Seçim = ")

		if secim == "1":

			ogrenci_ekle()


		elif secim == "2":

			ogrenci_sil()

		elif secim == "3":

			ogrenci_listele()

		elif secim == "4":

			ogrenci_bilgi()

		elif secim == "5":
			
			final_vize()

		elif secim == "6":

			ogrenci_ders_bilgi()


if __name__ == "__main__":

	main()

