# 实现基础能力：PDF -> text -> 分段 -> 嵌入. (24.06.08)
## 能力介绍：
# - 下载，把PDF内容转化成text.
import requests
from PyPDF2 import PdfReader

def realtimeQuestion():
   pass

def save_string_to_file(string_variable):
    try:
        with open("ooo.txt", "w") as file:
            file.write(string_variable)
        print("String successfully written to ooo.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

## 下载
def mainv2():
    url = "https://s22.q4cdn.com/959853165/files/doc_events/2024/May/15/netflix-inc-_company-conference-presentation_2024-05-15_english.pdf"

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
    allcontent = ""

    reader = PdfReader('output.pdf')
    for item in reader.pages:
        page = item
        text = page.extract_text()
        # print(text)
        allcontent = allcontent + text.split("†")[0].split("∗Correspondence")[0]
    if "Abstract" in allcontent:
        allcontent = allcontent.split("Abstract")[1]
    
    print("论文地址:{}".format(url))
    if ("interning" in allcontent):
        print("实习生作品，不用看")
    else:
        result = allcontent.split("References")[0].split("Acknowledgement")[0]
        print(result)
        save_string_to_file(result)
mainv2()