from PIL import Image 
import numpy as np 
from pybooru import Danbooru
from pathlib import Path 
import urllib.request 
import os, sys 
from pathlib import Path 
import cv2 
from sklearn.externals import joblib 
from sklearn.decomposition import IncrementalPCA

def img_to_matrix(filename):
  img = cv2.imread(filename, cv2.IMREAD_COLOR)
  img = cv2.resize(img,(300,300))
  imgArray = np.asarray(img)
  return imgArray 

def flatten_image(img):
  s = img.shape[0] * img.shape[1] * img.shape[2] 
  img_width = img.reshape(1, s) 
  return img_width[0] 

path = Path("./images/")
files = list(path.glob("*.*"))

images = []
for file in files:
  if not file == ".DS_Store"
    images.append(str(file))

data = []
for image in images:
  img = img_to_matrix(image)
  if not len(img.shape) < 3:
    img = flatten_image(img)
    data.append(img)
  else:
    os.remove(image)

path = Path("./images/")
files = list(path.glob("*.*"))
images = []
for file in files:
  if not file == ".DS_Store"
    images.append(str(file))

data = np.array(data)
images = np.array(images)

ipca = IncrementalPCA(n_components=20)
data = ipca.fit_transform(data)

classifier = joblib.load("model.pkl")
pr_labels = classifier.predict(data)
print(pr_labels)
for label, image in zip(pr_labels, images):
  if not label == 1:
    os.remove(image)
print(np.sum(pr_labels==1))