# !pip install PyPDF2
from PyPDF2 import PdfReader
import re
import os
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

def askGPT3(mprompt,name):
    sprompt = """
    请将下面内容翻译成中文,说人话,使之更符合中国人阅读理解习惯。
    """
    client = OpenAI()
    try:
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": sprompt},
            {"role": "user", "content": mprompt}
        ]
        )
        result = completion.choices[0].message.content.strip()
        print(result)
        filename = name+".txt"
        writecontent(result,filename)
        return(result)
    except:
        print("ERROR")
        
def writecontent(content,filename):
    with open('/Users/a0000/mywork/commonLLM/opensource/nnnew/getPDFContent-quickstart/'+filename, 'a+') as file:
        file.write(content)

def mainv2(name):
  completeText = ""
  reader = PdfReader(name)

  # number_of_pages = len(reader.pages)

  for page in reader.pages:
    text = page.extract_text()
    completeText = completeText + text
  
  print(completeText)

filepath = "688570_20240527_2DEC.pdf"
print("""以下是一份问询函公告，请使用最简单的表达方式说明其中关键内容，返回一个表格，表格里每一行包含2列，覆盖：问题、答案说明。
-----
""")
mainv2(filepath)
