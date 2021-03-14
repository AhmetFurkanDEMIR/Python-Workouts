
"""  Yapay Sinir Ağları örnek 2 """

from numpy import exp, array, random, dot

egitim_girisler = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
egitim_cikislar = array([[0, 1, 1, 0]]).T

random.seed(1)

agirliklar = 2 * random.random((3, 1)) - 1

for iterasyon in range(10000):
    cikis = 1 / (1 + exp(-(dot(egitim_girisler, agirliklar))))
    agirliklar += dot(egitim_girisler.T, (egitim_cikislar - cikis) * cikis * (1 - cikis))

print(1 / (1 + exp(-(dot(array([1, 0, 0]), agirliklar)))))

# ------------- son -------------