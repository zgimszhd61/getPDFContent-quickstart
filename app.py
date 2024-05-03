# !pip install PyPDF2
from PyPDF2 import PdfReader
import os,re

def mainv2(name):
  completeText = ""
  reader = PdfReader(name)

  number_of_pages = len(reader.pages)

  for page in reader.pages:
    text = page.extract_text()
    completeText = completeText + text
  
  ## 去掉摘要之前内容.
  if "Abstract\n" in completeText:
    completeText = "Abstract\n" + completeText.split("Abstract\n")[1]
  ## 去掉引用.
  if "References\n" in completeText:
    completeText = completeText.split("References\n")[0]
  ## 使用replace来识别和所有并不是以.结尾的换行(\n)
  completeText = re.sub(r'(?<=[^.])\n', ' ', completeText)

  print(completeText)

mainv2("2404.08634v1.pdf")
