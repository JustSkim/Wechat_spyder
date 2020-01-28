#coding=utf-8
import urllib.request
import urllib
import re
import os
from bs4 import BeautifulSoup

class pictures:

    #正则表达式，定位所有图片
    def getPng(html):
        reg_png=r'data-src="(https://mmbiz.qpic.cn/mmbiz_png.{5,200}\=png)"'
        
        imgre=re.compile(reg_png)#编译一下，提升运行速度
        imglist=imgre.findall(html)#匹配
        return imglist

    def getJpg(html):
        #注意jpeg格式图片和png格式图片在资源地址上的诸多不同
        reg_jpg=r'data-src="(https://mmbiz.qpic.cn/mmbiz_jpg.{5,200}\=jpeg)"'
        imgre=re.compile(reg_jpg)
        imglist=imgre.findall(html)
        return imglist
        
    #对文件指定位置存放
    def reserve_pictures(imglist1,imglist2,paths):
        print("准备")
        num=0

        #因为公众号文章往往有一些广告宣传等无关的信息，会混杂在爬取的图片中
        #可以通过在网页端打开控制台的方法，找出宣传图片的url地址，并将其加入到此处的过滤列表中
        filterlist=["https://mmbiz.qpic.cn/mmbiz_png/hRUkcdhic6aLvBjJGncJ03ZvOa1y4J3EM3kWs2K1BAmf9lKTSMict3LzG4lT8UPo1iaDgnia5zK88mzqdf8SL7BheA/640?wx_fmt=png",
                    "https://mmbiz.qpic.cn/mmbiz_png/hRUkcdhic6aLvBjJGncJ03ZvOa1y4J3EM1eYxAKFHSpWOjJ67AZPBbibLMUj6IUJDokMGnnqEN1RM5htx8H0qArg/640?wx_fmt=png",
                    "https://mmbiz.qpic.cn/mmbiz_png/hRUkcdhic6aITBrcvkMGnGDqXqUcG5eTUrI4nsdiaRIHo2rVicWIUaHRLdmnMeZx69yFlTl3vlGtRnccDrgfUR6XQ/640?wx_fmt=png",
                    "https://mmbiz.qpic.cn/mmbiz_png/hRUkcdhic6aITBrcvkMGnGDqXqUcG5eTUsGYSl08caPpXbHEjFToTb9pGTZrKF7uYHoereYfHscM5hlb2SXLqjA/640?wx_fmt=png"]

        for img1 in imglist1:
            #对广告、宣传图片等无用信息进行多次过滤
            if img1 in filterlist:
                continue
            num=num+1
            print("\n",img1,"\n")
            urllib.request.urlretrieve(img1,'{}{}.jpg'.format(paths,num))#以第二个名字下载链接
        print("png格式图片已爬取完毕")
        
        for img2 in imglist2:
            if img2 in filterlist:
                continue
            num=num+1
            print("\n",img2,"\n")
            urllib.request.urlretrieve(img2,'{}{}.jpg'.format(paths,num))
        print("jpg格式图片已爬取完毕")
        return num