import os
import hashlib as hasher
from time import sleep as sl
import datetime

def liste(imlec,db):

	os.system("clear")

	imlec.execute("SELECT * FROM Data")

	Id = imlec.fetchall()

	print("\n  DEMIR Hastane Otomasyonu - Tüm Hastalar\n\n")

	print("  |       Ad,Soyad          |    Yaş    |      T.C      |      Hastaneye yatırılış tarihi      |   Hastaneden çıkış tarihi   |")
	print("  ----------------------------------------------------------------------------------------------------------------------\n")

	try:

		for i in Id:

			print("  |  ",i[0],end="")

			print(" "*(22-len(i[0])),end="|")

			print("   ",i[1],end="")

			print(" "*(7-len(str(i[1]))),end="|")

			print(" ",i[2],end="")

			print("  ",end="|")

			print("          ",i[3],end="")

			print("           ",end="|")

			print("      ",i[4],end="")

			print("         ",end="")

			print("")


	except:

		pass


	input("\n\n   Ana menüye dönmek için Enter'e basınız. ")


def bilgi(imlec,db):

	os.system("clear")

	imlec.execute("SELECT * FROM Data")

	Id = imlec.fetchall()

	print("\n  DEMIR Hastane Otomasyonu - Hasta Bilgileri\n\n")

	tc = input("   Hasta T.C = ")

	kontrol = None

	for i in Id:

		if tc == i[2]:

			os.system("clear")

			kontrol = True

			print("\n  DEMIR Hastane Otomasyonu - Hasta Bilgileri\n\n")

			print("  |       Ad,Soyad          |    Yaş    |      T.C      |      Hastaneye yatırılış tarihi      |   Hastaneden çıkış tarihi   |")
			print("  ----------------------------------------------------------------------------------------------------------------------\n")

			print("  |  ",i[0],end="")

			print(" "*(22-len(i[0])),end="|")

			print("   ",i[1],end="")

			print(" "*(7-len(str(i[1]))),end="|")

			print(" ",i[2],end="")

			print("  ",end="|")

			print("          ",i[3],end="")

			print("           ",end="|")

			print("   ",i[4],end="")

			print(" "*(8-len(i[4])),end="")

			print("")

			input("\n\n   Ana menüye dönmek için Enter'e basınız. ")


			break


	if kontrol == None:

		print("\n\n   Sistemimizde istenilen hasta bulunmamaktadır.")

		input("\n\n   Ana menüye dönmek için Enter'e basınız. ")


def kayit(imlec, db):

	while True:

		os.system("clear")

		print("\n  DEMIR Hastane Otomasyonu - Hasta Kayıt\n\n")

		isim = input("   Hasta adı = ")

		if len(isim) <= 2 or len(isim) > 20:

			input("\n\n    Hasta adı istenilen uzunlukta değil\n    Ana menüye dönmek için Enter'e basınız")

			break

		print("")

		yas = input("   Hasta Yaşı = ")

		if len(yas) < 1 or len(yas) > 3:

			input("\n\n    Hatalı hasta yaşı. Ana menüye dönmek için Enter'e basınız")

			break

		print("")

		tc = input("   Hasta T.C = ")
		
		if len(tc) != 11:

			input("\n\n    Hatalı hasta T.C. Ana menüye dönmek için Enter'e basınız")

			break

		an = datetime.datetime.now()

		yıl = an.year

		ay = an.month

		gün = an.day

		saat = str(an.hour) + ":" + str(an.minute)
        
		tarih = str(gün) + "/" +str(ay) + "/" + str(yıl) + " - " + saat

		cikis = " Hastanede"
		imlec.execute("INSERT INTO Data VALUES(?,?,?,?,?)",(isim,yas,tc,tarih,cikis))

		db.commit()

		os.system("clear")

		print("\n  DEMIR Hastane Otomasyonu - Hasta Kayıt\n\n")

		print("    Hasta kaydı yapılmıştır. Yeni hasta kaydı için Y 'ye\n    Ana menüye dönmek için Enter 'e basınız",end="")

		secim = input(" = ")

		if secim == "y" or secim == "Y":

			continue

		else:

			break


def hasta_cıkıs(imlec, db):

	while True:

		os.system("clear")

		imlec.execute("SELECT * FROM Data")

		Id = imlec.fetchall()

		print("\n  DEMIR Hastane Otomasyonu - Hasta Çıkış\n\n")

		tc = input("   Hasta T.C = ")

		kontrol = None

		for i in Id:

			if tc == i[2]:

				kontrol = True

				if i[4] != " Hastanede":

					print("\n\n   Bu Kişi hastanede bulunmamaktadır.")

					print("    Yeni hasta çıkışı için Y 'ye\n    Ana menüye dönmek için Enter 'e basınız",end="")

					secim = input(" = ")

					if secim == "y" or secim == "Y":

						continue

					else:

						break


				secim = input("\n\n    Hasta çıkışını onaylıyormusun (Y/N) = ")

				if secim == "Y" or secim == "y":

					an = datetime.datetime.now()

					yıl = an.year

					ay = an.month

					gün = an.day

					saat = str(an.hour) + ":" + str(an.minute)
        
					tarih = str(gün) + "/" +str(ay) + "/" + str(yıl) + " - " + saat

					imlec.execute("UPDATE Data SET Cikis_tarihi=? WHERE Hasta_tc=?",(tarih,tc))

					db.commit()

					os.system("clear")

					print("\n  DEMIR Hastane Otomasyonu - Hasta Çıkış\n\n")

					print("    Hasta Çıkışı yapılmıştır. Yeni hasta çıkışı için Y 'ye\n    Ana menüye dönmek için Enter 'e basınız",end="")

					secim = input(" = ")

					if secim == "y" or secim == "Y":

						continue

					else:

						break


		if kontrol==None:

			print("\n\n   Bu Kişi hastanede bulunmamaktadır.")

			print("    Yeni hasta çıkışı için Y 'ye\n    Ana menüye dönmek için Enter 'e basınız",end="")

			secim = input(" = ")

			if secim == "y" or secim == "Y":

				continue

			else:

				break

		break


def main(imlec,db):

	while True:

		os.system("clear")

		print(""" 

  DEMIR Hastane Otomasyonu

   1-) Tüm hastalar

   2-) Hasta bilgileri

   3-) Hasta kaydı

   4-) Hasta çıkışı

   A-) Ana menü

   Q-) Çıkış 

	""")

		secim = input("  Seçiminiz = ")


		if secim == "1":

			liste(imlec,db)

		elif secim == "2":

			bilgi(imlec,db)


		elif secim == "3":

			kayit(imlec,db)


		elif secim == "4":

			hasta_cıkıs(imlec,db)

		elif secim == "A" or secim == "a":

			return 0

		elif secim == "Q" or secim == "q":

			quit()


def kullanici_ekle(imlec, db):

	os.system("clear")

	print("\n  DEMIR Hastane Otomasyonu - Yeni Personel Ekle")

	idd = input("\n\n    ID = ")

	imlec.execute("SELECT * FROM Login")

	Id = imlec.fetchall()

	kontrol = True

	for i in Id:

		if i[0] == idd:

			kontrol = False


	if kontrol == True:

		if len(idd) >= 6 and len(idd) <= 14:

			sifre = input("\n\n    Sifre = ")

			sifrea = input("\n\n    Sifre Tekrar = ")

			if sifre == sifrea:

				if len(sifre) >= 6 and len(sifre) <= 14:
				
					sifreleyici = hasher.sha256()
					sifreleyici.update(sifre.encode("utf-8"))
					hash = sifreleyici.hexdigest() 
				

					imlec.execute("INSERT INTO Login VALUES(?,?)",(idd,hash))

					db.commit()

				else:

					input("\n\n     Sifre 5 < x < 15 arasında olmalıdır,\n    Ana menüye dönmek için Enter'e basınız.")

			else:
			
				input("\n\n     Sifreler eşleşmemektedir,\n    Ana menüye dönmek için Enter'e basınız.")


		else:

			input("\n\n     Kullanıcı adı 5 < x < 15 arasında olmalıdır,\n    Ana menüye dönmek için Enter'e basınız.")

	if kontrol == False:

		input("\n\n     Bu kullanıcı adı daha önceden alınmıştır,\n    Ana menüye dönmek için Enter'e basınız.")


def kullanici_giris(imlec, db):

	imlec.execute("SELECT * FROM Login")

	Id = imlec.fetchall()

	os.system("clear")

	print("\n  DEMIR Hastane Otomasyonu - Personel Giriş")

	idd = input("\n\n    ID = ")

	sifre = input("\n\n    Sifre = ")

	sifreleyici = hasher.sha256()
	sifreleyici.update(sifre.encode("utf-8"))
	hash = sifreleyici.hexdigest() 

	kontrol = None

	for i in Id:

		if i[0] == idd and i[1] == hash:

			kontrol = True


	if kontrol == True:

		print("\n\n     Giriş başarılı...")
		sl(5)

		return 1

	else:

		input("\n\n     Kullanıcı adı veya sifre hatalı,\n    Ana menüye dönmek için Enter'e basınız.")

		return 0