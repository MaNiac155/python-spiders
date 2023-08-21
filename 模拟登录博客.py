from selenium import webdriver
import time

browser = webdriver.Chrome()
# 打开博客
browser.get('https://wpblog.x0y1.com/')
# 找到登录按钮
login_btn = browser.find_element('link text', '登录')
# 点击登录按钮
login_btn.click()
time.sleep(2)
# 找到用户名输入框
user_name = browser.find_element('id', 'user_login')
# 输入用户名
user_name.send_keys('codetime')
# 找到密码按钮
password = browser.find_element('id', 'user_pass')
# 输入密码
password.send_keys('shanbay520')
# 找到登录按钮
submit = browser.find_element('id', 'wp-submit')
# 点击登录
submit.click()
# 找到python分类目录
python_directory = browser.find_element('css selector',
                                        'section#categories-2 ul li a')
# 点击该分类
python_directory.click()
# 找到python下所有文章标题元素

titles = browser.find_elements('css selector', 'h2.entry-title a')
links = [title.get_attribute('href') for title in titles]

# 依次打开链接中的文章
for link in links:
    browser.get(link)
    # 获取文章中的内容
    content = browser.find_element('class name', 'entry-content')
    print(content.text)
browser.quit()