import requests

url = "https://static.sse.com.cn/disclosure/listedinfo/announcement/c/new/2024-05-27/603037_20240527_QEJI.pdf"

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

