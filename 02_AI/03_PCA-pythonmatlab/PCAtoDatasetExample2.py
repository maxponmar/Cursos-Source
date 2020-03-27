import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA

digits = datasets.load_digits()
digits.data.shape
digits.images.shape

plt.imshow(digits.images[2], cmap='gray')

pca = PCA(n_components=2)
pca.fit(digits.data)

Z = pca.transform(digits.data)

plt.scatter(Z[:,0],Z[:,1], c=digits.target, cmap='tab10',alpha=0.7)
plt.colorbar()
plt.grid('on')
