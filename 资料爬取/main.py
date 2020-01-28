#coding=utf-8
import urllib.request
import urllib
import re
import os
from bs4 import BeautifulSoup
from pictures import pictures as p 
from text import text as t

print(u'---------准备开始网页抓取图片，现在进行准备工作----------')

#首先，要使用请求头，防止主机ip因请求频繁，导致被封
Mozila_headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

url=input("链接地址为：")
#进行检验工作
while urllib.request.urlopen(url).code != 200:
    print(u'---------请正确输入地址！----------')
    url=input("～(￣▽￣～)链接地址为：")

day=input("是第几天（输入一个数字即可）：")
#同样要进行检验
day_int=int(day)
while day_int<1 or day_int>30:
    print("请重新输入正确天数")
    day=input("是第几天（输入的数字需在1~30）:")


#文件储存地址设置
path_select=input("是否使用默认爬取文件储存地址（Y/N）？")
if path_select=="Y" or path_select=="y" or path_select=="Yes" or path_select=="yes":
    #文件夹命名加上天数，以加以区别
    path="d:\\CS书籍推荐\CS master\考研30天资料\Day" + day
else:
    path=input("请输入文件存储地址（格式为D:\\...\）：")

if not os.path.isdir(path):
    print("默认地址不存在，现在新建了一个文件夹地址")
    os.makedirs(path)

paths=path+"\\"

print(u'----------正在获取图片---------')
    


#打开网页,读取源码
def getHtml(url):
    page=urllib.request.urlopen(url,timeout=10)
    print(page)
    html=page.read()
    return html.decode('UTF-8')

html=getHtml(url)

pngList=p.getPng(html)
jpgList=p.getJpg(html)
p.reserve_pictures(pngList,jpgList,paths)

t.reserve_text(url,day,Mozila_headers,paths)
print("文本内容已爬取完毕")

