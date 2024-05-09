# python3
from openai import OpenAI

client = OpenAI(api_key="sk-60d9f89423204ed781979dcf75ad0d7f", base_url="https://api.deepseek.com/")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ]
)

print(response.choices[0].message.content)
