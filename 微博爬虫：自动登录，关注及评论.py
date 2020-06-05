#!/usr/bin/env python
# coding: utf-8



import selenium
import time
from selenium import webdriver
driver = webdriver.Chrome('/Users/youxie/Desktop/chromedriver/chromedriver')
driver.get('http://weibo.com/')
#自动登录微博
def login(loginname,password):
    input_account=driver.find_element_by_id('loginname')
    input_psw=driver.find_element_by_name('password')
    input_account.send_keys(loginname)
    input_psw.send_keys(password)
    bt_login=driver.find_element_by_class_name('login_btn')
    bt_login.click()



#判断是否有验证码
def isVerifyCodeExist():
    try:
        driver.find_element_by_name('verifycode')
        return True
    except:
        return False
#输入验证码
def inputVerifyCode():
    input_verifycode=driver.find_element_by_name('verifycode')
    bt_login=driver.find_element_by_class_name('login_btn')
    time.sleep(1)
    while isVerifyCodeExist():
        print("请输入验证码:")
        verifycode=input("验证码:")
        input_verifycode.send_keys(verifycode)
        bt_login.click()
        time.sleep(1)
        if driver.current_url.split('/')[-1].split('?')[0]=='home':
            print("登陆成功")
            break
        else:
            print("输入的验证码不正确")




#自动发微博（文字）
def upload_txt(text):
    input_w=driver.find_element_by_xpath('//div[@node-type="textElDiv"]/textarea[@class="W_input"]')
    input_w.send_keys(text)
    
def send():
    driver.find_element_by_class_name('W_btn_a').click()




#自动加关注
def follow(uid):
    driver.get('http://weibo.com/u/'+uid)
    try:
        focuslink=driver.find_element_by_xpath('//*[@id="Pl_Official_Headerv6__1"]/div[1]/div/div[2]/div[4]/div/div[1]/a[1]')
        focuslink.click()
    except:
        print('关注失败')
            



#微博自动评论
def comment(uid,text):
    #首先进入对方主页
    driver.get('http://weibo.com/u/'+uid)
    time.sleep(1)
    #先找到微博评论按钮并点击按钮
    button_c=driver.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__21"]/div/div[2]/div[2]/div/ul/li[3]/a/span/span')
    button_c.click()
    time.sleep(1)
    #出现评论框后输入文字
    input_c=driver.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__21"]/div/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/textarea')
    input_c.send_keys(text)
    time.sleep(1)
def send_c():
    bottom_s=driver.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__21"]/div/div[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/a')
    driver.execute_script("arguments[0].click();", bottom_s)



#主函数调用
def main():
    login(loginname,password)    
    isVerifyCodeExist()
    inputVerifyCode()
    upload_txt('爬虫测试')
    send()
    follow(uid)
    comment(uid,'爬虫测试')
    send_c()
main()

