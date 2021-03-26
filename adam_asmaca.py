# Adam asmaca
# Ahmet Furkan DEMIR W/ Batuhan TURK

from random import randint as rn
import os

def print_adam(count):

	if count==0:

		print(""" 
		_______
		|     |
		|     O
		|    /|\\
		|     |
		|    / \\
		¯""")

	elif count==1:

		print(""" 
		_______
		|     |
		|     O
		|    /|\\
		|     |
		|      \\
		¯""")

	elif count==2:

		print(""" 
		_______
		|     |
		|     O
		|    /|\\
		|     |
		|     
		¯""")

	elif count==3:

		print(""" 
		_______
		|     |
		|     O
		|    /|\\
		|     
		|     
		¯""")

	elif count==4:

		print(""" 
		_______
		|     |
		|     O
		|     |\\
		|     
		|     
		¯""")

	elif count==5:

		print(""" 
		_______
		|     |
		|     O
		|     |
		|     
		|     
		¯""")

	elif count==6:

		print(""" 
		_______
		|     |
		|     O
		|     
		|     
		|     
		¯""")

	elif count==7:

		print(""" 
		_______
		|     |
		|     
		|     
		|     
		|     
		¯""")

	elif count==7:

		print(""" 
		_______
		|     
		|     
		|     
		|     
		|     
		¯""")


def __initGame__(ana_kelime):

	tahmin = []

	len_finish=0

	for i in ana_kelime:

		if i==" ":

			tahmin.append("  ")

		else:

			len_finish+=1
			tahmin.append(" _ ")

	return tahmin, len_finish



function_count=0

kelimeler = ["hızlı araba", "güzel ev", "batuhan oğulgaymış", "şevki vurduranoğlu"]
ana_kelime = kelimeler[rn(0,3)]
cizgi=len(ana_kelime)
game_finish=0
tahmin, len_finish = __initGame__(ana_kelime)

print("\033[92m")

while True:

	os.system('cls' if os.name == 'nt' else 'clear')
	print_adam(function_count)
	print("\033[1;34m")
	print("  Kelime :  ", end="")

	for i in tahmin:

		print(" {} ".format(i),end="")

	harf=str(input("\n\n  Harf giriniz : "))

	flag=0

	for i, harf_cizgi in enumerate(ana_kelime):

		if harf_cizgi==harf:

			print("\033[92m")
			game_finish+=1

			tahmin[i]=harf

			flag=1

	if flag==0:

		function_count+=1

		print("\033[31m")

	if game_finish==len_finish:

		print("\033[92m")
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print("\n  Kelime :  ", end="")

		for i in tahmin:

			print(" {} ".format(i),end="")

		sc = input("\n\n  Tebrikler oyunu kazandiniz :), yeni oyun icin (E/e, H/h): ")


		if sc=="H" or sc=="h":

			os.system('cls' if os.name == 'nt' else 'clear')
			quit()

		else:

			function_count=0

			kelimeler = ["hızlı araba", "güzel ev", "batuhan oğulgaymış", "şevki vurduranoğlu"]
			ana_kelime = kelimeler[rn(0,3)]
			cizgi=len(ana_kelime)
			game_finish=0
			tahmin, len_finish = __initGame__(ana_kelime)

	elif function_count==8:

		os.system('cls' if os.name == 'nt' else 'clear')
		
		print("\n  Kelime :  ", end="")

		for i in ana_kelime:

			print(" {} ".format(i),end="")

		sc = input("\n\n  Malesef oyunu kaybettiniz, yeni oyun icin (E/e, H/h): ")


		if sc=="H" or sc=="h":

			os.system('cls' if os.name == 'nt' else 'clear')
			quit()

		else:

			function_count=0

			kelimeler = ["hızlı araba", "güzel ev", "batuhan oğulgaymış", "şevki vurduranoğlu"]
			ana_kelime = kelimeler[rn(0,3)]
			cizgi=len(ana_kelime)
			game_finish=0
			tahmin, len_finish = __initGame__(ana_kelime)