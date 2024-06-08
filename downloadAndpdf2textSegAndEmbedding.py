# 实现基础能力：PDF -> text -> 分段 -> 嵌入. (24.06.08)
## 能力介绍：
# - 下载，把PDF内容转化成text.
import requests
from PyPDF2 import PdfReader

def realtimeQuestion():
   pass

## TODO:分段检索.
## TODO：文本嵌入，并完成检索.

## Todo：将内容存储到特定txt文件下.
def mainv2():
    mmlist = []
    url = "https://arxiv.org/pdf/2405.17372"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://static.sse.com.cn/',    
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    pdf_file = requests.get(url, headers=headers)
    with open('output.pdf', 'wb') as f:
        f.write(pdf_file.content)

    reader = PdfReader('output.pdf')
    for item in reader.pages:
        page = item
        text = page.extract_text()
        mmlist.append(text)
        print(text)
    print(mmlist)
mainv2()
