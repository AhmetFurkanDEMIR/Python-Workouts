# kütüphaneler
from mpl_toolkits.mplot3d import Axes3D #3d
import matplotlib.pyplot as plt #görselleştirme için gerekli kütüphane
from matplotlib import cm #görselleştirme için gerekli kütüphane
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np # matris işlemleri


fig = plt.figure()
ax = fig.gca(projection='3d') # figürü seçtik. bundan sonraki işlemlerimizi ax üzerinden gerçekleştireceğiz. 

# data, veri
X = np.arange(-5, 5, 0.25) #matrisler.
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y) # Koordinat vektörlerinden koordinat matrislerini döndürür.
R = np.sqrt(X**2 + Y**2) # karekök alma.
Z = np.sin(R) #sinüs.

# yüzeyi çizim işlevi
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# z ekseni
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# renk çubuğu
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.title("3d Veri Görselleştirme") # başlık

plt.show() # grafiği ekrana yansıttık.
