import numpy as np
import matplotlib.pyplot as plt


def veri_olustur():
    l1 = [1] * 10000
    A1 = np.random.normal(2, 0.5, 10000)
    A2 = np.random.normal(2, 0.5, 10000)
    A = np.column_stack((A1, A2))
    l0 = [0] * 10000
    B1 = np.random.normal(0, 0.5, 10000)
    B2 = np.random.normal(0, 0.5, 10000)
    B = np.column_stack((B1, B2))
    X = np.vstack((A, B))
    Y = np.vstack((l1, l0))
    return X, Y


def dusmancil_ornekler(X, Y, model, epsilon=0.00001):
    dlt = model.tahmin(X).T - Y.reshape(X.shape[0], 1)
    yon = np.sign(np.matmul(dlt, model.agirlik.T))
    return X + epsilon * yon, Y


def f_hesap(Y_hat, Y):
    Y_hat = Y_hat.flatten()
    Y = Y.flatten()
    cost1 = 0
    elp = 0.0000000000000000000000000000000000000000000001
    for i in range(len(Y)):
        cost1 -= Y[i] * np.log(Y_hat[i] + elp) + (1 - Y[i]) * np.log(1 - Y_hat[i] + elp)
    return cost1


def hata_hesap(P, Y):
    return np.mean(Y != P)


class logistic_regresyon(object):
    def fit(self, X, Y, ogrenme_orani=0.0000001, iterasyon=10000000000000000):
        X = np.array(X, dtype="float32")
        Y = np.array(Y, dtype="float32")
        #
        N, D = X.shape
        Y = Y.reshape(N, 1)
        #
        dlt = np.zeros([N, 1], dtype="float32")
        dW = np.zeros([1, D], dtype="float32")
        db = 0
        self.agirlik = np.zeros([D, 1], dtype="float32")
        self.beta = 0
        #
        c = []
        #
        for n in range(iterasyon):
            dlt = self.tahmin(X).T - Y
            dW = np.matmul(dlt.T, X).T
            db = dlt.sum() / N
            #
            self.agirlik -= ogrenme_orani * dW
            self.beta -= ogrenme_orani * db
            if n % 1000 == 0:
                c_new = f_hesap(self.tahmin(X).T, Y)
                c.append(c_new)
                err = hata_hesap(self.tahmin_sinif(X).T, Y)
                print("iterasyon:", n, "f:", c_new, "hata oranı:", err)
    #

    def tahmin(self, X):
        z = np.matmul(self.agirlik.T, X.T) + self.beta
        return 1 / (1 + np.exp(-z))
    #

    def tahmin_sinif(self, X):
        tahminsinif = self.tahmin(X)
        return (tahminsinif >= 0.5) * 1


X, Y = veri_olustur()
plt.scatter(X[:9999, 0], X[:9999, 1], color='blue', alpha=0.4, label='Orijinal Veri')
plt.scatter(X[10000:, 0], X[10000:, 1], color='red', alpha=0.4, label='Orijinal Veri')
plt.legend(loc='best')
plt.show()
model = logistic_regresyon()
model.fit(X, Y, ogrenme_orani=0.0005, iterasyon=20000)
print('Düşmancıl örnek olmadan hata oranı:', hata_hesap(model.tahmin_sinif(X).T, Y.reshape(X.shape[0], 1)))
Xadv, Y = dusmancil_ornekler(X, Y, model, epsilon=0.2)
print('Düşmancıl örneklerle hata oranı, epsilon = 0.2:', hata_hesap(model.tahmin_sinif(Xadv).T, Y.reshape(Xadv.shape[0], 1)))
Xadv2, Y = dusmancil_ornekler(X, Y, model, epsilon=0.5)
print('Düşmancıl örneklerle hata oranı, epsilon = 0.5:', hata_hesap(model.tahmin_sinif(Xadv2).T, Y.reshape(Xadv2.shape[0], 1)))


plt.scatter(X[:9999, 0], X[:9999, 1], color='blue', alpha=0.4, label='Orijinal Veri')
plt.scatter(Xadv[:9999, 0], Xadv[:9999, 1], color='green', alpha=0.4, label='Düşmancıl Örnekler, Epsilon = 0.2')
plt.scatter(Xadv2[:9999, 0], Xadv2[:9999, 1], color='purple', alpha=0.4, label='Düşmancıl Örnekler, Epsilon = 0.5')
plt.scatter(X[10000:, 0], X[10000:, 1], color='red', alpha=0.4, label='Orijinal Veri')
plt.scatter(Xadv[10000:, 0], Xadv[10000:, 1], color='orange', alpha=0.4, label='Düşmancıl Örnekler, Epsilon = 0.2')
plt.scatter(Xadv2[10000:, 0], Xadv2[10000:, 1], color='yellow', alpha=0.4, label='Düşmancıl Örnekler, Epsilon = 0.5')
plt.legend(loc='best')
plt.show()