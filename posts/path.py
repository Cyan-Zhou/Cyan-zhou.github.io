import pyperclip
import re

while True:
    longline = input("请输入含有图片链接的文本(输入'q'结束程序)：")
    match = re.search(r'!\[image\.png\]\((.*?)\)', longline)
    url = match.group(1) if match else None
    
    if url == 'q':
        break
    else:
        output = "<center><a data-fancybox=\"gallery\" href=\"%s\"><img src=\"%s\"></a></center>" % (url, url)
        print(output)
        pyperclip.copy(output)
        print("输出已复制到剪贴板")

