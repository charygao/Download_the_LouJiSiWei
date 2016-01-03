#coding=utf-8
'''
下载文件时要调用外部下载工具，可以用curl，这里用wget
下载所有luoji.txt文件中的MP3到当前文件，并改名
@author: HK
'''
import os
if __name__ == '__main__':   
    for line in open('luoji.txt','+r',encoding='utf-8'):
        contents = line.split('{{href}}')
        downloadUrl = contents[1].split('{{from}}')
        print('马上下载：'+downloadUrl[0]+'文件名：'+contents[0])
        cmd = 'wget --continue --timestamping "'+downloadUrl[0]+'"'
        os.system(cmd)
        urlFilenames = downloadUrl[0].split('/')
        downedName =urlFilenames[len(urlFilenames)-1]
        print('更正命名：'+downedName,contents[0]+'.mp3')
        os.rename(downedName,contents[0]+'.mp3')


