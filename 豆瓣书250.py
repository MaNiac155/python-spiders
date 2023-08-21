# # 导入 requests 库
# import requests

# from bs4 import BeautifulSoup
# # 向 https://book.douban.com/top250/ 发送请求
# # 并将响应结果储存到 res 变量中

# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }
# res=requests.get("https://book.douban.com/top250/",headers=headers)

# soup=BeautifulSoup(res.text,'html.parser')

# book_name_tags=soup.select('div.pl2>a')

# #print(book_name_tags)
# book=book_name_tags[0]
# # print(type(book))
# # print(book.text)
# # print(book['href'])
# # print(book['title'])

# book_info_tags=soup.select('p.pl')
# for info_tag in book_info_tags:
#     info=info_tag.text
#     info_list=info.split(' / ')
#     author=info_list[0]
#     #print(info_list)
#     publisher=info_list[-3]
#     print(author,publisher)


import datetime
# 导入 requests 库
import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup

# 定制消息头
headers={
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
# 向 https://book.douban.com/top250/ 发送带消息头的请求
# 并将响应结果储存到 res 变量中
res=requests.get('https://book.douban.com/top250/',headers=headers)

# 将响应结果的文本内容解析为 BeautifulSoup 对象
# 并保存到变量 soup 中
soup=BeautifulSoup(res.text,'html.parser')
# 所有书名所在元素
book_name_tags=soup.select('div.pl2>a')

# 所有书籍信息所在元素
book_info_tags=soup.select('p.pl')
print(book_info_tags)
# 遍历每本图书
for i in range(len(book_name_tags)):
  # 通过元素 title 属性提取书名
    book_name=book_name_tags[i]['title']
  # 获取书籍信息
    book_info=book_info_tags[i]
  # 按“ / ”分割字符串
    book_info_list=book_info.text.split(' / ')
  # 结果列表中第一项为作者信息
    author=book_info_list[0]
  # 倒数第三项为出版社信息
    publisher=book_info_list[-3]
  # 打印书名、作者、出版社信息
    print(book_name,author,publisher)