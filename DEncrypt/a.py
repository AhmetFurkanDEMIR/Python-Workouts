from PIL import Image
from numpy import asarray
import numpy as np

def main(resim, sifre):

	sz = {"1":"A",
		  "2":"Z",
		  "3":"B",
		  "4":"G",
		  "5":"C",
		  "6":"D",
		  "7":"E",
		  "8":"H",
		  "9":"F",
		  "0":"K"}

	def de(data, liste, sz):

		x = -1

		y = 0

		while True:

			y+=1

			listee = []

			for i in data[x][y]:

				a = ""

				for z in str(int(i)):

					a += sz[z]

				listee.append(a)
			
			liste[x][y] = listee.copy()

			if y == data.shape[1]-1:

				y = -1

				x += 1

			if x == data.shape[0]-1:

				return liste

				break


	# load the image
	image = resim
	# convert image to numpy array
	data = asarray(image)

	x = 0

	y = -1

	liste = data.tolist()
		
	liste = de(data, liste, sz)

	boyut0 = len(liste)

	boyut = data.shape

	a = 0

	with open('Sifreli/veri.demir', 'w') as outfile:

		try:

			for i in liste:

				for z in i:

					kontrol = -1

					for x in z:

						kontrol+=1

						outfile.write(x)
						
						if kontrol != 2:
							
							outfile.write(",")

					outfile.write("\n")

		except:

			pass


		outfile.write("-")
		outfile.write("{},{},{}".format(boyut[0], boyut[1], boyut[2]))
		outfile.write("-")
		outfile.write(str(sifre))

    

