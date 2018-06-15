#顔画像のクラスタを行う（学習データの洗練）
#https://avinton.com/academy/image-classification/

import os 
from pathlib import Path 
import numpy as np 
from PIL import Image 

from sklearn.decomposition import IncrementalPCA
#from sklearn.cluster import DBSCAN 
from sklearn.cluster import KMeans

path = Path("../detect_animeface/faces96/")
files = list(path.glob("*"))

dataset = []
for file in files:
  image = Image.open(str(file))
  image = np.asarray(image)
  s = image.shape[0]*image.shape[1]*image.shape[2]
  img = image.reshape(1,s)
  dataset.append(img[0])
dataset = np.array(dataset)
print(dataset.shape)
print("Making dataset is done.\n")

n = dataset.shape[0]
batch_size = 180
ipca = IncrementalPCA(n_components=100)
 
for i in range(n//batch_size):
    r_dataset = ipca.partial_fit(dataset[i*batch_size:(i+1)*batch_size])
 
r_dataset = ipca.transform(dataset)
print(r_dataset.shape)
print("PCA is done.\n")

"""
###
# DBSCANっていうクラスタリング手法を使ってみたけど、
# 次元数を減らしたせいか、クラスタすることができなかった
###
for eps in [1, 3, 5, 7, 9, 11, 13, 15, 17]:
    print("eps:{}".format(eps))
    dbscan = DBSCAN(eps=eps, min_samples=3)
    labels = dbscan.fit_predict(r_dataset)
    print("Clusters present:{}".format(np.unique(labels)))
    print("Clusters size:{}".format(np.bincount(labels + 1)))
    print()
"""

#for i in range(2, 15):
n_clusters = 6 
kmeans = KMeans(n_clusters=n_clusters, random_state=5).fit(r_dataset)
labels = kmeans.labels_
print("K-means clustering is done.")
print("Cluster size %i-means: " % n_clusters)
print(np.bincount(labels))
print()


if not os.path.exists("cluster"+str(n_clusters)):
  os.makedirs("cluster"+str(n_clusters))


for i in range(n_clusters):
  label = np.where(labels==i)[0]
  count = 0

  if not os.path.exists("cluster"+str(n_clusters)+"/label"+str(i)):
    os.makedirs("cluster"+str(n_clusters)+"/label"+str(i))

  for j in label:
    img = Image.open(str(files[j]))
    FILE = str(files[j]).split("/")[-1]
    img.save("cluster"+str(n_clusters)+"/label"+str(i)+"/"+FILE)
    count = count + 1
  print("label%i: %i" % (i, count))
