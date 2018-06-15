import cv2
from pathlib import Path 
import os.path 

count = 0


def detect(filename, cascade_file = "lbpcascade_animeface.xml"):
    global count
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    output_dir = 'faces'
    for i, (x, y, w, h) in enumerate(faces):
      face_image = image[y:y+h, x:x+w]
      face_image = cv2.resize(face_image,(96,96))
      FILE = filename.split(".")
      FILE = FILE[-2].split("/")[-1]
      output_path = os.path.join(output_dir,'%s-%i.jpg'%(FILE,i))
      cv2.imwrite(output_path,face_image)
      count = count + 1
      print("%i %s" % (count, FILE+"-"+str(i)+".jpg"))
      #この下の処理は赤枠をつけてくれるヤツ。
      #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    #cv2.imshow("AnimeFaceDetect", image)
    cv2.waitKey(0)

path = Path("../crawl_fav_image/images")
files = list(path.glob("*"))

for file in files:
  detect(str(file))