# 导入 requests 库
import time

import requests
# 从 bs4 库导入 BeautifulSoup
from bs4 import BeautifulSoup

base_url='https://music.douban.com/top250/'
# 定制消息头
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}

for index in range(0,250,25):
    params={
        'start':index
    }
    # 向 https://book.douban.com/top250/ 发送带消息头的请求
    # 并将响应结果储存到 res 变量中
    res=requests.get(base_url,headers=headers,params=params)

    # 将响应结果的文本内容解析为 BeautifulSoup 对象
    # 并保存到变量 soup 中
    soup=BeautifulSoup(res.text,'html.parser')
    # 所有书名所在元素
    book_name_tags=soup.select('div.pl2>a')

    # 所有书籍信息所在元素
    book_info_tags=soup.select('p.pl')
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
    time.sleep(1)