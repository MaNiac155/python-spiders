from selenium import webdriver
import time
from openpyxl import Workbook
import yagmail
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser=webdriver.Chrome()
browser.get('https://xueqiu.com/S/SH000001')
time.sleep(2)
login_in=browser.find_element('link text','账号密码登录')
login_in.click()
time.sleep(2)
user_id=browser.find_element('name','username')
user_id.send_keys('19883127849')
user_passcode=browser.find_element('name','password')
user_passcode.send_keys('LiYidong123')

login_button=browser.find_element(By.CSS_SELECTOR,'#app > div.modals.dimmer.js-shown > div:nth-child(1) > div.modal.modal__login > div.modal__login__main > div.modal__login__mod > div:nth-child(3) > div.modal__login__btn.btn-active')
login_button.click()
time.sleep(10)
# WebDriverWait(browser,30).until(EC.url_contains('xueqiu'))
# close_button=browser.find_element(By.XPATH,'//*[@id="app"]/div[3]/div[1]/div[3]/a')
#close_button=browser.find_element(By.CSS_SELECTOR,'body > div:nth-child(11) > div.index_dialog_PKc > div > div > div > a > i')
# close_button.click()