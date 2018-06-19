from PIL import Image 
import numpy as np 
import os 
import pandas as pd 
from sklearn.externals import joblib 
from sklearn.svm import LinearSVC 
from sklearn.decomposition import IncrementalPCA

STANDARD_SIZE = (300, 300)

def img_to_matrix(filename):
  img = Image.open(filename)
  img = img.resize(STANDARD_SIZE)
  imgArray = np.asarray(img)
  return imgArray 

def flatten_image(img):
  s = img.shape[0] * img.shape[1] * img.shape[2] 
  img_width = img.reshape(1, s) 
  return img_width[0] 

def main(): 
  img_dislike_dir = 'images/dislike300/'
  dislike_images = [img_dislike_dir + f for f in os.listdir(img_dislike_dir) ]

  dislike_data = []
  for image in dislike_images:
    img = img_to_matrix(image)
    if not len(img.shape) < 3:
      img = flatten_image(img)
      dislike_data.append(img)

  dislike_labels = [0] * len(dislike_data)
  
  img_like_dir = 'images/like300/'
  like_images = [img_like_dir + f for f in os.listdir(img_like_dir) ]

  like_data = []
  for image in like_images:
    img = img_to_matrix(image)
    if not len(img.shape) < 3:
      img = flatten_image(img)
      like_data.append(img)

  like_labels = [1] * len(like_data)

  data = dislike_data + like_data 
  labels = dislike_labels + like_labels

  data = np.array(data)
  labels = np.array(labels)
  print(data.shape)

  is_train = np.random.uniform(0, 1, len(data)) <= 0.7 

  train_x, train_y = data[is_train], labels[is_train]
  print("Training data is created.")

  n = train_x.shape[0]
  ipca = IncrementalPCA(n_components=20)
  train_x = ipca.fit_transform(train_x)
  print("PCA is done.")

  svm = LinearSVC(C=1.0)
  svm.fit(train_x, train_y)
  joblib.dump(svm, 'model.pkl')

  test_x, test_y = data[is_train==False], labels[is_train==False]
  test_x = ipca.fit_transform(test_x)
  print(pd.crosstab(test_y, svm.predict(test_x),rownames=['Actual'], colnames=['Predicated']))

if __name__ == '__main__':
  main()