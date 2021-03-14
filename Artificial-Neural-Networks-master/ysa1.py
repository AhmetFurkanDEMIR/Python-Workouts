""" Yapay Sinir Ağları örnek 1 """

from numpy import exp, array, random, dot

class YapaySinirAglariCKA():
    def __init__(self):
        # rastgele sayý
        random.seed(1)

        # 3 giriş bir çikis 
        # -1'den 1'e rastgele ağırlık değerleri
        self.agirliklar = 2 * random.random((2, 1)) - 1

    # Sigmoid aktivasyon fonksiyonu
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # Sigmoid aktivasyon fonksiyonunun türevi
    def __sigmoid_turev(self, x):
        return x * (1 - x)

    # eğitimin - tamamlanması
    def egit_beni(self, egitim_girisler, egitim_cikislar, toplam_iterasyon):
        for iterasyon in range(toplam_iterasyon):
            cikis = self.besle(egitim_girisler)

            # Hata hesaplanıyor...
            hata = egitim_cikislar - cikis

            # ayar değeri
            ayar = dot(egitim_girisler.T, hata * self.__sigmoid_turev(cikis))

            # Ağırlık ayarlama..
            self.agirliklar += ayar

    # ileri besleme/test/uyg.
    def besle(self, giris):
        return self.__sigmoid(dot(giris, self.agirliklar))

if __name__ == "__main__":

    #YSA kurulumu...
    ysa = YapaySinirAglariCKA()

    print("Başlangıç ağırlıkları (rastgele): ")
    print(ysa.agirliklar)

    # Eðitim seti þeyi...
    egitim_girisler = array([[1, 0], [1, 1], [0, 0]])
    egitim_cikislar = array([[1, 1, 0]]).T

    # ilgili iterasyon degeri kadar egitim
    ysa.egit_beni(egitim_girisler, egitim_cikislar, 10000)

    print("Eğitim sonrası ağırlıklar: ")
    print(ysa.agirliklar)

    # Test aşaması
    print("Yeni test girişleri için çıkış kaç ki lan?: ")
    print(ysa.besle(array([0, 1])))
   
# ------------- son -------------
