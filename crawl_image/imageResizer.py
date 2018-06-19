from pathlib import Path 
import os.path 
import cv2

path = Path("./images/like")
files = list(path.glob("*"))

count = 0
if not os.path.exists("images/like300"):
  os.makedirs("images/like300")
output_dir = './images/like300'

for file in files:
  file = str(file)
  image = cv2.imread(file, cv2.IMREAD_COLOR)
  image = cv2.resize(image,(300,300))
  FILE = file.split("/")[-1]
  output_path = os.path.join(output_dir,FILE)
  if not os.path.exists(output_path):
    cv2.imwrite(output_path, image)
    count = count + 1
    print("*%i %s" % (count, FILE))
  else: 
    count = count + 1
    print("%i %s" % (count, FILE))