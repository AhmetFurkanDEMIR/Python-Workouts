import sys
from PyQt5 import QtWidgets,QtGui
import pandas as pd

import hashlib as hasher

veri = pd.read_csv('veri.csv')

sifreleyici = hasher.sha256()
        

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        
        super().__init__()

        self.ozellik()
    
    def ozellik1(self):
        
        global veri
        
        self.setGeometry(100,200,700,400)
        
        self.setWindowTitle("DEMIR (Kayıt ol)")
        
        self.islem_alani3 = QtWidgets.QLineEdit()
        
        self.islem_alani2 = QtWidgets.QLineEdit()
        
        self.temizle = QtWidgets.QPushButton("Kayıt ol")
        
        self.sonuc = QtWidgets.QLabel("Şifre")
        
        self.sonuc1 = QtWidgets.QLabel("Şifre tekrar")
        
        self.hsp = QtWidgets.QLabel("Kullanıcı adı")
        
        self.islem_alanii = QtWidgets.QLineEdit()
        
        self.etiket = QtWidgets.QLabel()
        
        self.etiket.setPixmap(QtGui.QPixmap("demir.png"))
        
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addStretch()
        
        v_box.addWidget(self.etiket)
        
        v_box.addWidget(self.hsp)
        
        v_box.addWidget(self.islem_alani3)
        
        v_box.addWidget(self.sonuc)
        
        v_box.addWidget(self.islem_alani2)
        
        v_box.addWidget(self.sonuc1)
        
        v_box.addWidget(self.islem_alanii)
        
        v_box.addWidget(self.temizle)
        
        v_box.addStretch()
        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addStretch()
        
        h_box.addLayout(v_box)
        
        h_box.addStretch()
        
        self.setLayout(h_box)
        
        
        self.temizle.clicked.connect(self.click2)
        
        self.show()
              
    
    def click2(self):
        
        global veri
        
        self.asd = 0
            
        if len(self.islem_alani3.text()) < 5:
                
            self.temizle.setText("HATA! Kullanıcı adı 5 karektere eşit veya büyük olmalı. ")
            
            self.asd = 1
            
        if self.asd == 0:
            
            for i in veri.kullanici_adi:
            
                if i == self.islem_alani3.text():
                   
                    self.temizle.setText("HATA! bu kullanıcı adı daha önceden alınmış.")
                    
                    self.asd = 1
                    
                    break
                
                
            if self.asd == 0:
                
                if self.islem_alani2.text() != self.islem_alanii.text():
                    
                    self.temizle.setText("HATA! Şifreler uyuşmamaktadır.")
                    
                    self.asd = 1
                        
                if self.asd == 0:
                        
                    if len(self.islem_alani2.text()) <=8:
                        
                        self.temizle.setText("HATA! Şifre karekter sayısı 8 e eşit veya büyük olmalı.")
                        
                        self.asd = 1

                    
                    if self.asd == 0:
                      
                        file = open('veri.csv','a')
                      
                        sifreee = self.islem_alani2.text()                    
                     
                        sifreleyici.update(sifreee.encode("utf-8"))
          
                      
                        hash = sifreleyici.hexdigest()
                     
                       
                        file.write(self.islem_alani3.text())
                       
                       
                        file.write(",")
                        
                       
                        file.write(hash)
                       
                        file.write("\n")
                        
                        file.close()
                       
                        veri = pd.read_csv('veri.csv')
                        
                        self.temizle.setText("Üyeliğiniz başarıyla yapılmıştır. Şimdi bu sekmeyi kapatıp, ana sayfadan giriş yapabilirsiniz.")


    def ozellik(self):
        
        
        self.setGeometry(200,200,400,400)
        
        self.setWindowTitle("DEMIR")
        
        self.islem_alani = QtWidgets.QLineEdit()
        
        self.hesapla = QtWidgets.QPushButton("Giriş")
        
        self.temizle = QtWidgets.QPushButton("Kayıt ol")
        
        self.sonuc = QtWidgets.QLabel("Şifre")
        
        self.hsp = QtWidgets.QLabel("Kullanıcı adı")
        
        self.islem_alanii = QtWidgets.QLineEdit()
        
        self.etiket = QtWidgets.QLabel()
        
        self.etiket.setPixmap(QtGui.QPixmap("demir.png"))
        
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addStretch()
        
        v_box.addWidget(self.etiket)
        
        v_box.addWidget(self.hsp)
        
        v_box.addWidget(self.islem_alani)
        
        v_box.addWidget(self.sonuc)
        
        v_box.addWidget(self.islem_alanii)
        
        v_box.addWidget(self.hesapla)
        
        v_box.addWidget(self.temizle)
        
        v_box.addStretch()
        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addStretch()
        
        h_box.addLayout(v_box)
        
        h_box.addStretch()
        
        self.setLayout(h_box)
        
        self.hesapla.clicked.connect(self.click)
        
        self.temizle.clicked.connect(self.click)
        
        self.show()
    
    
    def click(self):
        
        tıkla = self.sender()
        
        if tıkla.text() == "Giriş" or tıkla.text() == "Giriş Başarılı" or tıkla.text() == "Hatalı Kullanıcı adı" or tıkla.text() == "Hatalı şifre":
            
           self.hesaplaa()
            
            
        else:
            
            super().__init__()
            
            self.ozellik1()
            

    def hesaplaa(self):
        
        self.kontrol = 0
        
        global veri
        
        print("veri = ",veri.kullanici_adi)
        print("sen = ",self.islem_alani.text())
        
        
        for i in veri.kullanici_adi:
            
            if i == self.islem_alani.text():
                
                self.kontrol = 1
                
                self.asdd = i
                
                break
            
            else:
                
                self.hesapla.setText("Hatalı Kullanıcı adı")
            
            
        if self.kontrol == 1:
            
            sifreleyici1 = hasher.sha256()
            
            sifree = self.islem_alanii.text()
            
            sifreleyici1.update(sifree.encode("utf-8"))
            
            hash = sifreleyici1.hexdigest()
            
            
            for i in veri.sifre:
                
                
                if i == hash:
                    
                    self.hesapla.setText("Giriş Başarılı")
                    
                    super().__init__()
                    
                    self.maina(self.asdd)
                    
                    
                else:
                    
                    self.hesapla.setText("Hatalı şifre")
                    
                    
    def maina(self,asdd):
        
        self.setGeometry(200,200,600,400)
        
        self.setWindowTitle("DEMIR [ ID = {} ]".format(asdd))
        
        self.show()
        
           
uygulama = QtWidgets.QApplication(sys.argv)

pencere = Pencere()


sys.exit(uygulama.exec__())