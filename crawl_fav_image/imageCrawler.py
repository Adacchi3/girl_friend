from pathlib import Path 
import json, urllib.request

path = Path("../crawl_fav_list/favs")
files = list(path.glob("*"))

imagepath = Path("./images")

count = 0
for file in files:
  with open(file, 'r') as f:
    favs = json.load(f)
    for fav in favs:
      if 'extended_entities' in fav:
        images = fav['extended_entities']['media']
        for image in images:
          image_url = image['media_url']
          FILE = image_url.split("/")[-1]
          if not imagepath.joinpath(FILE).exists(): 
            try:
              urllib.request.urlretrieve(image_url,"./images/%s"%FILE)
              count = count + 1
              print("*%i: %s"%(count, FILE))
            except:
              print("%s cannot be retrieved from %s."%(FILE, image_url))
          else:
            count = count + 1
            print("%i: %s"%(count, FILE))