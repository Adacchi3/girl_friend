from pybooru import Danbooru
from pathlib import Path 
import urllib.request 
import os 

client = Danbooru('danbooru')

min_pages = 0
max_pages = min_pages + 2 
count = 0

for page in range(min_pages, max_pages):
  posts = client.post_list(limit=100, page=page, random=False, raw=False)
  for post in posts:
    if 'file_url' in post:
      image_url = post['file_url']
      FILE = image_url.split("/")[-1]
      if not os.path.exists("images"):
        os.makedirs("images")
      imagepath = Path("./images")
      if not imagepath.joinpath(FILE).exists():
        try:
          urllib.request.urlretrieve(image_url, "./images/%s" % FILE)
          count = count + 1
          print("*%i: %s"%(count,FILE))
        except:
          print("%s cannot be retrieved from %s ."%(FILE, image_url))
      else:
        count = count + 1
        print("%i: %s"%(count,image_url))