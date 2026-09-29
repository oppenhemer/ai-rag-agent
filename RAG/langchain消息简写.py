from langchain_community.chat_models import ChatTongyi

# 1.创建聊天模型对象（ChatTongyi 底层依赖 dashscope 包，读取 DASHSCOPE_API_KEY）
model = ChatTongyi(
    model="qwen3-max",
    temperature=0.7
)
messages = [
    ("system", "你是一个 helpful的助手。"),
    ("human", "请写一篇关于春天的短诗。")
]
res = model.stream(messages)
# 2.流式输出：聊天模型返回 AIMessageChunk 对象，文本内容在 .content 里
print("流式输出：", end="")
for chunk in res:
    print(chunk.content, end="", flush=True)
print()
