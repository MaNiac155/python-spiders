# 导入 requests 库
import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup

# 定制消息头
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 向 https://movie.douban.com/top250/ 发送带消息头的请求
# 并将响应结果储存到 res 变量中
res=requests.get('https://movie.douban.com/top250',headers=headers)

# 将响应结果的文本内容解析为 BeautifulSoup 对象
# 并保存到变量 soup 中
soup=BeautifulSoup(res.text,'html.parser')
# 所有书名所在元素
movie_name_tags=soup.select('div.hd>a')

# 所有书籍信息所在元素
#movie_info_tags=soup.select('div.bd>p')
# print(movie_info_tags)
# 遍历每本图书
for i in range(len(movie_name_tags)):
  # 通过元素 title 属性提取书名
    movie_name=movie_name_tags[i].select('span.title')[0]
    link=movie_name_tags[i]['href']

    print(movie_name.text,link)

  # # 获取书籍信息
  #   movie_info=movie_info_tags[i]
  # # 按“ / ”分割字符串
  #   movie_info_list=movie_info.text.split(' / ')
  # # 结果列表中第一项为作者信息
  #   author=movie_info_list[0]
  # # 倒数第三项为出版社信息
  #   publisher=movie_info_list[-3]
  # # 打印书名、作者、出版社信息
  #   print(movie_name,author,publisher)