import numpy as np # to handle numeric data
import matplotlib.pyplot as plt # for visualization
import pandas as pd
data = pd.read_csv('pharama data.csv')
print(data)
datasubset = data.loc[:, ["orders","payment"]]
plt.figure(figsize=(5, 7))
plt.scatter(datasubset['orders'], datasubset['payment'], s=45,c='green')
plt.show()

import scipy.cluster.hierarchy as sch
plt.figure(figsize=(5, 7))
dendrogram = sch.dendrogram(sch.linkage(datasubset, method = 'ward'))
plt.title('Dendrogram') # title of the dendrogram

plt.xlabel('Pharma-Data') # label of the x-axis
plt.ylabel('Euclidean distances') # label of the y-axis
plt.show()
from sklearn.cluster import AgglomerativeClustering
cluster= AgglomerativeClustering(n_clusters = 2, affinity = 'euclidean', linkage = 'ward')
cluster. fit_predict(datasubset)