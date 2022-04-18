from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys as keys
import chromedriver_binary
import time
import os
from selenium.webdriver.chrome.options import Options
import twi
num = 0
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
tw_url = "https://www.mirrativ.com/broadcast/history"
url=(twi.url)
driver.get(tw_url)
time.sleep(3)
tw_login = driver.find_element_by_xpath('//*[@id="username_or_email"]').send_keys(twi.un)
tw_login2 = driver.find_element_by_xpath('//*[@id="password"]').send_keys(twi.pw)
tw_login3 = driver.find_element_by_xpath('//*[@id="allow"]').click()
time.sleep(5)
driver.get(url)
def aisatu_comnt():
    time.sleep(2)
    cmt_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').click()
    cmt_btn2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys("こんにｔは！ゆっくりしていってね！このコメントはbotによって自動で実行されているため主は気づいてないかもしれません。配信のルールはメモに書いています。")
    cmt_btn3 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys(keys.ENTER)
def aisatu2_comnt():
    time.sleep(2)
    cmt_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').click()
    cmt_btn2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys("")
    cmt_btn3 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys(keys.ENTER)
def nyusitu():
    cmt_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').click()
    cmt_btn2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys(usr_name + "さん、参加方法はディスコードに入ると参加できます!   https://discord.gg/hphSwJ6X2y")
    cmt_btn3 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys(keys.ENTER)
def nyusitu2():
    cmt_btn = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').click()
    cmt_btn2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys(usr_name + "さんいらっしゃい!mirrativへようこそ！ゆっくりしていってね！もしよければふぉろーしてね")
    cmt_btn3 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/input').send_keys(keys.ENTER)
for i in range(99999):
    time.sleep(1)
    u_name = driver.find_elements_by_class_name('_3XmCC1rS9BcAN8CQPCPBqG')
    cmt = driver.find_elements_by_class_name("_3EiRSh7-t9tRPcPgOmaKdu")
    cmt2 = cmt[0].text
    usr_name = u_name[0].text
    usr2_name = u_name[1].text
    kensaku_word = cmt[2].text 
    time.sleep(2)
    if "こんにちは" in cmt2 and cmt2 != cmt[1].text:
        aisatu_comnt()
    elif "こんばんは" in cmt2 and cmt2 != cmt[1].text:
        aisatu2_comnt()
    elif "!参加" in cmt2:
        nyusitu()
    elif "が入室しました" in cmt2:
        nyusitu2()
