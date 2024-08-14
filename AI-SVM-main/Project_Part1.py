import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs


x, y = make_blobs(n_samples=800, centers=2, random_state=17)

my_svm = svm.SVC(kernel='linear', C=1000)
my_svm.fit(x, y)
plt.scatter(x[:, 0], x[:, 1], c=y, s=30, cmap=plt.cm.Paired)

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = my_svm.decision_function(xy).reshape(XX.shape)

ax.contour(XX, YY, Z, colors='k', levels = [-1,0,1], alpha=0.5
           , linestyles=['--', '-', '--'])

ax.scatter(my_svm.support_vectors_[:, 0], my_svm.support_vectors_[:, 1],
            s = 100, linewidth=1, facecolors='none')
plt.show()
