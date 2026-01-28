'''
这个程序跑不了，因为我的api_key是第三方的，不适配OpenAI函数，但是无所谓了
'''

from dotenv import load_dotenv

load_dotenv()
import os
base_url = os.environ.get("BASE_URL2")
api_key = os.environ.get("API_KEY2")

from llama_index.core import SimpleDirectoryReader
documents = SimpleDirectoryReader(".").load_data()

from llama_index.core import VectorStoreIndex
index = VectorStoreIndex.from_documents(documents)

from llama_index.llms.openai_like import OpenAILike
from llama_index.core import Settings

llm = OpenAILike(
    api_key=api_key,
    model = "gpt-4.1",
    base_url=base_url
)
Settings.llm = llm

query_engine = index.as_query_engine()

response = query_engine.query("深圳市纳税人身份信息报告申请条件是什么？")
print("深圳市纳税人身份信息报告申请条件是什么？ ", response)
response = query_engine.query("深圳市纳税人身份信息报告的办理流程？")
print("深圳市纳税人身份信息报告的办理流程？ ", response)

index.storage_context.persist()
