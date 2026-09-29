# 使用 LangChain 访问通义千问大语言模型（文本模型接口）
# LangChain 把模型分成两类接口：LLM(文本模型) 和 ChatModel(对话模型)
# 文本模型：传入纯字符串提示，返回纯文本；对话模型：传入消息列表，返回消息对象
import os

from langchain_community.llms import Tongyi

# 1.创建文本模型对象（Tongyi 底层依赖 dashscope 包，读取 DASHSCOPE_API_KEY）
llm = Tongyi(
    model="qwen-max",
    temperature=0.7
)

# 2.简单调用：传入字符串，返回纯文本
response = llm.invoke("什么是RAG？请用一句话回答")
print("简单调用：", response)

# 3.流式输出：逐块返回字符串片段
print("流式输出：", end="")
for chunk in llm.stream("请写一篇关于春天的短诗"):
    print(chunk, end="", flush=True)
print()
