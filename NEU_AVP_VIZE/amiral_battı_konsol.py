# Ad,Soyad = Ahmet Furkan DEMIR , No = 19010011019

import os
from time import sleep as sl
from random import randint as rn

clea = os.name # işletim sisteminizi öğrendim

global clear

if clea == "posix": # linux, mac 
    clear = "clear"

else: # windows

    clear = "cls"

class Game(): # oyun sınıfı
    
    def __init__(self): # başlangıç fonksiyonu
        
        self.oyun()

    def oyun(self): # ana menü
        
        while True:
        
            os.system(clear)

            print("\n\n    --- Amiral Battı ---")

            print("\n\n     1-) Gizli Mod\n\n     2-) Açık Mod\n\n     Q-) Çıkış")

            self.secim = input("\n      Secim = ")

            if self.secim == "q" or self.secim == "Q":

                quit()

            elif self.secim != "1" and self.secim != "2" and self.secim != "q" and self.secim != "Q":

                continue

            break

        while True:

            os.system(clear)
            
            try:
                
                self.boyut = int(input("\n\n    Harita Boyutu (10 ve 10 dan büyük kare matris olmalı) = "))
                
                if self.boyut < 10:
                    
                    input("\033[31m"+"\n\n    HATA !!! Oyun ekranı Boyutu 10 ve 10 dan büyük kare matris olmalı. Devam etmek için Enter 'e basınız"+"\033[39m")

                    continue
                
            except:
                
                input("\033[31m"+"\n\n    HATA !!! Oyun ekranı Boyutu INT veri tipinde girmelisin. Devam etmek için Enter 'e basınız""\033[39m")

                continue

            self.map = []

            for self.i in range(0,self.boyut):

                self.gecici = []

                for self.j in range(0,self.boyut):

                    self.gecici.append("?")

                self.map.append(self.gecici)

            break


        if self.secim == "1":

            self.kontrolmod = True # oyun modu

            self.gemi() # gemileri oluşturma

            self.oyunn() # oyun ekranı

        elif self.secim == "2":

            self.kontrolmod = False

            self.gemi()

            self.oyunn()


    def oyunn(self): # oyun ekranı

        self.text = "Oyun Mesajları Burada Gözükecek. Ana menü için satir veya sütuna 'A' giriniz. "

        self.hak = self.boyut*self.boyut // 3

        self.kontrola = 0

        self.kontrolb = 0

        self.kontrolc = 0

        self.d = 0

        self.toplam = 0

        self.ilk = None

        while True:

            os.system(clear)

            print("\n\n    --- Amiral Battı --- ( {} )\n".format(self.text))

            print("     ",end="")

            for self.z in range(1,self.boyut+1):

            	print(" %.2d" % self.z,end="")

            print("\n")

            self.z = 0

            if self.kontrolmod == True: # kapalı mod, harita gösterme

                for self.i in range(0,self.boyut):

                    self.z += 1

                    print("\033[0m"+"  %.2d " % self.z,end="")

                    for self.j in range(0,self.boyut):

                        if self.map[self.i][self.j] == "X":

                            print("\033[92m"+" ",self.map[self.i][self.j],end="")

                        elif self.map[self.i][self.j] == "*":

                            print("\033[31m"+" ",self.map[self.i][self.j],end="")
                    
                        else:

                            print("\033[39m"+" ",self.map[self.i][self.j],end="")

                    print("")

            else: # açık mod, harita gösterme

                for self.i in range(0,self.boyut):

                    self.z += 1

                    print("\033[0m"+"  %.2d " % self.z,end="")

                    for self.j in range(0,self.boyut):

                        if self.i == self.gemiler[0][0] and self.j == self.gemiler[0][1]:

                            if self.ilk == None:
                                self.map[self.i][self.j] = "^"

                            print("\033[92m"+" ",self.map[self.i][self.j],end="")


                        elif (self.i == self.gemiler[1][0] and self.j == self.gemiler[1][1]) or (self.i == self.gemiler[1][2] and self.j == self.gemiler[1][3]):

                            if self.ilk == None:
                                
                                self.map[self.i][self.j] = "^"
                        	
                            print("\033[92m"+" ",self.map[self.i][self.j],end="")


                        elif (self.i == self.gemiler[2][0] and self.j == self.gemiler[2][1]) or (self.i == self.gemiler[2][2] and self.j == self.gemiler[2][3]) or (self.i == self.gemiler[2][4] and self.j == self.gemiler[2][5]):

                            if self.ilk == None:

                                self.map[self.i][self.j] = "^"

                            print("\033[92m"+" ",self.map[self.i][self.j],end="")


                        elif (self.i == self.gemiler[3][0] and self.j == self.gemiler[3][1]) or (self.i == self.gemiler[3][2] and self.j == self.gemiler[3][3]) or (self.i == self.gemiler[3][4] and self.j == self.gemiler[3][5]) or (self.i == self.gemiler[3][6] and self.j == self.gemiler[3][7]):

                            if self.ilk == None:

                                self.map[self.i][self.j] = "^"

                            print("\033[92m" + " ", self.map[self.i][self.j], end="")

                        elif self.map[self.i][self.j] == "*":

                            print("\033[31m"+" ",self.map[self.i][self.j],end="")
                    
                        else:
                            print("\033[39m"+" ",self.map[self.i][self.j],end="")

                    

                    print("")

            self.ilk = True

            print("\033[0m"+"\n    ","\033[32m"+"Kalan Hakkınız = {}".format(self.hak))


            self.satir = input("\033[39m"+"\n\n     Satır Giriniz = ")

            self.sutun = input("\n\n     Sütün Giriniz = ")

            # oyun anında satir veya sutuna "a","A" girerseniz ana menüye döner.

            if self.satir == "a" or self.satir == "A" or self.sutun == "a" or self.sutun == "A":

            	self.oyun()


            try:

                self.map[int(self.satir)-1][int(self.sutun)-1]

            except IndexError:

                self.text = "\033[31m"+"Lütfen Atışlarınız Matris Sınırları İçerisinde Olsun"+"\033[39m"

                continue

            except ValueError:

                self.text = "\033[31m"+"Lütfen Satır Ve Sütün Olarak INT(sayı) Değerler Girininz"+"\033[39m"

                continue


            if self.map[int(self.satir)-1][int(self.sutun)-1] == "?" or self.map[int(self.satir)-1][int(self.sutun)-1] == "^": # daha önce atış yaptığı yere tekrar atış yapmazsa girer

                self.satir = int(self.satir) - 1

                self.sutun = int(self.sutun) - 1

                if self.satir <=-1 or self.sutun <= -1:

                	self.text = "\033[31m"+"Lütfen Atışlarınız Matris Sınırları İçerisinde Olsun"+"\033[39m"

                	continue

                if self.satir == self.gemiler[0][0] and self.sutun == self.gemiler[0][1]: # bir birimlik gemi batırma

                    self.map[int(self.satir)][int(self.sutun)] = "X"

                    self.text = "\033[32m"+"Tebrikler Bir - Gemi Batırdınız (Alabora) -"+"\033[39m"

                    self.hak -= 1

                    self.d += 1

                elif (self.satir == self.gemiler[1][0] and self.sutun == self.gemiler[1][1]) or (self.satir == self.gemiler[1][2] and self.sutun == self.gemiler[1][3]):

                    # iki birimlik gemi batırma ve vurma kontrolü

                    self.map[int(self.satir)][int(self.sutun)] = "X"

                    self.text = "\033[36m"+"Tebrikler Bir Gemi Vurdunuz"+"\033[39m"

                    self.kontrola += 1

                    self.hak -= 1

                    if self.kontrola == 2:

                        self.text = "\033[32m"+"Tebrikler Bir - Gemi Batırdınız (Alabora) -"+"\033[39m"


                elif (self.satir == self.gemiler[2][0] and self.sutun == self.gemiler[2][1]) or (self.satir == self.gemiler[2][2] and self.sutun == self.gemiler[2][3]) or (self.satir == self.gemiler[2][4] and self.sutun == self.gemiler[2][5]):

                    # üç birimlik gemi batırma ve vurma kontrolü

                    self.map[int(self.satir)][int(self.sutun)] = "X"

                    self.text = "\033[36m"+"Tebrikler Bir Gemi Vurdunuz"+"\033[39m"

                    self.kontrolb += 1

                    self.hak -= 1

                    if self.kontrolb == 3:

                        self.text = "\033[32m"+"Tebrikler Bir - Gemi Batırdınız (Alabora) -"+"\033[39m"


                elif (self.satir == self.gemiler[3][0] and self.sutun == self.gemiler[3][1]) or (self.satir == self.gemiler[3][2] and self.sutun == self.gemiler[3][3]) or (self.satir == self.gemiler[3][4] and self.sutun == self.gemiler[3][5]) or (self.satir == self.gemiler[3][6] and self.sutun == self.gemiler[3][7]):

                    # dört birimlik gemi batırma ve vurma kontrolü

                    self.map[int(self.satir)][int(self.sutun)] = "X"

                    self.text = "\033[36m"+"Tebrikler Bir Gemi Vurdunuz"+"\033[39m"

                    self.kontrolc += 1

                    self.hak -= 1


                    if self.kontrolc == 4:

                        self.text = "\033[32m"+"Tebrikler Bir - Gemi Batırdınız (Alabora) -"+"\033[39m"


                else: # isabetsiz atış kontrolü

                    self.map[int(self.satir)][int(self.sutun)] = "*"

                    self.text = "\033[31m"+"İsabetsiz Atış"+"\033[39m"

                    self.hak -= 1


                self.toplam = self.kontrola + self.kontrolb + self.kontrolc + self.d # oyunu kazanması için toplam değişkeninin on olması gerekli



                if self.toplam == 10: # kazanırsa

                    while True:

                        os.system(clear)

                        self.haka = self.boyut*self.boyut // 3

                        print("\033[32m"+"\n\n    --- Amiral Battı --- ( Tebrikler Kazandınız Puan = {})".format(self.haka-(self.haka-self.hak)))

                        print("\033[39m""\n\n         Y) Yeni Oyun           Q) Çıkış ")

                        self.secim = input("\n\n    Secim = ")

                        if self.secim == "q" or self.secim == "Q":

                            quit() 

                        elif self.secim == "y" or self.secim == "Y":

                            self.oyun()

                if self.hak == 0: # kaybederse

                    while True:

                        os.system(clear)

                        print("\033[31m"+"\n\n    --- Amiral Battı --- ( Kaybettiniz )")

                        print("\033[39m"+"\n\n         Y) Yeni Oyun           Q) Çıkış ")

                        self.secim = input("\n\n    Secim = ")

                        if self.secim == "q" or self.secim == "Q":

                            quit() 

                        elif self.secim == "y" or self.secim == "Y":

                            self.oyun()

            else: # daha önce atış yapılan yere atış yaparsa

                self.text = "\033[31m"+"Bu Alana Daha Önceden Atış Yapıldı"+"\033[39m"


    def gemi(self): # gemi oluşturma

        while True:

            self.gemiler = []

            self.gemi1x = rn(0,self.boyut-1)

            self.gemi1y = rn(0,self.boyut-1)

            self.gemiler.append([self.gemi1x,self.gemi1y])

            if rn(0,1) == 0: # ilk geminin yatay veya dikey olması

                self.gemi2x = rn(0,self.boyut-2)

                self.gemi2y = rn(0,self.boyut-2)

                self.gemi2x2 = self.gemi2x

                self.gemi2y2 = self.gemi2y + 1

                self.gemiler.append([self.gemi2x, self.gemi2y, self.gemi2x2, self.gemi2y2])
            
            else:

                self.gemi2x = rn(0,self.boyut-2)

                self.gemi2y = rn(0,self.boyut-2)

                self.gemi2x2 = self.gemi2x + 1

                self.gemi2y2 = self.gemi2y

                self.gemiler.append([self.gemi2x, self.gemi2y, self.gemi2x2, self.gemi2y2])



            if rn(0,1) == 0: # ikinci geminin yatay veya dikey olması

                self.gemi3x = rn(0,self.boyut-3)

                self.gemi3y = rn(0,self.boyut-3)

                self.gemi3x2 = self.gemi3x

                self.gemi3y2 = self.gemi3y + 1

                self.gemi3x3 = self.gemi3x

                self.gemi3y3 = self.gemi3y2 + 1

                self.gemiler.append([self.gemi3x, self.gemi3y, self.gemi3x2, self.gemi3y2, self.gemi3x3, self.gemi3y3])

            else: 

                self.gemi3x = rn(0,self.boyut-3)

                self.gemi3y = rn(0,self.boyut-3)

                self.gemi3x2 = self.gemi3x + 1

                self.gemi3y2 = self.gemi3y

                self.gemi3x3 = self.gemi3x2 + 1

                self.gemi3y3 = self.gemi3y

                self.gemiler.append([self.gemi3x, self.gemi3y, self.gemi3x2, self.gemi3y2, self.gemi3x3, self.gemi3y3])


            if rn(0,1) == 0: # üçüncü geminin yatay veya dikey olması

                self.gemi4x = rn(0,self.boyut-4)

                self.gemi4y = rn(0,self.boyut-4)

                self.gemi4x2 = self.gemi4x

                self.gemi4y2 = self.gemi4y + 1

                self.gemi4x3 = self.gemi4x

                self.gemi4y3 = self.gemi4y2 + 1

                self.gemi4x4 = self.gemi4x

                self.gemi4y4 = self.gemi4y3 + 1

                self.gemiler.append([self.gemi4x, self.gemi4y, self.gemi4x2, self.gemi4y2, self.gemi4x3, self.gemi4y3, self.gemi4x4, self.gemi4y4])


            else:

                self.gemi4x = rn(0,self.boyut-4)

                self.gemi4y = rn(0,self.boyut-4)

                self.gemi4x2 = self.gemi4x + 1

                self.gemi4y2 = self.gemi4y

                self.gemi4x3 = self.gemi4x2 + 1

                self.gemi4y3 = self.gemi4y

                self.gemi4x4 = self.gemi4x3 + 1

                self.gemi4y4 = self.gemi4y3

                self.gemiler.append([self.gemi4x, self.gemi4y, self.gemi4x2, self.gemi4y2, self.gemi4x3, self.gemi4y3, self.gemi4x4, self.gemi4y4])


            # gemilerin birbiriyle çarpışma kontrolü

            if (self.gemiler[0][0] in self.gemiler[1]) or (self.gemiler[0][0] in self.gemiler[2]) or (self.gemiler[0][0] in self.gemiler[3]):

                continue

            elif (self.gemiler[0][1] in self.gemiler[1]) or (self.gemiler[0][1] in self.gemiler[2]) or (self.gemiler[0][1] in self.gemiler[3]):

                continue  

            elif (self.gemiler[1][0] in self.gemiler[2]) or (self.gemiler[1][0] in self.gemiler[3]) or (self.gemiler[1][1] in self.gemiler[2]) or (self.gemiler[1][1] in self.gemiler[3]):

                continue


            elif (self.gemiler[1][2] in self.gemiler[2]) or (self.gemiler[1][2] in self.gemiler[3]) or (self.gemiler[1][3] in self.gemiler[2]) or (self.gemiler[1][3] in self.gemiler[3]):

                continue


            elif (self.gemiler[2][0] in self.gemiler[3]) or (self.gemiler[2][1] in self.gemiler[3]) or (self.gemiler[2][2] in self.gemiler[3]) or (self.gemiler[2][3] in self.gemiler[3]):

                continue

            elif (self.gemiler[2][4] in self.gemiler[3]) or (self.gemiler[2][5] in self.gemiler[3]):

                continue


            break # sorun yoksa gemiler oluşur

game = Game() # oyun nesnesini tanımlama