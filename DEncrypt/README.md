# DEncrypt

* Görsel verilerinizi üçüncü kişilerin görmemesi için şifrelemek amaçlı yazılmış uygulama.
* Whatsapp ve Instagram gibi sosyal medya platformlarında, yakın çevrenize resim atarken kalitesinin düşmesini engeller.


# Ana Menü

![Screenshot_2020-08-04_17-52-44](https://user-images.githubusercontent.com/54184905/89309016-9659a400-d67b-11ea-986c-359554546aab.png)

* Sol tarftaki kilit butonuna basarak resimlerinizi şifreleyebilirsiniz.
* Sağ taraftaki anahtar butonuna basarak resimlerinizi çözebilirsiniz.


# Encryption

![Screenshot_2020-08-04_17-53-20](https://user-images.githubusercontent.com/54184905/89309018-978ad100-d67b-11ea-8dbd-51f15dc6bb97.png)

* Şifrelenecek resminizi seçip ardından şifrenizi belirledikten sonra ise Şifrele butonuna tıklayınız.
* Şifrelenmiş .demir adlı dosya "Sifreli" adlı klasöre oluşturulur.


# Decryption

![Screenshot_2020-08-04_17-53-56](https://user-images.githubusercontent.com/54184905/89309023-978ad100-d67b-11ea-80d8-894d20d496b9.png)

* Çözmek istediğiniz .demir uzantılı dosyayı seçip ardından şifrelerken kullandığınız şifreyi giriniz sonra ise çöz butonuna tıklayınız.
* Resim tekrar eski haline getirilir(Çözülür) ve ekrana yansıtılır.


# Şifrelerken Ne Yaptık ?

![channelsrgb](https://user-images.githubusercontent.com/54184905/89309831-99a15f80-d67c-11ea-926f-fd3d5bed69a9.gif)

* Resimler içersinde 3 adet eleman bulunan bir liste vardır, R G B şeklinde yani [kırmızı, yeşil, mavi] değer aralığını tutar.
* Beyaz renk = [255,255,255] , Siyah = [0,0,0] , Pembe nin x. tonu = [191,0,95] gibi.
* Resimlerin yükseklik ve genişlik değerleride vardır yani bir resim 500X600 olabilir.
* Resim üzerinde oynamak için resmi bir diziye aktarmamız gerek, bu dizi üç bouyutlu bir dizidir. Resim[yükseklik][genişlik][RGB_değerler] şeklinde.
* Sonra bu RGB değerlere erişip her sayı bir harf olacak şeklinde dönüştürme yaptım. Yani;

![Screenshot_2020-08-04_18-10-27](https://user-images.githubusercontent.com/54184905/89310864-f2252c80-d67d-11ea-93a9-63a370e59985.png) şeklinde.

örneğin [230, 65, 255] olan bir listeyi ["ZBK", "DC", "ZCC"] şekline getirdim.

* Daha sonra bu yeni listeyi bir dosyaya aktardım, dosyanın sonununa ise resmin yüksekliği, genişligi ve renk kanallarının sayısını verdim, en sonuna ise kullanıcının girdiği şifrenin SHA-256 ile hash lenmiş halini yazıp dosyayı kaydettim.



# Çözerken Ne Yaptık ?

* Öncelikle dosyayı açıp split ile "-" şeklinde ayırma işlemi yaptık. Geriye dönen listenin ilk elemanı, resim verimizin harflerle değiştirdiğimiz değerleridir. Listenin ikinci elemanı ise şifrelenen resmimizin yükseklik, genişlik ve renk kanal sayısını tutmaktadır. son elemanı ise kullanıcının girdiği hash lenmiş şifredir.

* Uygulama kullanıcıdan şifre sorar, şifre doğru ise resim verimizin harflerle değiştirdiğimiz değerleri eski haline getiririz. Yani; 


![Screenshot_2020-08-04_18-21-46](https://user-images.githubusercontent.com/54184905/89312046-71ffc680-d67f-11ea-9527-54e9e7da9536.png) şeklinde.


örneğin ["ZBK", "DC", "ZCC"] olan bir listeyi [230, 65 ,255]

* Ve resim çözülür kullanıcıya sunulur.


# Örenk Şifrelenmiş Resim

![Screenshot_2020-08-04_18-27-36](https://user-images.githubusercontent.com/54184905/89312853-6fea3780-d680-11ea-91a3-0d94d978aeb9.png)

![Screenshot_2020-08-04_18-27-42](https://user-images.githubusercontent.com/54184905/89312856-7082ce00-d680-11ea-93a9-24c1906ce5d4.png)


# Örenk Çözülmüş Resim

![Screenshot_2020-08-04_18-28-56](https://user-images.githubusercontent.com/54184905/89312858-7082ce00-d680-11ea-8fda-9c8fce258da9.png)
