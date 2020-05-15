import sqlite3
import os
import hashlib as hasher
import login

def veri_tabani():

	db = sqlite3.connect("veri_tabani.db")

	imlec = db.cursor()

	imlec.execute("CREATE TABLE IF NOT EXISTS Login (Id TEXT, Sifre TEXT)")

	imlec.execute("CREATE TABLE IF NOT EXISTS Data (Hasta_adi_soyadi TEXT, Hasta_yas INT, Hasta_tc TEXT, Yatırılıs_tarihi TEXT, Cikis_tarihi TEXT)")

	db.commit()

	return imlec, db


def main():

	while True:

		os.system("clear")

		imlec, db = veri_tabani()

		print(""" 

  DEMIR Hastane Otomasyonu

    1-) Personel girişi

    2-) Yeni personel ekle

    Q-) Çıkış

			""")


		secim = input("\n     Seçim = ")


		if secim == "1":

			kontrol = login.kullanici_giris(imlec, db)


			if kontrol == 1:

				login.main(imlec, db)

		if secim == "2":


			login.kullanici_ekle(imlec, db)


		if secim == "q" or secim == "Q":

			quit()



main()