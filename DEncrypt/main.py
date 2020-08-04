from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import QFileDialog
import a,s
import hashlib as hasher
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow

class Ui1_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(797, 508)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 160, 321, 81))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(390, 260, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 260, 91, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 320, 321, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(692, 464, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.graphicsView = QtWidgets.QLabel(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(202, 10, 370, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setPixmap(QtGui.QPixmap("images/demir.png"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Çözülecek Resim Dosyası (.demir) Seç"))
        self.label.setFont(QtGui.QFont('SansSerif', 15))
        self.label.setText(_translate("Dialog", "Şifre : "))
        self.pushButton_2.setText(_translate("Dialog", "Çöz"))
        self.pushButton_3.setText(_translate("Dialog", "Ana menü"))


        self.pushButton.clicked.connect(self.clicka)
        self.pushButton_2.clicked.connect(self.clickb)
        self.pushButton_3.clicked.connect(self.clickc)

    def clicka(self):

        print(os.getcwd())
        self.dosya_ismi = QFileDialog.getOpenFileName(os.getenv("Masaüstü"))

        kontrol = ".demir" in self.dosya_ismi[0]

        if kontrol == True:

        	self.pushButton.setText("Çözülecek Dosya Seçildi")

        else:
        	self.pushButton.setText("Hatalı Dosya!!, Tekrar Deneyiniz")



    def clickb(self):

    	if self.pushButton.text() != "Çözülecek Dosya Seçildi":
    		self.pushButton_2.setText("Hata!!")


    	elif self.pushButton.text() == "Çözülecek Dosya Seçildi":
        
	        self.sifre = self.lineEdit.text()

	        self.sifreleyici = hasher.sha256()
	        self.sifreleyici.update(self.sifre.encode("utf-8"))
	        hash = self.sifreleyici.hexdigest()

	        kn = s.main(hash, self.dosya_ismi[0])

	        if kn == 0:

	        	self.pushButton_2.setText("Başarılı!!, \"out\" klasörünü kontrol ediniz")

	        elif kn == -5:

	        	self.pushButton_2.setText("Hata!!, Şifre hatalı")

	        elif kn == -3:

	        	self.pushButton_2.setText("Hata!!")
	        	

    def clickc(self):
    	
        ui.mainwin.hide()
        Dialog.hide()
        
        Dialog.show()


class Ui0_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(797, 508)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 160, 321, 81))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(390, 260, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 260, 91, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 320, 321, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(692, 464, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.graphicsView = QtWidgets.QLabel(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(202, 10, 370, 131))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setPixmap(QtGui.QPixmap("images/demir.png"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Şifrelenecek Resim Dosyası Seç"))
        self.label.setFont(QtGui.QFont('SansSerif', 15))
        self.label.setText(_translate("Dialog", "Şifre : "))
        self.pushButton_2.setText(_translate("Dialog", "Şifrele"))
        self.pushButton_3.setText(_translate("Dialog", "Ana menü"))


        self.pushButton.clicked.connect(self.clicka)
        self.pushButton_2.clicked.connect(self.clickb)
        self.pushButton_3.clicked.connect(self.clickc)

    def clicka(self):

        print(os.getcwd())
        self.dosya_ismi = QFileDialog.getOpenFileName(os.getenv("Masaüstü"))

        kontrol = None

        try:
            
            self.image = Image.open(self.dosya_ismi[0])

        except:

            kontrol = False

            self.pushButton.setText("Hatalı Resim Türü!!, Yeni Bir Resim Seçiniz")

        if kontrol == None:

            self.pushButton.setText("Resim Başarıyla Seçildi")


    def clickb(self):
        
        self.sifre = self.lineEdit.text()

        if len(self.sifre) >=4 and len(self.sifre) <= 13:

            self.sifreleyici = hasher.sha256()
            self.sifreleyici.update(self.sifre.encode("utf-8"))
            hash = self.sifreleyici.hexdigest()

            if self.pushButton.text() == "Resim Başarıyla Seçildi":

            	a.main(self.image, hash)

            	self.pushButton_2.setText("Başarılı. (\"Sifreli\" Adlı Klasörü Kontrol Ediniz)")

            else:

            	self.pushButton_2.setText("Hata!!, Tekrar Deneyiniz")

        else:

            self.pushButton_2.setText("Şifre uzunluğu 3 ila 14 arasında olamlı")

    def clickc(self):
    	
        ui.mainwin.hide()
        Dialog.hide()
        
        Dialog.show()

class Ui_Dialog(object):

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(797, 508)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(-18, -6, 411, 521))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 0, 411, 521))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", ""))
        self.pushButton_2.setText(_translate("Dialog", ""))

        self.icon0 = QtGui.QPixmap('images/image0.png')
        self.pushButton.setIcon(QIcon(self.icon0))
        self.pushButton.setIconSize(QtCore.QSize(411,521))

        self.icon1 = QtGui.QPixmap('images/image1.png')
        self.pushButton_2.setIcon(QIcon(self.icon1))
        self.pushButton_2.setIconSize(QtCore.QSize(411,521))

        self.pushButton.clicked.connect(self.clicka)
        self.pushButton_2.clicked.connect(self.clickb)


    def clicka(self):

    	self.mainwin=QMainWindow()
    	self.ui=Ui0_Dialog()
    	self.ui.setupUi(self.mainwin)
    	self.mainwin.setWindowTitle("Encryption")
    	self.mainwin.setFixedSize(797, 508)
    	self.mainwin.move(300,100)
    	self.mainwin.show()
    	Dialog.hide()


    def clickb(self):

    	self.mainwin=QMainWindow()
    	self.ui=Ui1_Dialog()
    	self.ui.setupUi(self.mainwin)
    	self.mainwin.setWindowTitle("Decrypt")
    	self.mainwin.setFixedSize(797, 508)
    	self.mainwin.move(300,100)
    	self.mainwin.show()
    	Dialog.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("demir.ai")
    Dialog.setFixedSize(797, 508)
    Dialog.move(300,100)
    Dialog.show()
    sys.exit(app.exec_())
