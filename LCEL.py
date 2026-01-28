from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("api_key2")
base_url = os.environ.get("base_url2")

print(api_key)
print(base_url)

prompt = ChatPromptTemplate.from_template("请讲一个关于{topic}的故事")

model = ChatOpenAI(model = "gpt-4",
                   api_key = api_key,
                   base_url = base_url)
output_parser = StrOutputParser()
chain = prompt|model|output_parser
message = chain.invoke({"topic":"水仙花"})
print(message)