import requests
from PyPDF2 import PdfReader

def realtimeQuestion():
   pass

def mainv2():
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
    page = reader.pages[0]
    text = page.extract_text()
    try:
        text = text.replace("\n"," ").replace("- ","").lower().strip().replace(" —","").replace("^ ","").replace("\n ","")
        text = text.split("abstract")[1].split("introduction")[0].split(". 1")[0]
        print(text)
        # realtimeQuestion(text)
    except:
        print("ERROR")
mainv2()