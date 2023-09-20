import pyperclip
import re

while True:
    url = input("请输入含有图片链接的文本(输入'q'结束程序)：")
    
    if url == 'q':
        break
    else:
        output = "<center><a data-fancybox=\"gallery\" href=\"%s\"><img src=\"%s\"></a></center>" % (url, url)
        print(output)
        pyperclip.copy(output)
        print("输出已复制到剪贴板")