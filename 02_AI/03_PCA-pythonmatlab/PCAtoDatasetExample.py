import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_digits()

X = iris.data
y = iris.target

pca = PCA(n_components=2)
pca.fit(X)

Z = pca.transform(X)

plt.scatter(Z[:,0],Z[:,1], c=y)
