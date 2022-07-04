from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris = load_iris()
print(iris.data)
print(iris.data)
kmeans = KMeans(n_clusters=3)
KMmodel = kmeans.fit(iris.data)
print(KMmodel.labels_)
print(KMmodel.cluster_centers_)
import pandas as pd 
pd.crosstab(iris.target,KMmodel.labels_)
