import time
import numpy as np

def main(sifreee, veri):

	try:

		sz = {"A":"1",
			  "Z":"2",
			  "B":"3",
			  "G":"4",
			  "C":"5",
			  "D":"6",
			  "E":"7",
			  "H":"8",
			  "F":"9",
			  "K":"0"}

		def de(data, sz):

			liste = []


			for i in data:


				temp = []

				for z in i:

					a = ""

					for k in z:

						a += sz[k]

					temp.append(a)

				liste.append(temp.copy())

			return liste


		file = open(veri, "r+")

		data = file.read().split("-")

		boyut = data[1].split(",")

		sifre = data[2]

		if sifre == sifreee:

			data0 = data[0].split("\n")

			datax = []

			for i in data0:

				datax.append(i.split(","))

			x = 0

			for i in datax:

				for y in range(0,3):

					try:

						datax[x][y] = i[y]

					except:
						pass


			datax = de(datax, sz)



			veri = np.zeros((int(boyut[0]) , int(boyut[1]) , int(boyut[2])), dtype="float64")

			x = 0

			y = -1

			for i in datax:

				y += 1

				try:

					veri[x][y] = i

				except:

					pass

				if y == int(boyut[1]) - 1:

					x += 1

					y = -1

			from scipy.misc import toimage
			toimage(veri).show()

			return 0

		else:

			return -5

	except:

		return -3
