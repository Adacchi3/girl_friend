#参考
#https://qiita.com/bakira/items/00743d10ec42993f85eb#%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB

import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
ATK = config.ACCESS_TOKEN_KEY
ATS = config.ACCESS_TOKEN_SECRET
SCREEN_NAME = config.SCREEN_NAME

twitter = OAuth1Session(CK, CS, ATK, ATS)

url = "https://api.twitter.com/1.1/users/show.json"
params = {'screen_name': SCREEN_NAME}
res = twitter.get(url, params=params)

if res.status_code == 200:
  user_info = json.loads(res.text)
  favourites_count = user_info['favourites_count']
  crawl_favs_count = 0
  max_id = -1
  print("[GET] favourites_count: %i" % favourites_count)
  while crawl_favs_count < favourites_count:
    url = "https://api.twitter.com/1.1/favorites/list.json"
    if max_id != -1:
      params = {'count': 200, 'max_id': max_id}
    else:
      params = {'count': 200}
    res = twitter.get(url, params=params)
    if res.status_code == 200:
      list = json.loads(res.text)
      max_id = list[-1]['id']
      FILE = './favs/favlist'+str(crawl_favs_count)+'.json'
      with open(FILE,'w') as file:
        file.write(json.dumps(list,indent=2))
        file.close()
      crawl_favs_count = crawl_favs_count + 200
      print("%i --> %i"% (crawl_favs_count-200, crawl_favs_count))
    else: 
      print("Failed: %d" % res.status_code) 
      break
else: 
  print("Failed: %d" % res.status_code)