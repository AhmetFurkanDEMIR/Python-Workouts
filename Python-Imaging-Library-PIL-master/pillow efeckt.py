#! /usr/bin/python
# -*- coding:utf-8 -*-

import os
import time
from PIL import Image,ImageFilter

os.system("clear")
print("\n\n   DEMIR effect ")
print("\n\n   effect yapmak istediğiniz resim {} dizininde olması gerek.".format(os.getcwd()))
input("\n   Devam etmek için Enter tuşuna basınız. ")

while True:

	os.system("clear")
	print("\n\n   DEMIR effect ")

	ad = input("\n\n   {} dizininde bulunan,\n   resim adı ve uzantısı (dosya adı.uzantı) = ".format(os.getcwd()))
	
	try:
		
		dosya = Image.open(ad)
		dosya.show()

	
	except FileNotFoundError:
		
		os.system("clear")
		print("\n\n   DEMIR effect ")
		print("\n\n   HATA!!\n   {} adlı dosya bulunamadı".format(ad))
		input("\n\n   Yeni bir dosya adı girmek için Enter e basınız ")
		continue

	except AttributeError:

		os.system("clear")
		print("\n\n   DEMIR effect ")
		print("\n\n   HATA!!\n   Lütfen dosya adı giriniz")
		input("\n\n   Yeni bir dosya adı girmek için Enter e basınız ")
		continue

	print("\n  ",dosya.format,dosya.size,dosya.mode)

	input("\n\n   Devam etmek icin Enter'e basınız ")

	while  True:
		
		os.system("clear")
		print("""\n\n   DEMIR effect 

  1) Sansürle / Bulanıklaştır X

  2) Sansürle / Bulanıklaştır 2X

  3) Kalemle çizgi

  4) Canlandırma / Renklendirme

  5) Boyayarak Eskitme X

  6) Boyayarak Eskitme 2X

  7) Canlandırma

	""")

		try:
			al = int(input("   effect türü = "))

		except ValueError:

			print("\n\n   Lütfen istenilen değer aralığındaki ( 0 < x < 8 ) sayıları giriniz")
			input("\n\n   Devam etmek icin Enter'e basınız ")
			continue

		if al>=1 and al<=7:
			

			if al == 1:
				yeni=dosya.filter(ImageFilter.SMOOTH)

			elif al == 2:
				yeni=dosya.filter(ImageFilter.BLUR)

			elif al == 3:
				yeni=dosya.filter(ImageFilter.CONTOUR)

			elif al == 4:
				yeni=dosya.filter(ImageFilter.DETAIL)

			elif al == 5:
				yeni=dosya.filter(ImageFilter.EDGE_ENHANCE)

			elif al == 6:
				yeni=dosya.filter(ImageFilter.EDGE_ENHANCE_MORE)

			elif al == 7:
				yeni=dosya.filter(ImageFilter.SHARPEN)

			print("\n\n   işlem gerçekleştiriliyor...")	
			time.sleep(2)

			yeni.show()
			yeni.save("yeni_DEMIR_effect.png")

			i = 0

			while True:
				
				os.system("clear")
				
				print("\n\n   DEMIR effect ")
				print("\n\n   Resminiz {} adresine kaydedilmiştir.".format(os.getcwd()))
				print("\n\n   Resim üzerinde tekrar işlem yapmak için '1' e,\n   yeni bir Resim üzerinde işlem yapmak için '2' ye,\n   Uygulamadan çıkmak için '3' e basınız ")

				alr = int(input("\n\n   Seciminiz = "))

				if alr == 1:
					
					i = -1
					break

				elif alr == 2:
					
					i=0
					break

				elif alr ==3:

					quit()

			if i == 0:
				break