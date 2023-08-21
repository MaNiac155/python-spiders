# import os
# import urllib.request
# import win32com.client as win32
# url_list = "https://www.huzhidao.com/down/118/17611.html?title=%E8%8B%B1%E8%AF%AD%E5%8F%A5%E5%AD%90%E7%BB%93%E6%9E%84%E3%80%90%E7%B2%BE%E5%BD%A99%E7%AF%87%E3%80%91&classid=118&newsid=17611" # 假设我们需要下载的文件存储在网盘中
# # 循环遍历链接列表，逐一下载
# #for url in url_list:
# res = urllib.request.urlopen(url_list)
# html = res.read().decode("utf-8")
# #start = html.find("initPrefetchTable") # 下载链接在此处存放，可以通过检查百度网盘选项卡中的文件信息得到
# #end = html.find("file":{
# #"fs_id")
# # 从HTML中获取下载链接并下载
# #down_url = html[start:end]
# #down_url = down_url[down_url.find("http"):down_url.find("}")-1]
# down_name = "download.docx" # 定义下载的文件名，如果不需要修改，此处可以直接使用down_url.split("/")[-1]
# # 下载
# #urllib.request.urlretrieve(down_url, down_name)
# # 获取文件类型信息
# word = win32.gencache.EnsureDispatch('Word.Application')
# #doc = word.Documents.Open(os.path.dirname(os.path.abspath(__file__)) + '\\' + down_name)
# new_doc = word.Documents.Add()
# doc_type = new_doc.Application.Name
# # 将扩展名修改为正确的格式
# if doc_type == 'Microsoft Word': # Word 2003文档，使用.doc格式
#     os.rename(down_name, down_name[:-5] + '.doc')
# elif doc_type == 'Microsoft Word 阅读器': # Word 2007及以上文档，使用.docx格式
#     os.rename(down_name, down_name[:-5] + '.docx')
# new_doc.Close()
# word.Quit()



import os
import urllib.request
import win32com.client as win32

# 想要下载的url
doc_url="http://www.cse.zju.edu.cn/_upload/article/files/04/8a/aee3993c40309c8560110979016c/c5e4d4db-b516-4d2e-87eb-998cd5a2553b.doc"

# 找到url的后缀，即.doc还是.docx
index_of_last_dot = doc_url.rfind(".")  # 找到最后一个点的索引
if index_of_last_dot != -1:  # 确保找到了点
    suffix = doc_url[index_of_last_dot:]  # 提取点后面的字符
else:
    suffix=""
    print("String doesn't contain a dot.")

# 把后缀加给document
local_path="D:\LIB\Desktop\pypc\document"+suffix
# 本地文件路径，用来存储下载的文件
#local_path = "D:\LIB\Desktop\pypc\document.doc"
print(local_path)

#使用 urllib.request 下载文件
urllib.request.urlretrieve(doc_url, local_path)

# 使用 win32com 打开word应用
word_app = win32.gencache.EnsureDispatch("Word.Application")

# 打开下载的文件
doc = word_app.Documents.Open(local_path)

# 如果需要进行文字编写的话，在这里进行

# 关闭文件
doc.Close()

# 关闭word应用
word_app.Quit()