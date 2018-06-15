from pathlib import Path 
import os.path 
import cv2

path = Path("./faces")
files = list(path.glob("*"))

count = 0
output_dir = 'faces96'

for file in files:
  file = str(file)
  image = cv2.imread(file, cv2.IMREAD_COLOR)
  image = cv2.resize(image,(96,96))
  FILE = file.split("/")[-1]
  output_path = os.path.join(output_dir,FILE)
  cv2.imwrite(output_path, image)
  count = count + 1
  print("%i %s" % (count, FILE))