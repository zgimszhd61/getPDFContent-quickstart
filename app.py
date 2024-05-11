# !pip install PyPDF2
from PyPDF2 import PdfReader
import re
import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-"

def askGPT3(mprompt,name):
    sprompt = """
    请将下面内容翻译成中文,说人话,使之更符合中国人阅读理解习惯。
    """
    client = OpenAI()
    try:
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
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
  
  # ## 去掉摘要之前内容.
  # if "Abstract\n" in completeText:
  #   completeText = "Abstract\n" + completeText.split("Abstract\n")[1]


  if "Introduction\n" in completeText:
    completeText = "Introduction\n" + completeText.split("Introduction\n")[1]
  ## 去掉引用.
  if "References\n" in completeText:
    completeText = completeText.split("References\n")[0]

  if "REFERENCES" in completeText:
    completeText = completeText.split("REFERENCES")[0]

  ## 使用replace来识别和所有并不是以.结尾的换行(\n)
  completeText = re.sub(r'(?<=[^.])\n', ' ', completeText)

  print(len(completeText.split("\n")))
  for line in completeText.split("\n"):
    if len(line) > 2:
      ## 启发式去除数据.
      if "Publication date:" in line:
         continue
      askGPT3(line,name)
      # print(line)
      print()

mainv2("2401.13802v3.pdf")
