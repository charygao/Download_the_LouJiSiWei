#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request #网络
import re #引入正则表达式
f = open('luoji.txt', 'w',encoding='utf-8')#保存获取到的文件名，下载连接，原文链接
batFile = open('luoji.bat', 'w')#生成wget下载批处理
'''
从http://www.ljsw.cc/forum-39-1.html获取所有罗辑思维的语音连接，并保持到luoji.txt
@author: HK
'''
def getHtmlCode(url):#获取html代码
    print('正在获取html代码的地址： '+url)
    return urllib.request.urlopen(url).read().decode('UTF-8')

def getTitle(htmlString):#获取文件名
    regTitle = re.compile('onclick="atarget\(this\)" class="s xst">(.+?)</a>')
    return regTitle.findall(htmlString)

def getMp3Url(htmlString):#获取mp3下载连接
    regMp3 = re.compile('\<audio src="(.+?)" controls="true" preload="none"\>\</audio\>')
    return regMp3.findall(htmlString)

def getUrl(htmlCode):#获取原文链接
    regUrls = re.compile('<a href="(.+?)" onclick="atarget\(this\)" class="s xst">')
    return regUrls.findall(htmlCode)

def getLuojiContent(url,witchOne):#创建luoji.txt文件
    htmlCode = getHtmlCode(url)
#     open(url.split('-39-')[1],'w',encoding='utf-8').write(htmlCode)
    titles = getTitle(htmlCode)
#     f.write('\n'.join(titles))
    urls = getUrl(htmlCode)
#     f.write('\n'.join(urls))
    for i in range(0,len(urls)):        
        contentHtml = getHtmlCode(urls[i])
        contents = getMp3Url(contentHtml)      
        print(witchOne+str(i)+'/'+str(len(urls)))
        print('资源： '+titles[i]+'{{from}}'+urls[i])
        f.write('资源： '+titles[i]+'{{from}}'+urls[i]+'\n')
        if len(contents):
            print('解析到的资源： '+titles[i]+'{{href}}'+contents[0]+'{{from}}'+urls[i])
            f.write(titles[i]+'{{href}}'+contents[0]+'{{from}}'+urls[i]+'\n')
            cmd = 'wget -c "'+contents[0]+'"  -O "'+validateTitle(titles[i],'')+'.MP3"\n'
            batFile.write(cmd)
           
def validateTitle(title,WithChar):#返回规范的文件名
    rstr = r"[\/\\\:\*\?\"\<\>\|\(\)]"  # '/\:*?"<>|';<>,/,\,|,:,"",*,? 
    new_title = re.sub(rstr, WithChar, title)
    return new_title
                
if __name__ == '__main__':
    lastPage = 57
    for i in range(1,lastPage):
        url = 'http://www.ljsw.cc/forum-39-'+str(i)+'.html'
        progress = str(i)+'/'+str(lastPage)
        print(progress+'start: '+url)
#         try:
        getLuojiContent(url,progress)
        print(progress+'finished: ' + url)
#         except:  
#             print(progress+'error: ' + url)
    print("txt创建完成！")
    f.close()
    batFile.close()