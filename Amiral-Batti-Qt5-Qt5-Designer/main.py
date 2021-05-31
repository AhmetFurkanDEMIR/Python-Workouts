# Ahmet Furkan Demir 2020

import os
from time import sleep as sl
from random import randint as rn
import sys

clea = os.name # işletim sisteminizi öğrendim

if clea == "posix": # linux, mac 
    clear = "clear"

else: # windows

    clear = "cls"

try: # gerekli kütüphaneler varmı diye kontrol ettim

    import wget

    from PyQt5 import QtCore, QtGui, QtWidgets
    
    from PyQt5.QtWidgets import QMainWindow


except: # eğer olmadığına dair hata alırsam, modülleri bu blokta kurmaya başlayacağım

    print("\n\n  - Gerekli modüller bulunamadı.")
    sl(3)
    print("\n\n  - Modüller kuruluyor, lütfen bekleyiniz... (internet bağlantısı gerekli!!!) \n")
    sl(4)
    os.system("python -m pip install --upgrade pip")
    os.system("python3 -m pip install --upgrade pip")
    os.system("python -m pip install pyqt5")
    os.system("python3 -m pip install pyqt5")

    os.system("pip install vext.pyqt5")

    os.system("pip3 install PyQt5")

    os.system("pip3 install wget")

    import wget
    if not os.path.isfile(os.path.join("demir.png")):

    	# eğer oyunun başındaki resim kodla aynı dizinde değilse resmi indiriyorum

        print("\n EKSİK DOSYALAR İNDİRİLİYOR ....")
 

        file_url1 = "https://www.dropbox.com/s/p17t5e7b4cegk29/demir.png?dl=1"
        wget.download(file_url1)

    # programı tekrar çalıştırdığınızda tüm modüller yüklü olduğu için herhengi bir sorun çıkmayacaktır.    
    os.system(clear)
    print("\n\n  - Gerekli modüller kuruldu. Lütfen Programı tekrar çalıştırınız.\n\n") 
    quit()

if not os.path.isfile(os.path.join("demir.png")):

	# eğer oyunun başındaki resim kodla aynı dizinde değilse resmi indiriyorum

    print("\n EKSİK DOSYALAR İNDİRİLİYOR ....")
 
    file_url1 = "https://www.dropbox.com/s/p17t5e7b4cegk29/demir.png?dl=1"
    wget.download(file_url1)


# haritayı bu fonksiyonda yaptım
def map(md):

    global mod # oyunun açık veya gizli modda başlaması kontrolu için
    global gemiler # gemileri global yaptım çünki tüm sınıfların erişmesi gerek

    mod = md

    while True:

        kontrol = None

        a = rn(0,100) # ilk geminin başlangıç noktası

        b = rn(0,100) # ikinci geminin başlangıç noktası

        c = rn(0,100) # üçüncü geminin başlangıç noktası

        d = rn(0,100) # son geminin baslangıç noktası

        # burada random sayı listeden bir elemen seçecek
        rast = [1,10,-1,-10] 

        # seçtiği elemanlar başlangıç noktasından sonra nasıl ilerleneceği belirlenecek (dikey, yatay) 

        b1 = rast[rn(0,3)]

        c1 = rast[rn(0,3)]

        d1 = rast[rn(0,3)]

        gemiler = [a,[b,b+1*b1,b+2*b1],[c,c+1*c1,c+2*c1,c+3*c1],[d,d+1*d1]] # tüm gemileri listeye ekledim
        
        if (str(gemiler[1][0])[0] != str(gemiler[1][1])[0]) or (str(gemiler[1][1])[0] != str(gemiler[1][2])[0]) and (b1==1 or b1==-1):
        	# gemiler yataysa bir alt satıra geçmeme kontrolü(yatay gemilerin birleşik olma kontrolü) * dikey gemiler bu kontrole girmez
            continue

        elif ((str(gemiler[2][0])[0] !=  str(gemiler[2][1])[0]) or (str(gemiler[2][1])[0] != str(gemiler[2][2])[0]) or (str(gemiler[2][2])[0] != str(gemiler[2][3])[0])) and (c1==1 or c1==-1):
        	# gemiler yataysa bir alt satıra geçmeme kontrolü(yatay gemilerin birleşik olma kontrolü) * dikey gemiler bu kontrole girmez
            continue

        elif (str(gemiler[3][0])[0] != str(gemiler[3][1])[0]) and (d1==1 or d1==-1):
        	# gemiler yataysa bir alt satıra geçmeme kontrolü(yatay gemilerin birleşik olma kontrolü) * dikey gemiler bu kontrole girmez
            continue


        elif gemiler[0] >= 100 or gemiler[0] < 0:
        	# gemilerin başlangıç noktalarından sonraki gelen blokların 0,100 arasında olma kontrolü
            continue

        elif gemiler[1][2] >= 100 or gemiler[1][0] < 0 or gemiler[1][2] < 0:
        	# gemilerin başlangıç noktalarından sonraki gelen blokların 0,100 arasında olma kontrolü

            continue

        elif gemiler[2][3] >= 100 or gemiler[2][0] < 0 or gemiler[2][3] <0 :
        	# gemilerin başlangıç noktalarından sonraki gelen blokların 0,100 arasında olma kontrolü

            continue

        elif gemiler[3][1] >= 100 or gemiler[3][0] < 0 or gemiler[3][1] < 0:
        	# gemilerin başlangıç noktalarından sonraki gelen blokların 0,100 arasında olma kontrolü

            continue

        # aşağıdaki kontrol blokları gemiler çakışıyormu diye kontrol ediyor.    
        elif gemiler[0] in gemiler[1]: 
            # ilk gemi ikinci gemiyle çakışıyormu

            kontrol = False

        elif gemiler[0] in gemiler[2]:
            # ilk gemi üçüncü gemiyle çakışıyormu

            kontrol = False

        elif gemiler[0] in gemiler[3]:
            # ilk gemi dördüncü gemiyle çakışıyormu

            kontrol = False


        elif gemiler[1][0] in gemiler[2] or gemiler[1][1] in gemiler[2] or gemiler[1][2] in gemiler[2]:
            # ikinci gemi üçüncü gemiyle çakışıyormu

            kontrol = False

        elif gemiler[1][0] in gemiler[3] or gemiler[1][1] in gemiler[3] or gemiler[1][2] in gemiler[3]:
            # ikinci gemi dördüncü gemiyle çakışıyormu

            kontrol = False

        elif gemiler[3][0] in gemiler[2] or gemiler[3][1] in gemiler[2]:
            # dördüncü gemi ikinci gemiyle çakışıyormu

            kontrol = False

        # eğer hiçbir sorun yoksa gemiler adlı liste yaratılır.

        elif kontrol == None:
            
            break # döngüüden çıkılır


class Ui_Main(object): # giriş menüsü


    def setupUi(self, Dialog): # resim, butonlar, yazılar ve bunların boyutlarının tanımlanması, ekrandaki yerlerin ayarlanması

        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 564) # pencere boyutu
        self.graphicsView = QtWidgets.QLabel(Dialog) # ana ekrandaki resim
        self.graphicsView.setGeometry(QtCore.QRect(40, 20, 581, 421)) # resim boyutu
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(Dialog) # yazı yazdığım yerler
        self.label.setGeometry(QtCore.QRect(30, 460, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog) # yazı yazdığım yerler
        self.label_2.setGeometry(QtCore.QRect(107, 460, 64, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog) # gizli mod butonu
        self.pushButton.setGeometry(QtCore.QRect(30, 510, 83, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog) # açık mod butonu
        self.pushButton_2.setGeometry(QtCore.QRect(520, 510, 83, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView.setPixmap(QtGui.QPixmap("demir.png"))


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "MERHABA "))
        self.label_2.setText(os.getlogin()) # kullanıcı adınızı öğrenip ekrana yazdırdım.
        self.pushButton.setText(_translate("Dialog", "Gizli Mod"))
        self.pushButton_2.setText(_translate("Dialog", "Açık Mod"))

        self.pushButton.clicked.connect(self.click0) # gizli modda oyunu açma kısmına tıklarsanız click0 fonksiyonuna ilerler.

        self.pushButton_2.clicked.connect(self.click1) # açık modda oyunu açma kısmına tıklarsanız click1 fonksiyonuna ilerler


    def click0(self):

        mod = True # oyunu hangi modda açtığınızı kontrol  için
        map(mod) # yeni harita oluşturulur
        
        self.mainwin=QMainWindow()  
        self.ui=Ui_asdf()  
        self.ui.setupUi(self.mainwin) 
        self.mainwin.setFixedSize(649,582)
        self.mainwin.setWindowTitle("Amiral Battı - Gizli Mod") # başlık
        self.mainwin.show() # oyun haritası açılır
        asdf.hide() # eski ekran kaybolur

    def click1(self):

        mod = False # oyunu hangi modda açtığınızı kontrol  için
        map(mod) # yeni harita oluşturulur
        
        self.mainwin=QMainWindow()  
        self.ui=Ui_asdf()  
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setFixedSize(649,582)
        self.mainwin.setWindowTitle("Amiral Battı - Açık Mod") # başlık
        self.mainwin.show() # oyun haritası açılır	
        asdf.hide()	#eski ekran kaybolur


# oyun alanımız burası !!

class Ui_asdf(QtWidgets.QWidget): # Qtwidget modülnden miras alarak yeni bir sınıf oluşturuyoruz


    def setupUi(self,asdf): # butonlar, ekrandaki yerleri ve boyutları


        self.sayac = 33 # oyundaki hakkımız
        # ekran 10x10 luk olduğundan dolayı 100 buton var
        asdf.setObjectName("Gizli Mod") # baslik
        asdf.resize(649, 582) # ekran boyutu
        self.buton00 = QtWidgets.QPushButton(asdf) # buton tanımlama
        self.buton00.setGeometry(QtCore.QRect(40, 40, 31, 25)) # buton boyutu ve ekrandaki yeri
        self.buton00.setObjectName("buton00")
        self.buton90 = QtWidgets.QPushButton(asdf)
        self.buton90.setGeometry(QtCore.QRect(40, 490, 31, 25))
        self.buton90.setObjectName("buton90")
        self.buton80 = QtWidgets.QPushButton(asdf)
        self.buton80.setGeometry(QtCore.QRect(40, 440, 31, 25))
        self.buton80.setObjectName("buton80")
        self.buton70 = QtWidgets.QPushButton(asdf)
        self.buton70.setGeometry(QtCore.QRect(40, 390, 31, 25))
        self.buton70.setObjectName("buton70")
        self.buton60 = QtWidgets.QPushButton(asdf)
        self.buton60.setGeometry(QtCore.QRect(40, 340, 31, 25))
        self.buton60.setObjectName("buton60")
        self.buton50 = QtWidgets.QPushButton(asdf)
        self.buton50.setGeometry(QtCore.QRect(40, 290, 31, 25))
        self.buton50.setObjectName("buton50")
        self.buton40 = QtWidgets.QPushButton(asdf)
        self.buton40.setGeometry(QtCore.QRect(40, 240, 31, 25))
        self.buton40.setObjectName("buton40")
        self.buton30 = QtWidgets.QPushButton(asdf)
        self.buton30.setGeometry(QtCore.QRect(40, 190, 31, 25))
        self.buton30.setObjectName("buton30")
        self.buton20 = QtWidgets.QPushButton(asdf)
        self.buton20.setGeometry(QtCore.QRect(40, 140, 31, 25))
        self.buton20.setObjectName("buton20")
        self.buton10 = QtWidgets.QPushButton(asdf)
        self.buton10.setGeometry(QtCore.QRect(40, 90, 31, 25))
        self.buton10.setObjectName("buton10")
        self.buton41 = QtWidgets.QPushButton(asdf)
        self.buton41.setGeometry(QtCore.QRect(100, 240, 31, 25))
        self.buton41.setObjectName("buton41")
        self.buton21 = QtWidgets.QPushButton(asdf)
        self.buton21.setGeometry(QtCore.QRect(100, 140, 31, 25))
        self.buton21.setObjectName("buton21")
        self.buton11 = QtWidgets.QPushButton(asdf)
        self.buton11.setGeometry(QtCore.QRect(100, 90, 31, 25))
        self.buton11.setObjectName("buton11")
        self.buton31 = QtWidgets.QPushButton(asdf)
        self.buton31.setGeometry(QtCore.QRect(100, 190, 31, 25))
        self.buton31.setObjectName("buton31")
        self.buton71 = QtWidgets.QPushButton(asdf)
        self.buton71.setGeometry(QtCore.QRect(100, 390, 31, 25))
        self.buton71.setObjectName("buton71")
        self.buton91 = QtWidgets.QPushButton(asdf)
        self.buton91.setGeometry(QtCore.QRect(100, 490, 31, 25))
        self.buton91.setObjectName("buton91")
        self.buton61 = QtWidgets.QPushButton(asdf)
        self.buton61.setGeometry(QtCore.QRect(100, 340, 31, 25))
        self.buton61.setObjectName("buton61")
        self.buton51 = QtWidgets.QPushButton(asdf)
        self.buton51.setGeometry(QtCore.QRect(100, 290, 31, 25))
        self.buton51.setObjectName("buton51")
        self.buton01 = QtWidgets.QPushButton(asdf)
        self.buton01.setGeometry(QtCore.QRect(100, 40, 31, 25))
        self.buton01.setObjectName("buton01")
        self.buton81 = QtWidgets.QPushButton(asdf)
        self.buton81.setGeometry(QtCore.QRect(100, 440, 31, 25))
        self.buton81.setObjectName("buton81")
        self.buton42 = QtWidgets.QPushButton(asdf)
        self.buton42.setGeometry(QtCore.QRect(160, 240, 31, 25))
        self.buton42.setObjectName("buton42")
        self.buton22 = QtWidgets.QPushButton(asdf)
        self.buton22.setGeometry(QtCore.QRect(160, 140, 31, 25))
        self.buton22.setObjectName("buton22")
        self.buton12 = QtWidgets.QPushButton(asdf)
        self.buton12.setGeometry(QtCore.QRect(160, 90, 31, 25))
        self.buton12.setObjectName("buton12")
        self.buton32 = QtWidgets.QPushButton(asdf)
        self.buton32.setGeometry(QtCore.QRect(160, 190, 31, 25))
        self.buton32.setObjectName("buton32")
        self.buton72 = QtWidgets.QPushButton(asdf)
        self.buton72.setGeometry(QtCore.QRect(160, 390, 31, 25))
        self.buton72.setObjectName("buton72")
        self.buton92 = QtWidgets.QPushButton(asdf)
        self.buton92.setGeometry(QtCore.QRect(160, 490, 31, 25))
        self.buton92.setObjectName("buton92")
        self.buton62 = QtWidgets.QPushButton(asdf)
        self.buton62.setGeometry(QtCore.QRect(160, 340, 31, 25))
        self.buton62.setObjectName("buton62")
        self.buton52 = QtWidgets.QPushButton(asdf)
        self.buton52.setGeometry(QtCore.QRect(160, 290, 31, 25))
        self.buton52.setObjectName("buton52")
        self.buton02 = QtWidgets.QPushButton(asdf)
        self.buton02.setGeometry(QtCore.QRect(160, 40, 31, 25))
        self.buton02.setObjectName("buton02")
        self.buton82 = QtWidgets.QPushButton(asdf)
        self.buton82.setGeometry(QtCore.QRect(160, 440, 31, 25))
        self.buton82.setObjectName("buton82")
        self.buton43 = QtWidgets.QPushButton(asdf)
        self.buton43.setGeometry(QtCore.QRect(220, 240, 31, 25))
        self.buton43.setObjectName("buton43")
        self.buton23 = QtWidgets.QPushButton(asdf)
        self.buton23.setGeometry(QtCore.QRect(220, 140, 31, 25))
        self.buton23.setObjectName("buton23")
        self.buton13 = QtWidgets.QPushButton(asdf)
        self.buton13.setGeometry(QtCore.QRect(220, 90, 31, 25))
        self.buton13.setObjectName("buton13")
        self.buton33 = QtWidgets.QPushButton(asdf)
        self.buton33.setGeometry(QtCore.QRect(220, 190, 31, 25))
        self.buton33.setObjectName("buton33")
        self.buton73 = QtWidgets.QPushButton(asdf)
        self.buton73.setGeometry(QtCore.QRect(220, 390, 31, 25))
        self.buton73.setObjectName("buton73")
        self.buton93 = QtWidgets.QPushButton(asdf)
        self.buton93.setGeometry(QtCore.QRect(220, 490, 31, 25))
        self.buton93.setObjectName("buton93")
        self.buton63 = QtWidgets.QPushButton(asdf)
        self.buton63.setGeometry(QtCore.QRect(220, 340, 31, 25))
        self.buton63.setObjectName("buton63")
        self.buton53 = QtWidgets.QPushButton(asdf)
        self.buton53.setGeometry(QtCore.QRect(220, 290, 31, 25))
        self.buton53.setObjectName("buton53")
        self.buton03 = QtWidgets.QPushButton(asdf)
        self.buton03.setGeometry(QtCore.QRect(220, 40, 31, 25))
        self.buton03.setObjectName("buton03")
        self.buton83 = QtWidgets.QPushButton(asdf)
        self.buton83.setGeometry(QtCore.QRect(220, 440, 31, 25))
        self.buton83.setObjectName("buton83")
        self.buton44 = QtWidgets.QPushButton(asdf)
        self.buton44.setGeometry(QtCore.QRect(280, 240, 31, 25))
        self.buton44.setObjectName("buton44")
        self.buton24 = QtWidgets.QPushButton(asdf)
        self.buton24.setGeometry(QtCore.QRect(280, 140, 31, 25))
        self.buton24.setObjectName("buton24")
        self.buton14 = QtWidgets.QPushButton(asdf)
        self.buton14.setGeometry(QtCore.QRect(280, 90, 31, 25))
        self.buton14.setObjectName("buton14")
        self.buton34 = QtWidgets.QPushButton(asdf)
        self.buton34.setGeometry(QtCore.QRect(280, 190, 31, 25))
        self.buton34.setObjectName("buton34")
        self.buton74 = QtWidgets.QPushButton(asdf)
        self.buton74.setGeometry(QtCore.QRect(280, 390, 31, 25))
        self.buton74.setObjectName("buton74")
        self.buton94 = QtWidgets.QPushButton(asdf)
        self.buton94.setGeometry(QtCore.QRect(280, 490, 31, 25))
        self.buton94.setObjectName("buton94")
        self.buton64 = QtWidgets.QPushButton(asdf)
        self.buton64.setGeometry(QtCore.QRect(280, 340, 31, 25))
        self.buton64.setObjectName("buton64")
        self.buton54 = QtWidgets.QPushButton(asdf)
        self.buton54.setGeometry(QtCore.QRect(280, 290, 31, 25))
        self.buton54.setObjectName("buton54")
        self.buton04 = QtWidgets.QPushButton(asdf)
        self.buton04.setGeometry(QtCore.QRect(280, 40, 31, 25))
        self.buton04.setObjectName("buton04")
        self.buton84 = QtWidgets.QPushButton(asdf)
        self.buton84.setGeometry(QtCore.QRect(280, 440, 31, 25))
        self.buton84.setObjectName("buton84")
        self.buton45 = QtWidgets.QPushButton(asdf)
        self.buton45.setGeometry(QtCore.QRect(340, 240, 31, 25))
        self.buton45.setObjectName("buton45")
        self.buton25 = QtWidgets.QPushButton(asdf)
        self.buton25.setGeometry(QtCore.QRect(340, 140, 31, 25))
        self.buton25.setObjectName("buton25")
        self.buton15 = QtWidgets.QPushButton(asdf)
        self.buton15.setGeometry(QtCore.QRect(340, 90, 31, 25))
        self.buton15.setObjectName("buton15")
        self.buton35 = QtWidgets.QPushButton(asdf)
        self.buton35.setGeometry(QtCore.QRect(340, 190, 31, 25))
        self.buton35.setObjectName("buton35")
        self.buton75 = QtWidgets.QPushButton(asdf)
        self.buton75.setGeometry(QtCore.QRect(340, 390, 31, 25))
        self.buton75.setObjectName("buton75")
        self.buton95 = QtWidgets.QPushButton(asdf)
        self.buton95.setGeometry(QtCore.QRect(340, 490, 31, 25))
        self.buton95.setObjectName("buton95")
        self.buton65 = QtWidgets.QPushButton(asdf)
        self.buton65.setGeometry(QtCore.QRect(340, 340, 31, 25))
        self.buton65.setObjectName("buton65")
        self.buton55 = QtWidgets.QPushButton(asdf)
        self.buton55.setGeometry(QtCore.QRect(340, 290, 31, 25))
        self.buton55.setObjectName("buton55")
        self.buton05 = QtWidgets.QPushButton(asdf)
        self.buton05.setGeometry(QtCore.QRect(340, 40, 31, 25))
        self.buton05.setObjectName("buton05")
        self.buton85 = QtWidgets.QPushButton(asdf)
        self.buton85.setGeometry(QtCore.QRect(340, 440, 31, 25))
        self.buton85.setObjectName("buton85")
        self.buton46 = QtWidgets.QPushButton(asdf)
        self.buton46.setGeometry(QtCore.QRect(400, 240, 31, 25))
        self.buton46.setObjectName("buton46")
        self.buton26 = QtWidgets.QPushButton(asdf)
        self.buton26.setGeometry(QtCore.QRect(400, 140, 31, 25))
        self.buton26.setObjectName("buton26")
        self.buton16 = QtWidgets.QPushButton(asdf)
        self.buton16.setGeometry(QtCore.QRect(400, 90, 31, 25))
        self.buton16.setObjectName("buton16")
        self.buton36 = QtWidgets.QPushButton(asdf)
        self.buton36.setGeometry(QtCore.QRect(400, 190, 31, 25))
        self.buton36.setObjectName("buton36")
        self.buton76 = QtWidgets.QPushButton(asdf)
        self.buton76.setGeometry(QtCore.QRect(400, 390, 31, 25))
        self.buton76.setObjectName("buton76")
        self.buton96 = QtWidgets.QPushButton(asdf)
        self.buton96.setGeometry(QtCore.QRect(400, 490, 31, 25))
        self.buton96.setObjectName("buton96")
        self.buton66 = QtWidgets.QPushButton(asdf)
        self.buton66.setGeometry(QtCore.QRect(400, 340, 31, 25))
        self.buton66.setObjectName("buton66")
        self.buton56 = QtWidgets.QPushButton(asdf)
        self.buton56.setGeometry(QtCore.QRect(400, 290, 31, 25))
        self.buton56.setObjectName("buton56")
        self.buton06 = QtWidgets.QPushButton(asdf)
        self.buton06.setGeometry(QtCore.QRect(400, 40, 31, 25))
        self.buton06.setObjectName("buton06")
        self.buton86 = QtWidgets.QPushButton(asdf)
        self.buton86.setGeometry(QtCore.QRect(400, 440, 31, 25))
        self.buton86.setObjectName("buton86")
        self.buton47 = QtWidgets.QPushButton(asdf)
        self.buton47.setGeometry(QtCore.QRect(460, 240, 31, 25))
        self.buton47.setObjectName("buton47")
        self.buton27 = QtWidgets.QPushButton(asdf)
        self.buton27.setGeometry(QtCore.QRect(460, 140, 31, 25))
        self.buton27.setObjectName("buton27")
        self.buton17 = QtWidgets.QPushButton(asdf)
        self.buton17.setGeometry(QtCore.QRect(460, 90, 31, 25))
        self.buton17.setObjectName("buton17")
        self.buton37 = QtWidgets.QPushButton(asdf)
        self.buton37.setGeometry(QtCore.QRect(460, 190, 31, 25))
        self.buton37.setObjectName("buton37")
        self.buton77 = QtWidgets.QPushButton(asdf)
        self.buton77.setGeometry(QtCore.QRect(460, 390, 31, 25))
        self.buton77.setObjectName("buton77")
        self.buton97 = QtWidgets.QPushButton(asdf)
        self.buton97.setGeometry(QtCore.QRect(460, 490, 31, 25))
        self.buton97.setObjectName("buton97")
        self.buton67 = QtWidgets.QPushButton(asdf)
        self.buton67.setGeometry(QtCore.QRect(460, 340, 31, 25))
        self.buton67.setObjectName("buton67")
        self.buton57 = QtWidgets.QPushButton(asdf)
        self.buton57.setGeometry(QtCore.QRect(460, 290, 31, 25))
        self.buton57.setObjectName("buton57")
        self.buton07 = QtWidgets.QPushButton(asdf)
        self.buton07.setGeometry(QtCore.QRect(460, 40, 31, 25))
        self.buton07.setObjectName("buton07")
        self.buton87 = QtWidgets.QPushButton(asdf)
        self.buton87.setGeometry(QtCore.QRect(460, 440, 31, 25))
        self.buton87.setObjectName("buton87")
        self.buton48 = QtWidgets.QPushButton(asdf)
        self.buton48.setGeometry(QtCore.QRect(520, 240, 31, 25))
        self.buton48.setObjectName("buton48")
        self.buton28 = QtWidgets.QPushButton(asdf)
        self.buton28.setGeometry(QtCore.QRect(520, 140, 31, 25))
        self.buton28.setObjectName("buton28")
        self.buton18 = QtWidgets.QPushButton(asdf)
        self.buton18.setGeometry(QtCore.QRect(520, 90, 31, 25))
        self.buton18.setObjectName("buton18")
        self.buton38 = QtWidgets.QPushButton(asdf)
        self.buton38.setGeometry(QtCore.QRect(520, 190, 31, 25))
        self.buton38.setObjectName("buton38")
        self.buton78 = QtWidgets.QPushButton(asdf)
        self.buton78.setGeometry(QtCore.QRect(520, 390, 31, 25))
        self.buton78.setObjectName("buton78")
        self.buton98 = QtWidgets.QPushButton(asdf)
        self.buton98.setGeometry(QtCore.QRect(520, 490, 31, 25))
        self.buton98.setObjectName("buton98")
        self.buton68 = QtWidgets.QPushButton(asdf)
        self.buton68.setGeometry(QtCore.QRect(520, 340, 31, 25))
        self.buton68.setObjectName("buton68")
        self.buton58 = QtWidgets.QPushButton(asdf)
        self.buton58.setGeometry(QtCore.QRect(520, 290, 31, 25))
        self.buton58.setObjectName("buton58")
        self.buton08 = QtWidgets.QPushButton(asdf)
        self.buton08.setGeometry(QtCore.QRect(520, 40, 31, 25))
        self.buton08.setObjectName("buton08")
        self.buton88 = QtWidgets.QPushButton(asdf)
        self.buton88.setGeometry(QtCore.QRect(520, 440, 31, 25))
        self.buton88.setObjectName("buton88")
        self.buton49 = QtWidgets.QPushButton(asdf)
        self.buton49.setGeometry(QtCore.QRect(580, 240, 31, 25))
        self.buton49.setObjectName("buton49")
        self.buton29 = QtWidgets.QPushButton(asdf)
        self.buton29.setGeometry(QtCore.QRect(580, 140, 31, 25))
        self.buton29.setObjectName("buton29")
        self.buton19 = QtWidgets.QPushButton(asdf)
        self.buton19.setGeometry(QtCore.QRect(580, 90, 31, 25))
        self.buton19.setObjectName("buton19")
        self.buton39 = QtWidgets.QPushButton(asdf)
        self.buton39.setGeometry(QtCore.QRect(580, 190, 31, 25))
        self.buton39.setObjectName("buton39")
        self.buton79 = QtWidgets.QPushButton(asdf)
        self.buton79.setGeometry(QtCore.QRect(580, 390, 31, 25))
        self.buton79.setObjectName("buton79")
        self.buton99 = QtWidgets.QPushButton(asdf)
        self.buton99.setGeometry(QtCore.QRect(580, 490, 31, 25))
        self.buton99.setObjectName("buton99")
        self.buton69 = QtWidgets.QPushButton(asdf)
        self.buton69.setGeometry(QtCore.QRect(580, 340, 31, 25))
        self.buton69.setObjectName("buton69")
        self.buton59 = QtWidgets.QPushButton(asdf)
        self.buton59.setGeometry(QtCore.QRect(580, 290, 31, 25))
        self.buton59.setObjectName("buton59")
        self.buton09 = QtWidgets.QPushButton(asdf)
        self.buton09.setGeometry(QtCore.QRect(580, 40, 31, 25))
        self.buton09.setObjectName("buton09")
        self.buton89 = QtWidgets.QPushButton(asdf)
        self.buton89.setGeometry(QtCore.QRect(580, 440, 31, 25))
        self.buton89.setObjectName("buton89")
        self.label = QtWidgets.QLabel(asdf)
        self.label.setGeometry(QtCore.QRect(250, 540, 301, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(asdf)
        self.label_2.setGeometry(QtCore.QRect(40, 540, 200, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(asdf) # ana menüye dönme butonu
        self.pushButton.setGeometry(QtCore.QRect(532, 540, 83, 20))
        self.pushButton.setObjectName("pushButton")


        self.retranslateUi(asdf)
        QtCore.QMetaObject.connectSlotsByName(asdf)

    # buton textleri ve butonları listeye ekleme.
    def retranslateUi(self, asdf):

    	# butonların metni ve indexleri [9][5] gibi 
        self.butonlar = [] # oluşturulan butonların hepsini listeye ekleyeceğim
        _translate = QtCore.QCoreApplication.translate
        asdf.setWindowTitle(_translate("asdf", "Dialog"))
        self.buton00.setText(_translate("asdf", "       ?   00"))
        # butonları listeye ekliyorum
        self.butonlar.append(self.buton00) 
        self.buton90.setText(_translate("asdf", "       ?   90"))
        self.butonlar.append(self.buton01)
        # butonda ? işareti gözükecek (haritada ? göreceksiniz.), ve bu buton [8][0] olacak, yani ilk rakam satır ikinci rakam sütun(80) 
        self.buton80.setText(_translate("asdf", "       ?   80")) 
        self.butonlar.append(self.buton02)
        self.buton70.setText(_translate("asdf", "       ?   70")) # [7][0]
        self.butonlar.append(self.buton03)
        self.buton60.setText(_translate("asdf", "       ?   60")) # [6][0]
        self.butonlar.append(self.buton04)
        self.buton50.setText(_translate("asdf", "       ?   50")) # [5][0] gibi
        self.butonlar.append(self.buton05)
        self.buton40.setText(_translate("asdf", "       ?   40"))
        self.butonlar.append(self.buton06)
        self.buton30.setText(_translate("asdf", "       ?   30"))
        self.butonlar.append(self.buton07)
        self.buton20.setText(_translate("asdf", "       ?   20"))
        self.butonlar.append(self.buton08)
        self.buton10.setText(_translate("asdf", "       ?   10"))
        self.butonlar.append(self.buton09)
        self.buton41.setText(_translate("asdf", "       ?   41"))
        self.butonlar.append(self.buton10)
        self.buton21.setText(_translate("asdf", "       ?   21"))
        self.butonlar.append(self.buton11)
        self.buton11.setText(_translate("asdf", "       ?   11"))
        self.butonlar.append(self.buton12)
        self.buton31.setText(_translate("asdf", "       ?   31"))
        self.butonlar.append(self.buton13)
        self.buton71.setText(_translate("asdf", "       ?   71"))
        self.butonlar.append(self.buton14)
        self.buton91.setText(_translate("asdf", "       ?   91"))
        self.butonlar.append(self.buton15)
        self.buton61.setText(_translate("asdf", "       ?   61"))
        self.butonlar.append(self.buton16)
        self.buton51.setText(_translate("asdf", "       ?   51"))
        self.butonlar.append(self.buton17)
        self.buton01.setText(_translate("asdf", "       ?   01"))
        self.butonlar.append(self.buton18)
        self.buton81.setText(_translate("asdf", "       ?   81"))
        self.butonlar.append(self.buton19)
        self.buton42.setText(_translate("asdf", "       ?   42"))
        self.butonlar.append(self.buton20)
        self.buton22.setText(_translate("asdf", "       ?   22"))
        self.butonlar.append(self.buton21)
        self.buton12.setText(_translate("asdf", "       ?   12"))
        self.butonlar.append(self.buton22)
        self.buton32.setText(_translate("asdf", "       ?   32"))
        self.butonlar.append(self.buton23)
        self.buton72.setText(_translate("asdf", "       ?   72"))
        self.butonlar.append(self.buton24)
        self.buton92.setText(_translate("asdf", "       ?   92"))
        self.butonlar.append(self.buton25)
        self.buton62.setText(_translate("asdf", "       ?   62"))
        self.butonlar.append(self.buton26)
        self.buton52.setText(_translate("asdf", "       ?   52"))
        self.butonlar.append(self.buton27)
        self.buton02.setText(_translate("asdf", "       ?   02"))
        self.butonlar.append(self.buton28)
        self.buton82.setText(_translate("asdf", "       ?   82"))
        self.butonlar.append(self.buton29)
        self.buton43.setText(_translate("asdf", "       ?   43"))
        self.butonlar.append(self.buton30)
        self.buton23.setText(_translate("asdf", "       ?   23"))
        self.butonlar.append(self.buton31)
        self.buton13.setText(_translate("asdf", "       ?   13"))
        self.butonlar.append(self.buton32)
        self.buton33.setText(_translate("asdf", "       ?   33"))
        self.butonlar.append(self.buton33)
        self.buton73.setText(_translate("asdf", "       ?   73"))
        self.butonlar.append(self.buton34)
        self.buton93.setText(_translate("asdf", "       ?   93"))
        self.butonlar.append(self.buton35)
        self.buton63.setText(_translate("asdf", "       ?   63"))
        self.butonlar.append(self.buton36)
        self.buton53.setText(_translate("asdf", "       ?   53"))
        self.butonlar.append(self.buton37)
        self.buton03.setText(_translate("asdf", "       ?   03"))
        self.butonlar.append(self.buton38)
        self.buton83.setText(_translate("asdf", "       ?   83"))
        self.butonlar.append(self.buton39)
        self.buton44.setText(_translate("asdf", "       ?   44"))
        self.butonlar.append(self.buton40)
        self.buton24.setText(_translate("asdf", "       ?   24"))
        self.butonlar.append(self.buton41)
        self.buton14.setText(_translate("asdf", "       ?   14"))
        self.butonlar.append(self.buton42)
        self.buton34.setText(_translate("asdf", "       ?   34"))
        self.butonlar.append(self.buton43)
        self.buton74.setText(_translate("asdf", "       ?   74"))
        self.butonlar.append(self.buton44)
        self.buton94.setText(_translate("asdf", "       ?   94"))
        self.butonlar.append(self.buton45)
        self.buton64.setText(_translate("asdf", "       ?   64"))
        self.butonlar.append(self.buton46)
        self.buton54.setText(_translate("asdf", "       ?   54"))
        self.butonlar.append(self.buton47)
        self.buton04.setText(_translate("asdf", "       ?   04"))
        self.butonlar.append(self.buton48)
        self.buton84.setText(_translate("asdf", "       ?   84"))
        self.butonlar.append(self.buton49)
        self.buton45.setText(_translate("asdf", "       ?   45"))
        self.butonlar.append(self.buton50)
        self.buton25.setText(_translate("asdf", "       ?   25"))
        self.butonlar.append(self.buton51)
        self.buton15.setText(_translate("asdf", "       ?   15"))
        self.butonlar.append(self.buton52)
        self.buton35.setText(_translate("asdf", "       ?   35"))
        self.butonlar.append(self.buton53)
        self.buton75.setText(_translate("asdf", "       ?   75"))
        self.butonlar.append(self.buton54)
        self.buton95.setText(_translate("asdf", "       ?   95"))
        self.butonlar.append(self.buton55)
        self.buton65.setText(_translate("asdf", "       ?   65"))
        self.butonlar.append(self.buton56)
        self.buton55.setText(_translate("asdf", "       ?   55"))
        self.butonlar.append(self.buton57)
        self.buton05.setText(_translate("asdf", "       ?   05"))
        self.butonlar.append(self.buton58)
        self.buton85.setText(_translate("asdf", "       ?   85"))
        self.butonlar.append(self.buton59)
        self.buton46.setText(_translate("asdf", "       ?   46"))
        self.butonlar.append(self.buton60)
        self.buton26.setText(_translate("asdf", "       ?   26"))
        self.butonlar.append(self.buton61)
        self.buton16.setText(_translate("asdf", "       ?   16"))
        self.butonlar.append(self.buton62)
        self.buton36.setText(_translate("asdf", "       ?   36"))
        self.butonlar.append(self.buton63)
        self.buton76.setText(_translate("asdf", "       ?   76"))
        self.butonlar.append(self.buton64)
        self.buton96.setText(_translate("asdf", "       ?   96"))
        self.butonlar.append(self.buton65)
        self.buton66.setText(_translate("asdf", "       ?   66"))
        self.butonlar.append(self.buton66)
        self.buton56.setText(_translate("asdf", "       ?   56"))
        self.butonlar.append(self.buton67)
        self.buton06.setText(_translate("asdf", "       ?   06"))
        self.butonlar.append(self.buton68)
        self.buton86.setText(_translate("asdf", "       ?   86"))
        self.butonlar.append(self.buton69)
        self.buton47.setText(_translate("asdf", "       ?   47"))
        self.butonlar.append(self.buton70)
        self.buton27.setText(_translate("asdf", "       ?   27"))
        self.butonlar.append(self.buton71)
        self.buton17.setText(_translate("asdf", "       ?   17"))
        self.butonlar.append(self.buton72)
        self.buton37.setText(_translate("asdf", "       ?   37"))
        self.butonlar.append(self.buton73)
        self.buton77.setText(_translate("asdf", "       ?   77"))
        self.butonlar.append(self.buton74)
        self.buton97.setText(_translate("asdf", "       ?   97"))
        self.butonlar.append(self.buton75)
        self.buton67.setText(_translate("asdf", "       ?   67"))
        self.butonlar.append(self.buton76)
        self.buton57.setText(_translate("asdf", "       ?   57"))
        self.butonlar.append(self.buton77)
        self.buton07.setText(_translate("asdf", "       ?   07"))
        self.butonlar.append(self.buton78)
        self.buton87.setText(_translate("asdf", "       ?   87"))
        self.butonlar.append(self.buton79)
        self.buton48.setText(_translate("asdf", "       ?   48"))
        self.butonlar.append(self.buton80)
        self.buton28.setText(_translate("asdf", "       ?   28"))
        self.butonlar.append(self.buton81)
        self.buton18.setText(_translate("asdf", "       ?   18"))
        self.butonlar.append(self.buton82)
        self.buton38.setText(_translate("asdf", "       ?   38"))
        self.butonlar.append(self.buton83)
        self.buton78.setText(_translate("asdf", "       ?   78"))
        self.butonlar.append(self.buton84)
        self.buton98.setText(_translate("asdf", "       ?   98"))
        self.butonlar.append(self.buton85)
        self.buton68.setText(_translate("asdf", "       ?   68"))
        self.butonlar.append(self.buton86)
        self.buton58.setText(_translate("asdf", "       ?   58"))
        self.butonlar.append(self.buton87)
        self.buton08.setText(_translate("asdf", "       ?   08"))
        self.butonlar.append(self.buton88)
        self.buton88.setText(_translate("asdf", "       ?   88"))
        self.butonlar.append(self.buton89)
        self.buton49.setText(_translate("asdf", "       ?   49"))
        self.butonlar.append(self.buton90)
        self.buton29.setText(_translate("asdf", "       ?   29"))
        self.butonlar.append(self.buton91)
        self.buton19.setText(_translate("asdf", "       ?   19"))
        self.butonlar.append(self.buton92)
        self.buton39.setText(_translate("asdf", "       ?   39"))
        self.butonlar.append(self.buton93)
        self.buton79.setText(_translate("asdf", "       ?   79"))
        self.butonlar.append(self.buton94)
        self.buton99.setText(_translate("asdf", "       ?   99"))
        self.butonlar.append(self.buton95)
        self.buton69.setText(_translate("asdf", "       ?   69"))
        self.butonlar.append(self.buton96)
        self.buton59.setText(_translate("asdf", "       ?   59"))
        self.butonlar.append(self.buton97)
        self.buton09.setText(_translate("asdf", "       ?   09"))
        self.butonlar.append(self.buton98)
        self.buton89.setText(_translate("asdf", "       ?   89"))
        self.butonlar.append(self.buton99)
        self.label_2.setText(_translate("asdf", "Kalan Hamle Hakkınız : {} ".format(self.sayac))) # kalan hakkı ekranda gösteren label
        self.pushButton.setText(_translate("asdf", "Ana Menü")) # ana menü butonu

        # gemilerin tamamen batma, oyunu bitirme gibi kontroller
        self.kontrola = 0
        self.kontrolb = 0
        self.kontrolc = 0
        self.kontrold = 0
        self.toplam = 0
        self.ukontrol = None

        if mod == False: # eğer açık moddaysa bu bloğa girecek değilse devam edecek, gemilerin yerlerini belli ettim

            for self.i in self.butonlar: # listedeki tüm butonları aldım

                self.a1 = self.i.text()[11] # butonda yazan yazının 11. indexdeki rakam butonun satırı demektir
                self.a2 = self.i.text()[12] # butonda yazan yazının 12. indexdeki rakam butonun sütunu demektir
                self.c1 = self.a1+self.a2

                self.c2 = int(self.c1) # satir ve sütünü birleştirip tipinin değiştirdik.

                if self.c2 in gemiler: # gemileri açık modda olduğu için renklendirdik.

                    self.i.setStyleSheet("background-color: blue")

                elif self.c2 in gemiler[1]:

                    self.i.setStyleSheet("background-color: purple")

                elif self.c2 in gemiler[2]:

                    self.i.setStyleSheet("background-color: yellow")

                elif self.c2 in gemiler[3]:

                    self.i.setStyleSheet("background-color: orange")

                    
        for self.i in self.butonlar: # 100 adet butonun hangisine tıklandıysa clicka fonksiyonuna ilerlenecek

        	self.i.clicked.connect(self.clicka)

        self.pushButton.clicked.connect(self.maa) # ana menüye tıklanma butonu


    # oyun haritası gemilerin vurulma kontrolü !!!!
    def clicka(self,asd):

    	# oyuncunun oyun hakkı varsa girer yoksa girmez
        if self.sayac != 0:

        	# sender ile hangi butonun tıkladığını öğrendim
            self.sendera = self.sender()

            # oyuncunun daha önceden atış yaptığı bloklara tıklarsa girmez. oyun bittiyse giremez
            if (self.sendera.text()[3] != "X") and (self.sendera.text()[3] != "*") and self.toplam != 10: 

                # burada butonun konumunu öğrendim
                self.i = self.sendera.text()[11] # tıklanan butonun satırı
                self.j = self.sendera.text()[12] # tıklanan butonun sütunu

                self.a = self.i+self.j
                self.a = int(self.a) # satir+sutun

                # aşağıdaki şart bloklarında ise butonun konumu ile gemilerin konumu aynımı diye bakıyorum.
                if self.a == gemiler[0]: 
                	# eğerbuton ilk gemiyi vurduysa (1 birimlik) butonun rengi ve texti değişecek
                    self.v = "   X   ".format(self.a)

                    # gemiyi batırdığı için mesaj
                    self.label.setText("Tebrikler Bir -Gemi Batırdınız !!!")
                    # bir birimlik olduğu için direk batırdınız yazdım.

                    self.sendera.setStyleSheet("background-color: green")

                    self.label.setStyleSheet('color: green')

                    self.sendera.setText(self.v)

                    self.kontrold += 1 # ilk (1 birimlik gemi) battığını kaydettim

                elif (self.a == gemiler[1][0]) or (self.a == gemiler[1][1]) or (self.a == gemiler[1][2]): # diğer (3 birimlik gemiyi vurduysa girecek)

                    self.v = "   X   ".format(self.a) # vurunca butononun metni değişecek

                    self.label.setText("Tebrikler Bir Gemi Vurdunuz !!!") # gemiyi vurma mesajı

                    self.sendera.setStyleSheet("background-color: green")

                    self.label.setStyleSheet('color: blue')

                    self.kontrola += 1 # gemiyi tamamen batırma kontrolü

                    if self.kontrola == 3: # eğer 3 defa aynı gemiyi vurduysa gemiyi batırdınız yazacak

                        self.label.setText("Tebrikler Bir -Gemi Batırdınız !!!")

                        self.label.setStyleSheet('color: green')



                    self.sendera.setText(self.v)


                elif (self.a == gemiler[2][0]) or (self.a == gemiler[2][1]) or (self.a == gemiler[2][2]) or (self.a == gemiler[2][3]): # 4 birimlik gemiyi vurma kontrolü

                    self.v = "   X   ".format(self.a) # metin değişikliği

                    self.label.setText("Tebrikler Bir Gemi Vurdunuz !!!") # vurduysa mesaj

                    self.sendera.setStyleSheet("background-color: green")

                    self.label.setStyleSheet('color: blue')

                    self.kontrolb += 1 # gemiyi tamamen batırma kontrolü

                    if self.kontrolb == 4:

                        self.label.setText("Tebrikler Bir -Gemi Batırdınız !!!") # aynı gemiyi 4 kez vurduysa mesaj

                        self.label.setStyleSheet('color: green')

                    self.sendera.setText(self.v)


                elif (self.a == gemiler[3][0]) or (self.a == gemiler[3][1]): # 2 birimlik gemi vurma kontrolü

                    self.v = "   X   ".format(self.a) # metin değişikliği

                    self.label.setText("Tebrikler Bir Gemi Vurdunuz !!!") # geminin herhangi bir parçası vurulduysa

                    self.sendera.setStyleSheet("background-color: green")

                    self.label.setStyleSheet('color: blue')

                    self.kontrolc += 1 # gemiyi tamamen batırma kontrolü

                    if self.kontrolc == 2: # geminin tamamı vurulursa

                        self.label.setText("Tebrikler Bir -Gemi Batırdınız !!!")

                        self.label.setStyleSheet('color: green')


                    self.sendera.setText(self.v)


                else: # eğer atış yapılan noktada gemi yoksa yazı ve renk değiştirilir (isabetsiz atış)

                    self.v = "   *   ".format(self.a) # butonun metni

                    self.label.setText("Malesef İsabet Edemediniz !!!") # yeni metin

                    self.label.setStyleSheet('color: red')

                    self.sendera.setText(self.v)

                    self.sendera.setStyleSheet("background-color: red")



                self.sayac = self.sayac - 1 # kalan hamle hakkını azalttım

                self.label_2.setText("Kalan Hamle Hakkınız : {} ".format(self.sayac)) # kalan hamle hakkı



                if self.kontrold == 1 and self.kontrola == 3 and self.kontrolb == 4 and self.kontrolc == 2: # tüm gemileri vurma kontrolü yani kazanma

                    self.label.setText("Tebrikler Oyunu Kazandınız! Puan : {}".format(33-(33-self.sayac))) # oyunu kazandığına dair mesaj

                    self.label.setStyleSheet('color: green')

                    self.ukontrol = True

                    self.pushButton.setText("Yeni Oyun")

                    self.pushButton.setStyleSheet("background-color: green")

                    self.toplam = self.kontrola + self.kontrolc + self.kontrolb + self.kontrold


                elif self.sayac == 0:
                    # oyun hakkı kalmadıysa kaybettiniz yazısı

                    self.pushButton.setStyleSheet("background-color: red")

                    self.label.setText("Malesef Oyunu Kaybettiniz !!!")

                    self.label.setStyleSheet('color: red')

                    self.pushButton.setText("Yeni Oyun")


            else: # tıklanan butona tekrar tıklarsa

                if self.label.text != "Malesef Oyunu Kaybettiniz !!!" and self.ukontrol == None:

                    self.label.setText("Bu Alana Daha Önceden Atış Yapıldı!!!") # daha önceden atış yapılan noktaya tıklanırssa

                    self.label.setStyleSheet('color: red')


    def maa(self): # ana menüye dönme butonu


        try:
            ui.mainwin.hide()
            asdf.hide()

        except:

            pass

        asdf.show()


# argümanlar, pencerenin açılması ve yeni nesne yaratılması
# ekran boyutu ve pencere adı
# çıkış için gerekli fonksiyonlar
app = QtWidgets.QApplication(sys.argv)
asdf = QtWidgets.QDialog()
ui = Ui_Main()
ui.setupUi(asdf)
asdf.setFixedSize(667,564)
asdf.show()
asdf.setWindowTitle("Amiral Battı")
sys.exit(app.exec_())
