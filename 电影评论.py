import requests
from bs4 import BeautifulSoup
import time

headers = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
  'referer': 'http://movie.mtime.com/'
}

for index in range(1,11):
  params = {
    "tt": "{}".format(int(time.time() * 1000)),
    "movieId": "209164",
    "pageIndex": index,
    "pageSize": "20",
    "orderType": "1"
  }

  res = requests.get('http://front-gateway.mtime.com/library/movie/comment.api', params=params, headers=headers)
  result = res.json()
  li = result['data']['list']
  for i in range(len(li)):
    print(index*20+i)
    print('user: ', li[i]['nickname'])
    print('comment: ', li[i]['content'])
  time.sleep(1)
