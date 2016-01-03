'''
合并所有Mp3文件到一个文件。
@author: HK
'''
import shutil
import os
'''
# 获取指定路径下所有指定后缀的文件
# dir 指定路径
# ext 指定后缀，链表&不需要带点 或者不指定。例子：['xml', 'java']
'''  
def GetFileFromThisRootDir(Path,ext = None):
    allfiles = []
    needExtFilter = (ext != None)
#     i = 0
    for root,dirs,files in os.walk(Path):
#         print(str(i)+'root:')
#         print(root+'\n')
#         print(str(i)+'dirs:')
        print('\ndirs:'.join(dirs)+'\n')
#         print(str(i)+'files:')
#         print('\nfiles:'.join(files)+'\n')
#         i+=1
        for filespath in files:
            filepath = os.path.join(root, filespath)
#             print(filepath)
            extension = os.path.splitext(filepath)[1][1:]
#             print(extension)
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
            elif not needExtFilter:
                allfiles.append(filepath)
    return allfiles
if __name__ == '__main__':
    PATH=os.path.abspath(os.curdir)
    mp3s = GetFileFromThisRootDir(PATH,['mp3'])
    print('\n'.join(mp3s))
    combinedMp3Name = os.path.join(PATH, 'louji.mp3')
    destination = open(combinedMp3Name, 'wb')
    print(combinedMp3Name)
    for filename in mp3s:
        print('正在合并的文件：'+filename)
        shutil.copyfileobj(open(filename, 'rb'), destination) 
    destination.close()
#from glob import iglob
#import shutil
#import os
#PATH = r'mp3'
#destination = open('luoji.mp3', 'wb')
#for filename in iglob(os.path.join(PATH, '*.mp3')):
#shutil.copyfileobj(open(filename, 'rb'), destination) destination.close()
