# kütüphaneler
from mpl_toolkits.mplot3d import Axes3D #3d
import matplotlib.pyplot as plt # görselleştirme için gerekli kütüphane


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') # figürü seçtik. bundan sonraki işlemlerimizi ax üzerinden gerçekleştireceğiz.

m = ["*","<","o"] # grafikte çıkacak şekillerimiz

xs = [0,10,8,5,2,3,6,98,52,20] # x düzlemindeki değerler.
ys = [0,1,-5,9,5,6,10,12,20,3] # y düzlemindeki değerler
zs = [0,20,30,15,20,60,20,10,10,20] # z düzlemindeki değerler.
ax.scatter(xs, ys, zs, marker=m[0]) 
# x, y ve z düzlemindeki verileri veriyoruz. birde verileri görselleştirmek için maker parametresine şekil veriyoruz.
xs = [0,30,40,20,50,23,61,98,52,20]
ys = [10,10,-50,93,52,61,10,12,20,32]
zs = [12,29,33,25,30,40,29,20,15,40]
ax.scatter(xs, ys, zs, marker=m[1])

xs = [5,39,42,21,58,33,41,90,12,50]
ys = [19,18,-20,83,12,71,20,42,30,42]
zs = [19,19,36,15,39,45,39,28,19,49]
ax.scatter(xs, ys, zs, marker=m[2])

ax.set_xlabel('X Düzlemi') # düzlemlerin etiketleri
ax.set_ylabel('Y Düzlemi')
ax.set_zlabel('Z Düzlemi')

plt.title("3d Veri Görselleştirme") # başlık

plt.show() # grafiği ekrana yansıttık.