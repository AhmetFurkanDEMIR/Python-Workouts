# Ad,Soyad = Ahmet Furkan DEMIR , No = 19010011019

"""

Proje ile ilgili açıklama


Verileri sakladığım dosyalar:

1) 19010011019.demir (Kullanıcı işlemleri)

2) 19010011019.txt (Araçlarla ilgili veriler)


* koleksiyon veri tiplerinden: Sözlük ve Listeleri kullandım.


İstediğiniz Fonksiyonlar:

Ekleme fonksiyonu = Tsk sınıfına ait arac_temin fonksiyonudur. *

Güncelleme fonksiyonu = Tsk sınıfına ait arac_güncelle fonksiyonudur. *

Arama fonksiyonu = Tsk sınıfına ait arac_ara fonksiyonudur. *

Silme fonksiyonu = Tsk sınıfına ait arac_hurda fonksiyonudur. *


Kendi fonksiyonlarım:

Mevcut araçları görüntüle = arac_görüntüle fonksiyonu. 

Mühimmat temin = Tsk sınıfına ait mühimmat_temin fonksiyonu.

Personel ayarları = Tsk sınıfına ait degistir fonksiyonu.

Yeni araç kaydı = Tsk sınıfına ait kayit fonksiyonu.


** Kod main(2016. satır) fonksiyonundan başlamaktadır

Personel giriş = giris fonksiyonu

Personel ekle = kullanici_ekle fonksiyonu

***
islem fonksiyonu, fonksiyon objesi döndüren fonksiyondur.
döndürdüğü fonksiyonlar personel ekle ve personel giriş fonksiyonlarıdır.
*** 
istenilen iç içe fonksiyonlar (nested / inner functions) personel ekle, ve personel giriş fonksiyonlarının 
Başında dosya işlemleri için yapılmaktadır(parcala fonksiyonları), iki kez.
parcala fonksiyonları iterable obje döndüren fonksiyonlardır(generator fonksiyon)

personel ekle ve personel giriş fonksiyonlarıda iç içe fonksiyonlardır.
***

***
Otomasyonun geri kalan bölümleri Tsk sınıfı içerisindedir.
***

"""

import os # ekran temizleme ve işletim sistemi öğrenme
from time import sleep as sl # kodu bekletme
import shutil # dosya kopyalama
import datetime # tarih,saat vb..

class Tsk(): # Tsk sınıfı

    def __init__(self,ida,sifre): # giriş fonksiyonu

        # sınıfın aldığı parametreler tanımlanıyor

        self.idaa = ida # Giriş yapan personelin kullanıcı adı

        self.sifre = sifre # Giriş yapan personelin şifre

        self.giris() # giris fonksiyonuna ilerler

    def giris(self): # giriş yapan personelin ana menüsü

        while True:

            self.hazirlik() # hazirlik fonksiyonuna ilerler

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n\n   TSK | Kara Araçları Envanter Otomasyonu - Personel : {} -".format(self.idaa))

            print("\n\n     1) Mevcut araçları görüntüle")

            print("\n     2) ID ile araç ara")

            print("\n     3) Araç temin et (Üret / Satın al)")

            print("\n     4) Mühimmat temin et (Üret / Satın al)")

            print("\n     5) Araç hurdaya çıkart")

            print("\n     6) Yeni araç kaydı")

            print("\n     7) Personel ayarları")

            print("\n     G) Giriş menüsüne geri dön")

            print("\n     Q) Çıkış")


            self.secim = input("\n\n      Seçim = ") # yapacağınız işlemi alır

            # klavyeden girdiğiniz tuşlara göre ilerler.

            if self.secim == "1":

                self.arac_görüntüle()

            elif self.secim == "2":

                self.arac_ara()

            elif self.secim == "3":

                self.arac_temin()

            elif self.secim == "4":

                self.mühimmat_temin()

            elif self.secim == "5":

                self.arac_hurda()

            elif self.secim == "6":

                self.kayit()

            elif self.secim == "7":

                self.degistir()

            elif self.secim == "G" or self.secim == "g":

                main()

            elif self.secim == "Q" or self.secim == "q":

                quit()


    def hazirlik(self):

        try:

            self.file = open("19010011019.txt","r+",encoding="utf-16") # r+ kipinde dosyayı açar


        # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
        except FileNotFoundError:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")

            quit()


        self.idd = [] # içindeki verileri parçalayacağım listeler

        self.tasit_ad = []

        self.tür = []

        self.adet = []

        self.mühimmat = []

        self.üreten_ülkeler = []

        
        for self.i in self.file: # dosya içindeki verileri i değişkenine aktarıp döngü başlatıyorum.

            self.i = self.i[:-1] # son satırdaki \n sildim

            self.gecici = self.i.split(",") # virgillerden ayırıyor, geriye liste döndürür.

            self.idd.append(self.gecici[0]) # listenin 0. elemanı araçların id si

            self.tasit_ad.append(self.gecici[1]) # listenin 1. elemanı taşıtların adı

            self.tür.append(self.gecici[2]) # listenin 2. elemanı araçlar hakkında kısa bilgi

            self.adet.append(int(self.gecici[3])) # listeniin 3. elemanı araçların envanterde kaçar adet olduğu

            try: # bazı araçlarda entagre silah yok dolayısıyla mühimmatıda yok, o yüzden int veri tipine dönüşemiyor           

                self.mühimmat.append(int(self.gecici[4])) # eğer silahı varsa mühhimatıda var

            except ValueError:

                self.mühimmat.append(self.gecici[4]) # yoksa direk str olarak kaydediyoruz

            self.üreten_ülkeler.append(self.gecici[5]) # aracın hangi ülkede üretildiği

            self.veri = {"ID":self.idd,
                        "Araç ad":self.tasit_ad,  # tüm verileri sözlüğe aktarıyorum.
                        "Tür":self.tür,
                        "Adet":self.adet,
                        "Mühimmat":self.mühimmat,
                        "Üreten ülkeler":self.üreten_ülkeler}



    def arac_görüntüle(self):

        # araçların hepsini yazdırdım.

        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n\n    TSK  |  Kara Araçları Envanter Otomasyonu - Mevcut araçları görüntüle")

        
        print("\n\n    ID     |          Araç ad           |                Tür             |    Adet     |  Mühimmat   |    Üreten ülkeler")

        print("\n  -------------------------------------------------------------------------------------------------------------------------")

        # tüm veriler aynı uzunlukta olmadığı için bazı ayarlar yaptım (görüntüde bozukluklar oluyordu)

        # bu fonksiyonda listeleri kullandım, geri kalan diğer fonksiyonlarda sözlükleri kullanacağım.

        for self.i in range(0,len(self.tasit_ad)):

            print("\n   %.4d   " % int(self.veri["ID"][self.i]),end="")

            print(" |",end="")

            print("  ",self.tasit_ad[self.i],end="")

            self.a = 25 - len(self.tasit_ad[self.i])

            for self.c in range(0,self.a):

                print(" ",end="")


            print("|",end="")


            print("  ",self.tür[self.i],end="")

            self.a = 29 - len(self.tür[self.i])

            for self.c in range(0,self.a):

                print(" ",end="")

            print("|",end="")

            print("  ",self.adet[self.i],end="")

            self.a = 10 - len(str(self.adet[self.i]))

            for self.c in range(0,self.a):

                print(" ",end="")

            print("|",end="")

            if self.mühimmat[self.i] == "*":

                self.c = "Silahsız"

            else:

                self.c = self.mühimmat[self.i]


            print("  ",self.c,end="")

            self.a = 10 - len(str(self.c))

            for self.c in range(0,self.a):

                print(" ",end="")

            print("|",end="")   

            print("  ",self.üreten_ülkeler[self.i],end="")

            self.a = 10 - len(self.üreten_ülkeler[self.i])

            for self.c in range(0,self.a):

                print(" ",end="")

            print("\n")

        input("\033[92m"+"\n\n    Geri dönmek için Enter 'e basınız. "+"\033[39m")



    def arac_ara(self):

        # girilen ID ye göre aracın özellikleri yazdırılır

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - ID ile araç ara")

            try:

                self.id = int(input("\n\n     Araç ID = "))

            except ValueError: # ID yerine str veri girerseniz bu buloğa girer

                self.a = input("\033[31m"+"\n\n      ID olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break

            # Girilen araç ID si sistemde mevcutmu kontrolü
            self.indis = -1

            self.kontrol = False

            for self.i in self.veri["ID"]:

                self.indis += 1

                if self.i == str(self.id):

                    self.kontrol = True

                    break
        

            if self.kontrol == True:

                if self.veri["Mühimmat"][self.indis] == "*":

                    self.c = "Silahsız"

                else:

                    self.c = self.veri["Mühimmat"][self.indis]

                os.system('cls' if os.name == 'nt' else 'clear')

                # istenilen aracın özelliklerine detaylı inceleme

                print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - ID ile araç ara")

                print("""


    ID               |  {}

   ------------------------------------------------------------------

    Araç adı         |  {}

   ------------------------------------------------------------------

    Tür              |  {}

   ------------------------------------------------------------------

    Adet             |  {}

   ------------------------------------------------------------------

    Mühimmat         |  {}

   ------------------------------------------------------------------

    Üretildiği ülke  |  {}

   ------------------------------------------------------------------

                """.format(self.id,self.veri["Araç ad"][self.indis],self.veri["Tür"][self.indis],self.veri["Adet"][self.indis],self.c,self.veri["Üreten ülkeler"][self.indis]))
                    # sözlükteki istenilen aracın verileri yazdırılıyor

            else: # Id bulunamadıysa girer

                self.a = input("\033[31m"+"\n\n      ID Bulunamadı. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break


            self.a = input("\033[92m"+"\n\n      Geri dönmek için herhangi bir tuşa, yeni arama için T' harfine basınız "+"\033[39m") # işlem sonunda karşınıza çıkan seçenek

            if self.a == "t" or self.a == "T":

                continue

            break



    def arac_güncelle(self):

        # arac_temin, mühimmat_temin, arac_hurda ve kayit adlı fonksiyonlarda yapılan işlemlerin sonucunda verileri güncellemek için bu fonksiyona ilerlenir.

        # dosya w kipinde açılır içindekiler silinir, sözlük dosyaya yazılır.

        # herhangi bir hata oluşursa diye eski dosya log_dir adlı klasöre kaydedilir.
        shutil.copy2("19010011019.txt", "log_dir/arac_veri_eski")

        try:

            self.file = open("19010011019.txt","w",encoding="utf-16")

        # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
        except FileNotFoundError:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")

            quit()

        # sözlüğün içindeki verileri yazar.
        for self.i in range(0,len(self.veri["Araç ad"])):

            self.file.write(str(self.veri["ID"][self.i]))

            self.file.write(",")

            self.file.write(self.veri["Araç ad"][self.i])

            self.file.write(",")

            self.file.write(self.veri["Tür"][self.i])

            self.file.write(",")

            self.file.write(str(self.veri["Adet"][self.i]))

            self.file.write(",")

            self.file.write(str(self.veri["Mühimmat"][self.i]))

            self.file.write(",")

            self.file.write(self.veri["Üreten ülkeler"][self.i])

            self.file.write("\n")


        self.file.close() # dosya kapatılır.

        self.hazirlik() # hazirlik fonksiyonuna ilerlenir, dosya tekrar açılır ve sözlük güncellenir.



    def arac_temin(self):

        # mevcut araçlardan satın almak veya üretmek.

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç temin et")

            try:

                self.id = int(input("\n\n     Temin etmek istediğiniz araç ID = ")) # hangi araçtan temin edilecek

            except ValueError: # int veri kontrolü

                self.a = input("\033[31m"+"\n\n      ID olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break


            # ID girilen araç sistemdemi diye kontrol edilir.
            self.indis = -1

            self.kontrol = False

            for self.i in self.veri["ID"]:

                self.indis += 1

                if self.i == str(self.id):

                    self.kontrol = True

                    break

                
            # Sistemdeyse kod blokları ilerlemeye devam eder.
            if self.kontrol == True:

                os.system('cls' if os.name == 'nt' else 'clear')

                print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç temin et")

                print("\n\n     Araç ad : {} ".format(self.veri["Araç ad"][self.indis]))


                try:

                    self.adet = int(input("\n\n     Kaç adet araç temin edilecek (tek seferde 10 adet alınabilir) = ")) # temin edilecek miktarın kontrolü

                # adet INT kontrolü
                except ValueError:

                    self.a = input("\033[31m"+"\n\n      Adet olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                    if self.a == "t" or self.a == "T":

                        continue

                    break

                # maximum araç alma kontrolü
                if self.adet > 0 and self.adet <= 10: # adet kontrolü

                    self.adett = self.adet

                    # aracın üretildiği konuma göre , satın alınır veya üretilir.

                    if self.veri["Üreten ülkeler"][self.indis].lower() == "türkiye":

                        self.veri["Adet"][self.indis] += self.adet

                        self.arac_güncelle()

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç temin et")

                        input("\033[92m"+"\n\n      İstediğiniz araçtan {} adet üretildi, geri dönmek için Enter 'e basınız".format(self.adett)+"\033[39m")

                    else:

                        self.veri["Adet"][self.indis] += self.adet

                        self.arac_güncelle()

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç temin et")

                        input("\033[92m"+"\n\n      İstediğiniz araçtan {} adet satın alındı, geri dönmek için Enter 'e basınız".format(self.adett)+"\033[39m")


                else: # adet hatalı girilirse

                    self.a = input("\033[31m"+"\n\n      Hatalı değer aralığı. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                    if self.a == "t" or self.a == "T":

                        continue

                    break


            else: # ID bulunamazsa

                self.a = input("\033[31m"+"\n\n      ID Bulunamadı. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break


            break



    def mühimmat_temin(self):

        # ID si girilen aracın entegre silahı varsa mühimmat alınabilir.

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n\n    TSK  |  Kara Araçları Envanter Otomasyonu - Mühimmat temin et")


            try:

                self.id = int(input("\n\n     Mühimmat temin etmek istediğiniz araç ID = "))

            except ValueError: # ID int kontrol

                self.a = input("\033[31m"+"\n\n      ID olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break


            # aracın sisemde olma kontrolü
            self.indis = -1

            self.kontrol = False

            for self.i in self.veri["ID"]:

                self.indis += 1

                if self.i == str(self.id):

                    self.kontrol = True

                    break

                

            if self.kontrol == True:

                if self.veri["Mühimmat"][self.indis] != "*":

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Mühimmat temin et")

                    print("\n\n     Mühimmat alınacak araç adı : {} ".format(self.veri["Araç ad"][self.indis]))

                    try:

                        self.adet = int(input("\n\n     Mühimmat adet (Tek seferde en fazla {} adlı aracın adetinin,\n\n     iki katı kadar mühimmat alabilirsiniz. Alabileceğiniz maksimum mühimmat : {}) = ".format(self.veri["Araç ad"][self.indis],self.veri["Adet"][self.indis]*2)))


                    except ValueError: # mühimmat adet int kontrolü

                        self.a = input("\033[31m"+"\n\n      Adet olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break

                    if self.adet > 0 and self.adet <= self.veri["Adet"][self.indis]*2:

                        self.adettt = self.adet

                        self.veri["Mühimmat"][self.indis] += self.adet # arcta mühümmat güncellemesi yapılır

                        self.arac_güncelle() # güncelle fonksiyonuna ilerler

                        # aracın üretildiği bölgeye göre, mühhimat üretilir veya satın alınır

                        if self.veri["Üreten ülkeler"][self.indis].lower() == "türkiye":

                            self.a = input("\033[92m"+"\n\n      {} adet mühimmat üretildi.\n     (Geri dönmek için herhangi bir tuşa,\n     tekrar Mühimmat almak için T' harfine basınız) ".format(self.adettt)+"\033[39m")

                        else:

                            self.a = input("\033[92m"+"\n\n      {} adet mühimmat satın alındı.\n     (Geri dönmek için herhangi bir tuşa,\n     tekrar Mühimmat almak için T' harfine basınız) ".format(self.adettt)+"\033[39m")


                        if self.a == "t" or self.a == "T":

                            continue

                        break

                    else:

                        self.a = input("\033[31m"+"\n\n      Lütfen geçerli adette mühimmat isteyin.\n      (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break


                else:

                    self.a = input("\033[31m"+"\n\n      Bu Araca entegre bir silah yoktur. Mühimmat alınamaz.\n      (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                    if self.a == "t" or self.a == "T":

                        continue

                    break


            else:

                self.a = input("\033[31m"+"\n\n      ID Bulunamadı. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break



    def arac_hurda(self):

        """
        Hasar görmüş, kullanılamayacak araçlar veya yabancı üretimli araçların yerine yerli üretimli araçları,
        kademeli olarak geçirmek için ID si girilen araçlar çıkartılmaktadır.
        Tek seferde maximum 10 araç çıkartılmaktadır.

        """

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç hurdaya çıkart")

            try:

                self.id = int(input("\n\n     Hurdaya çıkartmak istediğiniz araç ID = "))

            except ValueError: # arac ID kontrolü

                self.a = input("\033[31m"+"\n\n      ID olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break


            # aracın sistemde olması kontrolü
            self.indis = -1

            self.kontrol = False

            for self.i in self.veri["ID"]:

                self.indis += 1

                if self.i == str(self.id):

                    self.kontrol = True

                    break

                

            if self.kontrol == True:

                os.system('cls' if os.name == 'nt' else 'clear')

                print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç hurdaya çıkart")

                print("\n\n     Araç ad : {} ".format(self.veri["Araç ad"][self.indis]))


                try:

                    self.adet = int(input("\n\n     Kaç adet araç hurdaya çıkartılacak (tek seferde 10 adet çıkartılabilir) = "))

                except ValueError: # adet int kontolü


                    self.a = input("\033[31m"+"\n\n      Adet olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                    if self.a == "t" or self.a == "T":

                        continue

                    break

                if self.veri["Adet"][self.indis] - self.adet >= 0: # yeterli kadar araç varmı ?

                    if self.adet > 0 and self.adet <= 10:

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Onay") # her şeyi eksiksiz yaparsanız sizden onay için şifre istenecektir.

                        self.sifrea = input("\n\n     Yaptığınız işlemin onaylanması için şifrenizi giriniz = ")

                        if self.sifre != self.sifrea:

                            print("\033[31m"+"\n\n     Şifre Hatalı. Güvenlik amaçlı uygulamadan atılıyorsunuz..."+"\033[39m") # hatalı şifrede uygulama kapatılır

                            sl(4)

                            os.system('cls' if os.name == 'nt' else 'clear')

                            print("\n")

                            quit()

                        else:

                            os.system('cls' if os.name == 'nt' else 'clear')

                            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Onay")

                            print("\033[92m"+"\n\n     Şifre onaylandı...."+"\033[39m")

                            sl(4)

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç hurdaya çıkart")

                        self.adett = self.adet # eğer şifre doğru girilirse araç hurdaya çıkartılır.

                        self.veri["Adet"][self.indis] -= self.adet

                        # eğer arac adeti 0 olursa arac veriden tamamen silinir 
                        if self.veri["Adet"][self.indis] == 0:

                            del self.veri["ID"][self.indis]
                            
                            del self.veri["Araç ad"][self.indis]
                            
                            del self.veri["Tür"][self.indis]
                            
                            del self.veri["Adet"][self.indis]
                            
                            del self.veri["Mühimmat"][self.indis]
                            
                            del self.veri["Üreten ülkeler"][self.indis]


                        self.arac_güncelle() # güncelle fonksiyonuna ilerler.

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Araç hurdaya çıkart")

                        input("\033[92m"+"\n\n      İstediğiniz araçtan {} adet hurdaya çıakrtıldı, geri dönmek için Enter 'e basınız".format(self.adett)+"\033[39m")

                    # hata mesajları
                    else:

                        self.a = input("\033[31m"+"\n\n      Hatalı değer aralığı. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break

                else:

                    input("\033[31m"+"\n\n      İstediğiniz kadar araç bulunmamaktadır, geri dönmek için Enter 'e basınız"+"\033[39m")

            else:

                self.a = input("\033[31m"+"\n\n      ID Bulunamadı. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break



            break


    
    def degistir(self):

        # personel ayarları

        while True:

            try:

                self.file = open("19010011019.demir","r+",encoding="utf-8") # dosyayı açtım

            # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
            except FileNotFoundError:

                os.system('cls' if os.name == 'nt' else 'clear')

                print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")

                quit()

            # kuullanıcı adlarıı ve şifreleri listeye aktardım.

            self.ida = []

            self.sifree = []

            self.c = -1

            try: # eğer dosyada hiç kullanıcı yoksa hata vermesin diye

                for self.i in self.file:

                    self.c += 1

                    self.i = self.i[:-1]

                    self.gecici = self.i.split(",")

                    self.ida.append(self.gecici[0])

                    self.sifree.append(self.gecici[1])

                    if self.gecici[0] == self.idaa: # şuanki personelin listedeki indisinu buldum.

                        self.zx = self.c

            except:

                pass


            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel ayarları")

            print("\n\n      1) Kullanıcı adı değiştir")

            print("\n\n      2) Şifre değiştir")

            print("\n\n      M) Bir önceki menüye dön")

            print("\n\n      Q) Çıkış")

            self.secim = input("\n\n   Seçim = ")


            if self.secim == "1": # kullanıcı adı değiştirme

                while True:

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel ayarları")

                    # kullanıcı adındaki tüm şartlar ana menüdeki Personel ekle kısmı ile aynıdır.

                    self.add = input("\n\n      Yeni kullanıcı adı = ") # yeni kullanıcı adı

                    self.kontrol = None

                    # şartlar.

                    for self.i in self.ida:

                        if self.i == self.add:

                            self.kontrol = True

                            break

                    if self.kontrol == True:

                        self.a = input("\033[31m"+"\n\n      Bu Kullanıcı Adı Alınmıştır. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        self.file.close()

                        break


                    elif len(self.add) < 6 or len(self.add) > 9:

                        self.a = input("\033[31m"+"\n\n      Kullanıcı adı beş ile on karekter arasında olmalıdır.\n      (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        self.file.close()

                        break

                    else:

                        self.kontrol = None 

                        for self.i in self.add:

                            if self.add.count(self.i) > 2:

                                self.kontrol = True

                                break


                        if self.kontrol == True:

                            self.a = input("\033[31m"+"\n\n      Kullanıcı adında bir karekter en fazla iki defa tekrar edebilir.\n      (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                            if self.a == "t" or self.a == "T":

                                continue

                            self.file.close()

                            break

                        else:

                            os.system('cls' if os.name == 'nt' else 'clear')

                            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Onay")

                            self.sifrea = input("\n\n     Yaptığınız işlemin onaylanması için şifrenizi giriniz = ")

                        
                            if self.sifre != self.sifrea:

                                print("\033[31m"+"\n\n      Şifre Hatalı. Güvenlik amaçlı uygulamadan atılıyorsunuz..."+"\033[39m")

                                sl(4)

                                os.system('cls' if os.name == 'nt' else 'clear')

                                print("\n")

                                quit()

                        
                            else:

                                os.system('cls' if os.name == 'nt' else 'clear') 

                                # herşey sorunsuz ilerlerse onay amaçlı şifreniz istenir
                                # şifre onaylanırsa işlem gerçekleşir
                                # hatalıysa uygulamadan atılırsınız

                                print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Onay")

                                print("\033[92m"+"\n\n     Şifre onaylandı...."+"\033[39m")

                                sl(4)

                            self.file.close() # döngü başındaki dosya kaptılır

                            try:

                                self.file = open("19010011019.demir","w",encoding="utf-8") # yazma kipinde açılır

                            # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
                            except FileNotFoundError:

                                os.system('cls' if os.name == 'nt' else 'clear')

                                print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")

                                quit()

                            os.system('cls' if os.name == 'nt' else 'clear')

                            self.ida[self.zx] = self.add # listedeki veri değistirilir

                            self.idaa = self.add

                            for self.i in range(0,len(self.ida)): # liste dosyaya yazılır.

                                self.file.write(self.ida[self.i])

                                self.file.write(",")

                                self.file.write(self.sifree[self.i])

                                self.file.write(",")

                                self.file.write("\n")

                            self.file.close()

                            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel ayarları")

                            input("\033[92m"+"\n\n     Kullanıcı adınız {} olarak değiştirilmiştir.\n     Bir önceki menüye dönmek için Enter'e basınız. ".format(self.add)+"\033[39m")

                            break



            elif self.secim == "2": # şifre değiştirme

                while True:

                    os.system('cls' if os.name == 'nt' else 'clear')

                    print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel ayarları")

                    self.sifrea = input("\n\n     Yeni şifre        = ")

                    self.sifrea1 = input("\n\n     Yeni şifre tekrar = ")

                    # şifre kontrolü ana menüdeki personel ekle ile aynıdır.

                    if self.sifrea != self.sifrea1:

                        self.a = input("\033[31m"+"\n\n      Şifreler eşleşmemektedir. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        self.file.close()

                        break

                    else:

                        if len(self.sifrea) < 5 or len(self.sifrea) > 11:

                            self.a = input("\033[31m"+"\n\n      Şifre 4 ile 12 karekter arasında olmalıdır.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                            if self.a == "t" or self.a == "T":

                                continue

                            self.file.close()

                            break

                        else:

                            self.kontrol = None

                            for self.a in self.sifrea:

                                if(ord(self.a) >= 32 and ord(self.a) <= 47) or (ord(self.a) >= 58 and ord(self.a) <= 64) or (ord(self.a) >= 91 and ord(self.a) <= 96) or (ord(self.a) >= 122 and ord(self.a) <= 126):

                                    self.kontrol = True
                                    
                                    break


                            if self.kontrol == None:

                                self.a = input("\033[31m"+"\n\n      Şifre de en az bir tane alfanümerik karekter bulunmalı.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                                if self.a == "t" or self.a == "T":

                                    continue

                                self.file.close()

                                break

                        
                            else:

                                if self.idaa in self.sifrea:

                                    self.a = input("\033[31m"+"\n\n      Şifre içinde kullanıcı adınız olmamalı.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                                    if self.a == "t" or self.a == "T":

                                        continue

                                    self.file.close()

                                    break

                                else:

                                    os.system('cls' if os.name == 'nt' else 'clear')

                                    print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Onay")

                                    self.sifrea = input("\n\n     Yaptığınız işlemin onaylanması için ESKİ şifrenizi giriniz = ") # güvenlik amaçlı eski şifre istenilir

                                    # hatalı ise uygulamadan atılır

                        
                                    if self.sifre != self.sifrea:

                                        print("\033[31m"+"\n\n      Şifre Hatalı. Güvenlik amaçlı uygulamadan atılıyorsunuz..."+"\033[39m")

                                        sl(4)

                                        os.system('cls' if os.name == 'nt' else 'clear')

                                        print("\n")

                                        quit()

                        
                                    else:

                                        os.system('cls' if os.name == 'nt' else 'clear')

                                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Onay")

                                        print("\033[92m"+"\n\n     Şifre onaylandı...."+"\033[39m")

                                        sl(4)

                                        self.file.close()

                                        self.sifree[self.zx] = self.sifrea1 # sözlükte değişiklik yapılır

                                        self.sifre = self.sifrea1

                                        try:

                                            self.file = open("19010011019.demir","w",encoding="utf-8")


                                        except FileNotFoundError:

                                            os.system('cls' if os.name == 'nt' else 'clear')

                                            print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")

                                            quit()

                                        for self.i in range(0,len(self.ida)):

                                            # liste dosyaya yazılır.

                                            self.file.write(self.ida[self.i])

                                            self.file.write(",")

                                            self.file.write(self.sifree[self.i])

                                            self.file.write(",")

                                            self.file.write("\n")

                                        self.file.close()

                                        os.system('cls' if os.name == 'nt' else 'clear')

                                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel ayarları")

                                        input("\033[92m"+"\n\n      Yeni şifreniz onaylandı, Bir önceki menüye dönmek için Enter 'e basınız"+"\033[39m")

                                        break
                                    
            elif self.secim == "m" or self.secim == "M":

                break

            elif self.secim == "q" or self.secim == "Q":

                quit()


    def kayit(self):

        # envantere yeni üretilmiş araç veya satın alınmış araçları eklemek için fonksiyon

        while True:

            os.system('cls' if os.name == 'nt' else 'clear')

            print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Yeni araç kaydı")

            self.arac_ad = input("\n\n     Yeni araç adı (max: 23 harf, min: 4 harf) = ")

            if len(self.arac_ad) < 4 or len(self.arac_ad) >23: # araç adı uzunluk kontrolü

                self.a = input("\033[31m"+"\n\n     Yeni aracın adı istenilen karekter uzunluğunda değil.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                if self.a == "t" or self.a == "T":

                    continue

                break

            else:

                self.arac_tür = input("\n\n     Yeni araç türü (max: 27 harf, min: 5 harf) = ")

                if len(self.arac_tür) < 5 or len(self.arac_tür) >27: # araç türü uzunluk kontrol

                    self.a = input("\033[31m"+"\n\n     Yeni aracın adı türü istenilen karekter uzunluğunda değil.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                    if self.a == "t" or self.a == "T":

                        continue

                    break

                else:

                    try:

                        self.arac_adet = int(input("\n\n     Yeni aracın adeti (Tek seferde 200 araç ekleyebilirsiniz.) = "))

                    except ValueError: # adet int kontolü

                        self.a = input("\033[31m"+"\n\n      Adet olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break

                    if self.arac_adet <= 0 or self.arac_adet >200: # adet kontrol

                        self.a = input("\033[31m"+"\n\n     Yeni aracın adedi istenilen aralıkta değil.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break


                    try:

                        self.arac_mühimmat = int(input("\n\n     Araca entegre silah varsa mühimmat adeti giriniz (yoksa 0 giriniz, Tek seferde maximum 500 adet) = "))


                    except ValueError: # adet int kontolü

                        self.a = input("\033[31m"+"\n\n      Mühimmat adet olarak INT değerler giriniz. (Geri dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break

                    if self.arac_mühimmat < 0 or self.arac_mühimmat >500: # mühimmat kontrolü

                        self.a = input("\033[31m"+"\n\n     Yeni aracın Mühimmatı istenilen aralıkta değil.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break

                    self.ulkeler = input("\n\n     Yeni aracın üretildiği ülke veya ülkeler (max: 9, min: 3) = ")

                    if len(self.ulkeler) < 3 or len(self.ulkeler) > 9: # üretim yeri uzunluk kontrolü

                        self.a = input("\033[31m"+"\n\n     Yeni aracın üretildiği ülkeler istenilen karekter uzunluğunda değil.\n      (Ana menüye dönmek için herhangi bir tuşa,\n      tekrar denemek için T' harfine basınız) = "+"\033[39m")

                        if self.a == "t" or self.a == "T":

                            continue

                        break


                    else:

                        # yeni verileri sözlüğe ekleme

                        self.veri["ID"].append(len(self.veri["ID"]) +1)

                        self.veri["Araç ad"] += [self.arac_ad]

                        self.veri["Tür"] += [self.arac_tür]

                        self.veri["Adet"] += [self.arac_adet]

                        if self.arac_mühimmat == 0:

                            self.veri["Mühimmat"] += ["*"]

                        else:

                            self.veri["Mühimmat"] += [self.arac_mühimmat]


                        self.veri["Üreten ülkeler"] += [self.ulkeler]

                        self.arac_güncelle() # ardından dosyayı güncelleme

                        os.system('cls' if os.name == 'nt' else 'clear')

                        print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Yeni araç kaydı")

                        input("\033[92m"+"\n\n      {} adlı araç Envantere eklenmiştir\n\n      Ana menüye dönmek için herhangi bir tuşa basınız".format(self.arac_ad)+"\033[39m")

                        break


def islem(islem):

    def kullanici_ekle(personel_ekle_kontrol): # yeni personel ekleme
    
    	def parcala(): # iç içe fonksiyon, dosya işlemleri için
    		
    		try:

    			file = open("19010011019.demir","r+",encoding="utf-8")
            
            # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
    		except FileNotFoundError:

    			os.system('cls' if os.name == 'nt' else 'clear')
    			
    			print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")

    			quit()
				

    		ida = []
    
    		sifre = []
    
    		try: # dosyanın içi boşsa hata vermesin diye
    
    			for i in file:
    
    				i = i[:-1]
    
    				gecici = i.split(",")
    
    				ida.append(gecici[0]) # veriler listtelere aktarılıyor.
    
    				sifre.append(gecici[1])
    
    		except:
    
    			pass
    
    
    		yield ida # bellekte yer kaplamaması için iterable obje döndüren fonksiyon tercih ettim (generator fonksiyon)
    
    		yield file
    
    
    	ids, file = parcala()
    
    	while True:
    
    
    		if personel_ekle_kontrol == 3: # eğer üç defa hatalı personel eklenmeye çalışılırsa güvenlik amaçlı uygulamadan atılır.
    
    			os.system('cls' if os.name == 'nt' else 'clear')
    
    			print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel Giriş")
    
    			print("\033[31m"+"\n\n      Üç defa hatalı Personel eklemeye çalıştınız.\n      güvenlik amaçlı atılıyorsunuz..."+"\033[39m")
    
    			sl(4)
    
    			os.system('cls' if os.name == 'nt' else 'clear')
    
    			print("\n")
    
    			quit()
    
    
    		os.system('cls' if os.name == 'nt' else 'clear')
    
    		print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel Ekle")

    		print(""" 

    Kullanıcı adı şartları :
    		
    Daha önceden o kullanıcı adının alınmaması(Eşssiz olmalı),
    Kullanıcı adı 5 ile 10 karekter arasında olmalı (6,7,8,9),
    Kullanıcı adında bir karekter enfazla iki kere tekrar edebilir.""")
    
    		ida = input("\033[92m"+"\n\n     Kullanıcı adı  = "+"\033[39m")

    		print(""" 

    Şifre şartları :
    		
    Şifre ve şifre tekrar birbirine eşit olmalı,
    Şifre 4 ile 10 karekter arasında olmalı (5,6,7,8,9),
    Şifre de en az bir tane alfanümerik karekter bulunmalı(*,/,-,+,{ gibi).
    Şifre içersinde kullanıcı adınız bulunmamalı""")
    
    		sifrea  = input("\033[92m"+"\n     Şifre          = "+"\033[39m")
    
    		sifrea1 = input("\033[92m"+"\n     Şifre Tekrar   = "+"\033[39m")
    
    		kontrol = None
    
    		for i in ids: # kullanıcı adının eşsiz olma kontrolü
    
    			if i == ida:
    
    				kontrol = True
    
    				break
    
    		if kontrol == True:
    
    			a = input("\033[31m"+"\n\n     Bu Kullanıcı Adı Alınmıştır. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    			personel_ekle_kontrol += 1

    			if a == "t" or a == "T":
    
    				continue
    
    
    			file.close()
    
    			return personel_ekle_kontrol
    
    		elif len(ida) < 6 or len(ida) > 9: # kullanıcı adı uzunluk kontrolü
    
    			a = input("\033[31m"+"\n\n     Kullanıcı adı beş ile on karekter arasında olmalıdır.\n     (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    			personel_ekle_kontrol += 1

    			if a == "t" or a == "T":
    
    				continue
    
    			file.close()
    
    			return personel_ekle_kontrol
    
    		else:
    
    			kontrol = None 
    
    			for i in ida: # kullanıcı adında bir karekterin en fazla iki kez tekrar etme kontrolü
    
    				if ida.count(i) > 2:
    
    					kontrol = True
    
    					break
    
    
    			if kontrol == True:
    
    				a = input("\033[31m"+"\n\n     Kullanıcı adında bir karekter en fazla iki defa tekrar edebilir.\n     (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    				personel_ekle_kontrol += 1

    				if a == "t" or a == "T":
    
    					continue
    
    				file.close()
    
    				return personel_ekle_kontrol
    
    			else:
    
    				if sifrea != sifrea1: # girilen iki şifrenin aynı olması kontrolü
    
    					a = input("\033[31m"+"\n\n     Şifreler eşleşmemektedir. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    					personel_ekle_kontrol += 1

    					if a == "t" or a == "T":
    
    						continue
    
    					file.close()
    
    					return personel_ekle_kontrol
    
    				else:
    
    					if len(sifrea) < 5 or len(sifrea) > 11: # şifre uzunluk kontrolü
    
    						a = input("\033[31m"+"\n\n     Şifre 4 ile 12 karekter arasında olmalıdır.\n     (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    						personel_ekle_kontrol += 1

    						if a == "t" or a == "T":
    
    							continue
    
    						file.close()
    
    						return personel_ekle_kontrol
    
    					else:
    
    						kontrol = None
    
    						for a in sifrea: # şifrede alfanümerik karekter bulunma kontrolü
    
    							if(ord(a) >= 32 and ord(a) <= 47) or (ord(a) >= 58 and ord(a) <= 64) or (ord(a) >= 91 and ord(a) <= 96) or (ord(a) >= 122 and ord(a) <= 126):
    
    								kontrol = True
    								break
    
    
    						if kontrol == None:
    
    							a = input("\033[31m"+"\n\n     Şifre de en az bir tane alfanümerik karekter bulunmalı.\n     (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    							personel_ekle_kontrol += 1

    							if a == "t" or a == "T":
    
    								continue
    
    							file.close()
    
    							return personel_ekle_kontrol
    
    						
    						else:
    
    							if ida in sifrea: # şifre içersinde kullanıcı adı olmama kontrolü
    
    								a = input("\033[31m"+"\n\n     Şifre içinde kullanıcı adınız olmamalı.\n     (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    	
    								personel_ekle_kontrol += 1

    								if a == "t" or a == "T":
    
    									continue
    
    								file.close()
    
    								return personel_ekle_kontrol
    
    							else:
    
    								"""
    	
    								Kullanıcı adı ve şifre kısımlarını istenilen kurallarda belirledikten sonra TSK.pem adlı
    								Doğrulama anahtarını kod ile aynı dizinde bulundurursanız sorunsuz bir şekilde yeni
    								Personel oluşturulur.
    
    								"""
    
    								os.system('cls' if os.name == 'nt' else 'clear')
    
    								print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel Ekle")
    
    								print("\n\n    Bakanlık tarafından size verilen,\n    19010011019.pem adlı dosyayı ",os.getcwd()," Konumunda bulundurunuz ...")
    
    								sl(5)
    	
    								try:
    		
    									dosya = open("19010011019.pem","r+",encoding="utf-8")
    
    	
    								except FileNotFoundError: # dosya bulunamazsa hata verir.
    
    									print("\033[31m"+"\n\n    Anahtar bulunamadı. Güvenlik amaçlı uygulamadan atılıyorsunuz..."+"\033[39m")
    
    									sl(4)
    
    									os.system('cls' if os.name == 'nt' else 'clear')
    
    									print("\n")
    
    									quit()
    
    
    								if dosya.read() == güvenli_veri: # anahtarın içersindeki şifre doğruysa işlem gerçekleşir

    									try:

                                            # dosya güvenlik amaclı kaydedilir, herhangi bir hata olması durumunda eski kayıtlar kullanılır.
    										shutil.copy2("19010011019.demir", "log_dir/personel_veri_eski/")

    									except:

    										pass

    									metin = ida+ "," +sifrea
    
    									file.write(metin)
    
    									file.write(",")
    
    									file.write("\n")
    
    									file.close()
    
    									print("\033[92m"+"\n\n     Yeni Personel Başarıyla eklendi. Ana Menüye Yönlendiriliyorsunuz ..."+"\033[39m")

    									an = datetime.datetime.now()

    									yıl = an.year

    									ay = an.month

    									gün = an.day

    									saat = str(an.hour) + ":" + str(an.minute)

    									tarih = str(gün) + "/" +str(ay) + "/" + str(yıl) + " - " + saat

    									mesaj = "Yeni Personel Eklendi - " + tarih + ", \n"

    									try:

                                            # otomasyonda yapılan aktivite kaydedilir.
    										lg = open("log_dir/personel_veri_geçmiş/gecmis.txt","a+")

                                        # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
    									except FileNotFoundError:

    										os.system('cls' if os.name == 'nt' else 'clear')

    										print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")
    										quit()


    									lg.write(mesaj)

    									lg.close()
    
    									sl(5)
    								
    									return 0
    
    								else: # hatalıysa
    
    									print("\033[31m"+"\n\n    Anahtar Hatalı. Güvenlik amaçlı uygulamadan atılıyorsunuz..."+"\033[39m")
    
    									sl(3)
    
    									os.system('cls' if os.name == 'nt' else 'clear')
    
    									print("\n")
    
    									quit()
    
    
    def giris(personel_giris_kontrol):
    
    	while True:
    
    		# personelin giriş yaptığı fonksiyon.
    
    		if personel_giris_kontrol == 3: # eğer personel giriş kısmında üç kez hata yapıldıysa
    
    			# güvenlik amaçlı uygulamadan atılır.
    
    			os.system('cls' if os.name == 'nt' else 'clear')
    
    			print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel Giriş")
    
    			print("\033[31m"+"\n\n      Üç defa hatalı Personel girişi yapmaya çalıştınız.\n      güvenlik amaçlı atılıyorsunuz..."+"\033[39m")
    
    			sl(4)
    
    			os.system('cls' if os.name == 'nt' else 'clear')
    
    			print("\n")
    
    			quit()
    
    
    		os.system('cls' if os.name == 'nt' else 'clear')
    
    
    		def parcala(): # iç içe fonksiyon
    
    			# giriş yapmak isteyen personelin verilerini doğrulamak için dosya açılır.
    			
    			try:

    				file = open("19010011019.demir","r+",encoding="utf-8")
    
    			except FileNotFoundError:

    				os.system('cls' if os.name == 'nt' else 'clear')

    				print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")
    				quit()
					

    				
    			ida = []
    
    			sifre = []
    
    			try: # dosyanın içi boşsa hata vermesin diye
    
    				for i in file: # dosya parçalanır ve listelere aktarılır
    
    					i = i[:-1]
    
    					gecici = i.split(",")
    
    					ida.append(gecici[0])
    
    					sifre.append(gecici[1])
    
    			except:
    
    				pass
    
    			file.close() # dosya kapatılır
    
    			yield ida # bellekte yer kaplamaması için iterable obje döndüren fonksiyon tercih ettim (generator fonksiyon)
    
    			yield sifre
    
    
    		ids, sifre = parcala()
    
    		print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel Giriş")
    
    		ida = input("\n\n     Kullanıcı adı = ")
    
    		sifrea = input("\n     Şifre         = ")
    
    		kontrol = None
    
    		for i in ids: # kullanıcı adı kontrolü, listeden kontrol edilir
    
    			if i == ida:
    
    				kontrol = True
    
    				break
    
    
    		if kontrol == None: # hatalı ise
    
    			az = input("\033[31m"+"\n\n     Kullanıcı Adı Hatalı. (Ana menüye dönmek için herhangi bir tuşa,\n     tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    			personel_giris_kontrol += 1
    
    			if az == "t" or az == "T":
    
    				continue
    
    			return 0, "a", personel_giris_kontrol, "a"
    
    		else:
    
    
    			for i in sifre: # şifre kontrolü, listeden.
    
    				if i == sifrea:
    
    					kontrol = False
    
    					break
    
    
    		if kontrol != False: # hata
    
    			a = input("\033[31m"+"\n\n      Şifre Hatalı. (Ana menüye dönmek için herhangi bir tuşa,\n      Tekrar denemek için T' harfine basınız) = "+"\033[39m")
    
    			personel_giris_kontrol += 1
    
    			if a == "t" or a == "T":
    
    				continue
    
    			return 0, "a", personel_giris_kontrol, "a"
    
    		else: # herhangi bir sorun yoksa geriye 1 değerinin dödürür ve main fonksiyonuna ilerler.

    			an = datetime.datetime.now()

    			yıl = an.year

    			ay = an.month

    			gün = an.day

    			saat = str(an.hour) + ":" + str(an.minute)

    			tarih = str(gün) + "/" +str(ay) + "/" + str(yıl) + " - " + saat

    			mesaj = "Sisteme Giriş Yapıldı - " + tarih + ", \n"

    			try:

                    # yapılan aktivite kaydedilir.
    				lg = open("log_dir/personel_veri_geçmiş/gecmis.txt","a+")

                # dosyayı bulamazsa veri güvenliği tehlikede olduğu için otomasyondan atılır.
    			except FileNotFoundError:

    				os.system('cls' if os.name == 'nt' else 'clear')

    				print("\033[31m"+"\n\n      Güvenlik açığı tespit edildi. uygulamadan çıkışınız verilmiştir. "+"\033[39m"+"\n\n")
    				quit()


    			lg.write(mesaj)

    			lg.close()
    
    			os.system('cls' if os.name == 'nt' else 'clear')
    
    			print("\n\n    TSK | Kara Araçları Envanter Otomasyonu - Personel Giriş")
    
    			print("\033[92m"+"\n\n        Giriş Başarılı... "+"\033[39m")
    
    			sl(3)
    
    			return 1, ida, 0, sifrea


    if islem == "giriş":

    	return giris

    elif islem == "ekle":

    	return kullanici_ekle

    # fonksiyon objesi döndüren fonksiyon.



global güvenli_veri # global güvenlik anahtarı (Bakanlık tarafından verilen.)

güvenli_veri ="""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAgwJ3V0WovRZgs+TfgGIcIQzuwsSaLfMrx96N6209VOlBoWJ4/6oOcC8AfSqA
7n94xY7D2xNPz9H1KDb3plIINHotHUmq3Ql7+kFKqH8vVhOOSeQPtNosFsPVPSORSD8RRJWIesqW
7F5237LP5IzEXIBdoU6TIylE57ywTN6LyDlN3+n8rSy/fUceT/N4Mk5c79Yc9d62x2qFTW3WKsXh
1YNqC6mOho2ZTmmDYdDSeMm5Gnp21iYbMNw8cSE6xZvfFrQM4yCzVYZNFcPM1ZKvDZPTbZsO1l2b
8EjgdB5bH8SPGi9oFQlSBsY9nroFannC0uaZnJTqn4pIialTNZuwzwIDAQABAoIBAQCAhFDSGhGX
vHYMwz7FUHlLqsYl5nthDCUsopQSGU2LGG87g8Ay/X3AaztNjf6A+Cdflddn95/ZvJuEYbe7Psmx
wRC0pGmq//zQ2HAGrw2eoPx6W/FUdpm9k0qB+XwxpTypTQ9fdZFsOpbehykNiVGvdHVlIhGQ8pEX
y7AfGEmDldpNkiksLCBIPCiwG90bAgGEssRs3T7I+LwWoJg41vj33usXvsg9t4gfx1AD0XZtDdkL
/rnS/MV1iPPfjPBxYaZg+h/cJpu1Cw9OCUya+77QvZLlsbLaDT5tzgSbyPU69mLZdggMjy+IJcme
oUFgE/oGAQl/Ez7MFa+h6y/AUfNxAoGBAMo8DXFvEdhGHv2Txq4d+Qeg+uNulWApFuS7MHe9ajLo
s6HPZ3iwRTo9AUTEB2wzA3Jfz2E7J5d4ok1EfGwyajBauZ+T82uSjDnlBSjW7Rnu8ds00NgwEb9N
ZF2UPu/WqKQ7+0fC164OM2GYKRTy7m1cSGZ3UT1Ut3qgS27j1MwtAoGBAKXW5HUDlMHY6wJV8q4I
9uMYQS6mtqDnrR0OxtShPP/FdmAczyRmq1sATY7vlg4gO0YTpmb/bsWm0tHjmn5ikvJglRU2HNHJ
HS2yqmLE5imlC8uon/BYXHDZOH0yb7SJuMiNVaPuK5JXbz7rfEHMD1XWdZ4f1oYm/ewOe7nbmgJr
AoGASk5mYhd9ZwncuS9jAPbiWXs8s/QdzodKciCVXmmqa6o01m9uhVm/Ffb0UF/2mjrkOVIa0I77
rRwWBm3ziY28lqe/LHMgLZZbD6qmiqrt02mIVBLD6as/2hqFlhyyQ02MCUxAt81PkhSFrIZMEfZw
xJ3zvDJ7Fx3ZjKT5EnWD6sECgYAwRXCSLsyp7/3X3DSbO7jBOVofvh8CjuzwvFBbq+MZf9yI9VnF
+qx9/ISWyl4fFnqqVyXkbQ1NMtXCikF58C9dpYc/eVTCK4v2tT6rKSzlikj4qsiDKPUfU9sBdiDV
qBDFL35yDO1Z12FmKx0r+b2s+pOZxyKmQcs/Xqfc3XLiqQKBgHvMjiywPbWDlMHZ7m+xwv8uABZz
KwP0J6sWdsyqavgoA+f+WcJ6ZqS+NluxnrlGaFnhMS5OJhKM8t3Ubzt6/atGAK4QMKN9OjrgmLVV
5R86auyrZJ8R+N1hPFaxScPat61+CJ0foXP0yC1EigEcEc051e0d5Q8umjs4xTWOfnoO
-----END RSA PRIVATE KEY-----"""



def main():

	# kodun başladığı yer

	personel_giris_kontrol = 0 # 3 hata ile güvenlik amaçlı uygulamadan atmak için.

	personel_ekle_kontrol = 0 # 3 hata ile güvenlik amaçlı uygulamadan atmak için.

	while True:

		os.system('cls' if os.name == 'nt' else 'clear')

		print(""" 

   TSK | Kara Araçları Envanter Otomasyonu


	1) Personel Giriş

	2) Yeni Personel Ekle

	Q) Çıkış

			""") # menü


		secim = input("\n   Seçim = ")


		if secim == "1":

			fonk = islem("giriş")

			kontrol, ida, personel_giris_kontrol,sifre = fonk(personel_giris_kontrol) # giris fonksiyonuna ilerler

			if kontrol == 1: # çıkan kontrol değerine göre giriş başarılı veya hatalıdır.

				tsk = Tsk(ida,sifre) # Tsk objesi yaratılır ve parametre olarak, personel kullanıcı adı ve şifresini alır.

		
		elif secim == "2": # personel ekleme

			fonk = islem("ekle")

			personel_ekle_kontrol = fonk(personel_ekle_kontrol) # kullanici_ekle fonksiyonuna ilerler.


		elif secim == "q" or secim == "Q":

			os.system('cls' if os.name == 'nt' else 'clear')

			print("\n")

			quit()


if __name__ == "__main__":  
	
	# başka bir python kodundan bu kodu çağırınca çalışmaması için kullandım, güvenlik amaçlı
	
	main()