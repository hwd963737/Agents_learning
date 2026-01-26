from dotenv import load_dotenv
load_dotenv()

import os
base_url = os.environ.get("base_url")
api_key = os.environ.get("api_key")

print(base_url)
print(api_key)

from openai import OpenAI
client = OpenAI(api_key=api_key,
                base_url=base_url)
response = client.chat.completions.create(
    model = "gpt-4o-mini",
    response_format = {"type": "json_object"},
    messages = [
        {"role": "system", "content": "您是一个帮助用户了解鲜花信息的智能助手，并能够输出JSON格式的的内容。"},
        {"role": "user", "content": "生日送什么花最好？"},
        {"role": "assistant", "content": "玫瑰花是生日礼物的热门选择。"},
        {"role": "user", "content": "送货需要多长时间？" }
    ]
)

# print("原始返回内容:")
# print(repr(response.choices[0].message.content))
#
# import json
# try:
#     content_json = json.loads(response.choices[0].message.content)
#     print("\n解析后的JSON:")
#     print(json.dumps(content_json, ensure_ascii=False, indent=2))
# except:
#     print("响应不是有效的JSON格式")

print(response)
