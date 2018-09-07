from PIL import Image 
import numpy as np 
from pybooru import Danbooru
from pathlib import Path 
import urllib.request 
import os 

from sklearn.externals import joblib 
from sklearn.decomposition import IncrementalPCA

classfier = joblib.load("model.pkl")
ipca = IncrementalPCA(n_components=20)

hoge = [0.5] *200
hoge = np.array(hoge) 
#hoge.reshape(1,-1)
#print(hoge.shape)
data = []
data.append(hoge)
data = np.array(data)
print(data.shape)
data = ipca.fit_transform(data)
print(data.shape)
pr_label = classfier.predict(data)
print(pr_label)