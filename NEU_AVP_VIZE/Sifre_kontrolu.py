# Ad,Soyad = Ahmet Furkan DEMIR , No = 19010011019

"""
Kodu ilk çalıştırdığınızda PyQt5 modülü kurulu değilse bu modülü kuracaktır,

kurulumdan sonra sizi koddan atacak, bir sonraki çalıştırmanızda herhangi bir sorun çıkmayacaktır.

- kullanıcının girdiği sifreyi 133. satırdaki fonksiyondan(click) kontrol ettim.

sifre istenilen kriterlerde ise yeni bir pencere açıp giriş başarılı yazdırdım.

kendi belirlediğim 2 kriter:

 1-) Sifrede Türkçe karakterler bulunmayacak

 2-) Sifrede kullanici adınız bulunmayacak.

"""

import os # işletim sisteminizdeki kullanıcı adınızı öğrenmek ve ekran temizleme gibi işlemler için.
from time import sleep as sl # sleep fonksiyonunu kullandım
import sys # pencereden çıkma işlemi, ve tıklamalar için gerekli

clea = os.name # işletim sisteminizi öğrendim

if clea == "posix": # linux, mac 
	clear = "clear"

else: # windows

	clear = "cls"
try:

    from PyQt5 import QtWidgets,QtGui

    """ Görsel programlama için gerekli kütüphane.
    Eğer sisteminizde yüklü değilse hata verir.
    hatayı da try except bloklarıyla yakaladık  """

except:

    #bu blokta ise gerekli modülleri kurduk.
    #daha sonra kullanıcıyı programdan attık.
    #bir sonraki girişinizde modül kurulu olduğu için sorun çıkmayacaktır.
    
    print("\n\n  - Gerekli modüller bulunamadı.")
    sl(3)
    print("\n\n  - Modüller kuruluyor, lütfen bekleyiniz... (internet bağlantısı gerekli!!!) \n")
    sl(4)
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install pyqt5")

    os.system("pip install vext.pyqt5")

    os.system("pip3 install PyQt5") # kurulumlar
    os.system("pip install PyQt5")

    os.system(clear)
    print("\n\n  - Gerekli modüller kuruldu. Lütfen Programı tekrar çalıştırınız.\n\n")
    quit()


global veri1

veri1 = ""

for i in os.getlogin():

    if i != " ":

        veri1 += i


class Pencere(QtWidgets.QWidget): #PyQt5 modülünden miras alarak yeni bir sınıf oluşturduk.

    def __init__(self):
        
        super().__init__() # aldığımız mirası geliştirmek için gerekli metod (buton oluştuma, yazı alanı oluşturma)

        self.ozellik() # işlemler bittikten sonra bu fonksiyona ilerleyecek
    
    
    def ozellik(self):
        
        
        self.setGeometry(425,175,550,450) # pencere boyutu ve konumu
        
        self.setWindowTitle("DEMIR") # pencere başlığı
        
        self.islem_alani = QtWidgets.QLineEdit(veri1) # kullanıcı adı yazma yeri (otomatik olarak kullanıcı adınızı yazdım)
        
        self.hesapla = QtWidgets.QPushButton("Giriş") # giriş için buton olşturduk
        
        self.sonuc = QtWidgets.QLabel("Şifre") # şifre yazısı
        
        self.hsp = QtWidgets.QLabel("Kullanıcı adı") # kullanıcı adı yazısı
        
        self.islem_alanii = QtWidgets.QLineEdit() # şifre yazılacak kutu
        
        
        v_box = QtWidgets.QVBoxLayout() # tüm nesneleri düzgün bir şekilde göstermek için vertical layout oluşturdum.
        
        v_box.addStretch() # layerler arası boşluk
        
        v_box.addWidget(self.hsp) # burdan itibaren nesneleri pencereye dahil ediyorum
        
        v_box.addWidget(self.islem_alani)
        
        v_box.addWidget(self.sonuc)
        
        v_box.addWidget(self.islem_alanii)
        
        v_box.addStretch() # boşluk bıraktım
        
        v_box.addWidget(self.hesapla)
        
        v_box.addStretch()
        
        h_box = QtWidgets.QHBoxLayout() # ekranı büyültünce bozulma olmaması için horizontl layout oluşturdum
        
        h_box.addStretch() #boşluk bıraktım
        
        h_box.addLayout(v_box) # horizontl layout içine vertical layout ekledim
        
        h_box.addStretch() #boşluk bıraktım
        
        self.setLayout(h_box) # layoutları pencereye ekledim
        
        self.hesapla.clicked.connect(self.click) # giriş butonuna tıklanırsa click fonksiyonu tetiklenecek
        
        self.show() # pencere hazır ve ekrana çıkarttık.

    
# -------------------------------- Sifreyi kontrol ettigim fonksiyon ----------------------------- 
    
    def click(self):           

        self.tr = ["ı","ğ","ü","ş","ö","ç","Ü","Ş","İ","Ö","Ç","Ğ"] # türkçe karakterler
        
        self.veri = self.islem_alanii.text() # şifre yazdığınız kutudaki şifreyi aldım
        
        self.kontrol = False

        self.veri11 = ""

        for self.i in self.islem_alani.text(): # kullanıcı adındaki boşlukları sildim

            if self.i != " ":

                self.veri11 += self.i

        if len(self.veri11) < 4 or len(self.veri11) >= 10: # kullanıcı adı kontrolu
        	
        	self.hesapla.setText("HATA! (Kullanıcı adınız 3 ila 10 karekter arasında olmalı.)")
        
        elif len(self.veri)>=8 and len(self.veri)<=12: # şifre uzunluğu kontrol

            for self.i in self.tr: # türkçe karakter kontrol

                for self.a in self.veri:

                    if self.i == self.a:
                        self.kontrol = True
                        break
            
            
            self.islem_alani.setText(self.veri11)

            if self.kontrol == False:

                self.kontrol = False

                for self.i in range(0,10): # sayi ile başlayıp sayı ile bitmeme kontrolü
                
                    if str(self.i) == self.veri[0]:
                    
                        self.kontrol = True
                    
                        break
                
                    if str(self.i) == self.veri[-1]:
                    
                        self.kontrol = True
                    
                        break
                
                if self.kontrol == False:
                
                    self.kckontrol = False
                    self.bykontrol = False
                    self.strkontrol = False  
                
                    for self.i in range(0,26): # büyük küçük harf kontrolü ve boşluk kontrolü
                    
                        for self.a in self.veri:
                        
                            if chr(65+self.i) == self.a:
                            
                                self.bykontrol = True
                            
                            if chr(97+self.i) == self.a: # ascii karakter tablosuna göre kontrol ettim
                            
                                self.kckontrol = True
                            
                            if self.a == " ":
                            
                                self.strkontrol = True
                    
                    if self.strkontrol == True:
                    
                        self.hesapla.setText("HATA! (Sifre Boşluk karakteri içeremez..)")
                    
                    elif self.bykontrol == True and self.kckontrol == True:
                    
                        self.kontrol = False
                    
                        for self.a in self.veri: # sifrede alfanümerik karakter varmı diye kontrol ettim.
                        
                            if (ord(self.a) >= 32 and ord(self.a) <= 47) or (ord(self.a) >= 58 and ord(self.a) <= 64) or (ord(self.a) >= 91 and ord(self.a) <= 96) or (ord(self.a) >= 122 and ord(self.a) <= 126):
                                # ascii karakter tablosuna göre
                                self.kontrol = True
                                break
                        
                        if self.kontrol == True:
                        
                            self.kontrol = False
                        
                            for self.a in self.veri:
                            
                                if self.veri.count(self.a) > 1: # tekrarlayan karakter varmı diye kontrol ettim.
                                    # 1 den büyükse o karakterden birden çok var demektir.
                                    self.kontrol = True
                                    break
                         

                            if self.kontrol == False:

                                self.a = self.veri11

                                self.kontrol = self.a in self.veri # kullanıcı adınız şifrenin içinde varmı diye kontrol ettim.

                                if self.kontrol == bool(1):

                                    self.hesapla.setText("HATA! (Şifre içinde kullanıcı adınız bulunmamalıdır.)")

                                else:

                                    self.maina(self.islem_alani.text()) # giriş başarılıysa yeni bir pencere açtım.


                            # aşağıdaki kodlar hata mesajlarıdır.

                            else:
                            
                                self.hesapla.setText("HATA! (Şifre içinde tekrarlayan karakter bulunmamalıdır.)")
                            
                        
                        else:
                        
                            self.hesapla.setText("HATA! (Sifre en az 1 tane alfanümerik olmayan karakter içermelidir.)")
                    
                    else:
                    
                        self.hesapla.setText("HATA! (Sifre En az 1 büyük harf ve en az 1 küçük harf karakteri içermelidir.)")
                    
                
                else:
                
                    self.hesapla.setText("HATA! (Şifre Sayı ile başlayıp sayı ile bitemez.)")
            
            else:

                self.hesapla.setText("HATA! (Sifre Türkçe karekter içeremez.)")
            
        else:
            
            self.hesapla.setText("HATA! (Şifre en az 8 , en fazla 12 karakter içermelidir.)")
        
        
# ---------------------------------------------------------------------------------------        
   
    def maina(self,id): # yeni pencere, giriş başarılıysa girecek.
        
        super().__init__()
        
        self.hesapla.setText(" Giriş Başarılı ")
        
        self.setGeometry(475,210,450,400)
        
        self.setWindowTitle("Giriş Başarılı [{}]".format(id))
        
        self.giris = QtWidgets.QLabel("Giriş Başarılı.")
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addStretch()
        
        v_box.addWidget(self.giris)
        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addStretch()
        
        h_box.addLayout(v_box)
        
        h_box.addStretch()
        
        self.setLayout(h_box)
        
        self.show()
        
if __name__ == "__main__":  # başka bir python kodundan bu kodu çağırınca çalışmaması için kullandım, güvenlik amaçlı         

    try:
        
        uygulama = QtWidgets.QApplication(sys.argv) # argümanları, tıklama vb. durumları modüle iletiyoruz.

        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion')) # pencere türü
        pencere = Pencere() # nesne tanımlama

        uygulama.exec_() # uygulama çıkış kontrolü

    except:

        pass