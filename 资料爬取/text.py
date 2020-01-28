#coding=utf-8
import requests
import re
import os
from bs4 import BeautifulSoup
import codecs
class text:

    def reserve_text(url,day,headers,paths):
        
        #文本格式文件的保存
        file_name=input("请输入保存的文件名称（后缀默认为.txt）：")
        txt_paths=paths+file_name+'.txt'
        
        #以追加方式打开该文本文件，指针在末尾
        f = codecs.open(txt_paths,"a+",'utf_8_sig')
        '''
        此次爬取学习中，最大的困难在于编码的转换。的确，网页已给出charset="utf-8"的编码信息，
        但是控制台打印可行，在转码写入txt文件的过程中总是出现乱码、空白两种情况。
        翻阅了无数篇博客都未能解决此问题，最后一个博主介绍转码方法时标注win7系统下不能用，
        这启发了我，想到了可能是win10自带记事本编码、转码方式和python3有区别，
        终于翻阅到了大神的博客https://blog.csdn.net/xiangbq/article/details/51919219╰(￣▽￣)╮
        暂时成功解决问题，写下这段注释的时间：2020-01-28 凌晨01：03
        才发现我被这个小东西给牵制到了大年初四的凌晨一点（响应防疫号召宅在家:>）
        '''


        #检测文本文件是否已存在
        if not f:
            print("error!\n")
            pass
        else:
            textTitle="希鹊考研30天训练营 "+day
            f.write(textTitle+"\n")

        #接下来进行文字题型的爬取，需要注意的是，
        #在公众号文字中，往往没有特殊的CSS样式和id命名
        #需要爬取题目前标题文字

        #将获取到的内容转换为BeautifulSoup格式，使用html.parser作为解析器
        html = requests.get(url,headers).content  
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

        #因为每个关键的红色标题没有id、class，而都是一致的样式，使用属性选择方式
        redTitleList=soup.find_all('span',attrs={'style':'color: rgb(255, 255, 255);background-color: rgb(255, 41, 65);font-size: 14px;'})

        bigTitleList = soup.find_all("section",attrs={'style':'height: 35px;background: rgb(219, 14, 14);border-radius: 5px;border-width: 1px;border-style: solid;border-color: rgb(255, 216, 59);padding: 0px 35px;display: flex;justify-content: center;align-items: center;flex-wrap: nowrap;font-size: 16px;font-weight: 600;color: rgb(255, 216, 59);line-height: 23px;'})
        if bigTitleList==[]:
            print("出现错误！")
        else:
            EnglishTitle = bigTitleList[0]
            f.write(EnglishTitle.p.string)
            #因为每篇公众号文章的英语部分只有连线、翻译两种题型
            #连线题型在之前已经使用图片爬取功能爬取了，这里只爬取翻译题的文本即可
            EnglishTextList=EnglishTitle.parent.parent.next_sibling.next_sibling.find_all("p")
            for EnglishText in EnglishTextList:
                f.write(EnglishText.get_text()+"\n")

        PoliticTitle = bigTitleList[1]
        p_textList = PoliticTitle.parent.parent.next_sibling.next_sibling.next_sibling.find_all("p")
        for p_text in p_textList:
            f.write(p_text.get_text().encode('utf-8').decode('utf-8')+"\n")
        
        if "休息" in PoliticTitle.p.string:
            f.write("\n今天的马原老师休息，木有题目o(︶︿︶)o\n")

            #如果马原部分没有出题，只有昨日题目答案的话，其网页构成会不一样
            try:
                p_textList = PoliticTitle.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling.find_all("p")
                for p_text in p_textList:
                    f.write(p_text.get_text().encode('utf-8').decode('utf-8')+"\n")
            except AttributeError:
                p_textList = PoliticTitle.parent.parent.next_sibling.next_sibling.find_all("p")
                for p_text in p_textList:
                    f.write(p_text.get_text().encode('utf-8').decode('utf-8')+"\n")
            '''
        try:
            x=1
            for redTitle in redTitleList: 
                #马原题目
                mayuan = "练习"
                x=1
                try:
                    result2 = (mayuan in redTitle.string)
                #NoneType会导致类型异常，在此要加上捕获操作，进行跳过循环
                except TypeError:
                    continue
                print(result2,"\n")
                if (result2 and x):
                    f.write(mayuan)
                    f.write("\n")
                    x=0
                    print("YES\n")
                    try:
                        mayuanList = redTitle.parent.parent.next_sibling.span.span.children
                        for mayuanText in mayuanList:
                            try:
                                #必要的编码格式转换
                                xieru=mayuanText.get_text().encode('utf-8').decode('utf-8')
                                if len(xieru)>199:
                                    xieru1=xieru[:100]
                                    xieru2=xieru[100:]
                                    f.write(xieru1)
                                    f.write(xieru2+'\n')
                                else:
                                    f.write(xieru+'\n')
                            
                            except  AttributeError:
                                f.write("\n")
                            except UnicodeDecodeError:
                                f.write("\n")
                    except AttributeError:
                        print("\n")
                    except UnicodeDecodeError:
                        f.write("\n")
        '''
            

