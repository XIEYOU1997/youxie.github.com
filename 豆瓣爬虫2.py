#!/usr/bin/env python
# coding: utf-8

# In[15]:


#主要思路来源：https://lbjheiheihei.xyz/2019/02/14/Use-Python-Scrapy-Douban-Movie-Poster.html
#python中entree的简单应用：https://blog.csdn.net/u012067766/article/details/79903455
#关于寻找所有图片的xpath路径：找这些图片分别xpath的规律，提取最后一段，需要多试
#zip函数：https://www.runoob.com/?s=zip
import time
import os
import requests
from lxml import etree
from selenium import webdriver

#首先设置图片存储路径
name=input("请输入演员名:")
path='/Users/youxie/Desktop/豆瓣海报图片'
#设置图片目录
picpath=path+'/'+name
print(picpath)
if not os.path.isdir(picpath):
    os.mkdir(picpath)

#根据图片的URL下载图片
def download(url,id):
    dir=picpath+'/'+str(id)+'.jpg'
    try:
        pic=requests.get(url,timeout=30)
    except:
        print('图片获取失败')
    fp=open(dir,'wb')
    fp.write(pic.content)
    fp.close()
    
#使用webdriver自动获取海报图片的URL

def main():
    driver = webdriver.Chrome('/Users/youxie/Desktop/chromedriver/chromedriver')
    for i in range(0,10*15,15):
        homeurl = 'https://movie.douban.com/subject_search?search_text=' + name + '&cat=1002' + '&start=' + str(i)
        driver.get(homeurl)
        time.sleep(1)
        html=etree.HTML(driver.page_source)
        url_xpath="//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
        title_xpath="//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
        urls=html.xpath(url_xpath)
        titles=html.xpath(title_xpath)
        for url,title in zip(urls,titles):
            url=url.replace('webp','jpg')
            print('\t'.join([str(url), str(title.text)]))
            download(url,title.text)
    print("下载完成")
main()


# In[14]:





# In[ ]:




