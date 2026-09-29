# 导入聊天chatTemplate模板
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
# 导入大语言模型
from langchain_community.llms import Tongyi
model = Tongyi(model="qwen-max", temperature=0.7)
# 创建聊天模板对象
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system","你是一名边塞诗人"),
        MessagesPlaceholder("history"),
        ("human","写一首关于国家的诗")
    ]
)

# 补充聊天会话记录
history = [
    ("user","写一首关于大漠的诗"),
    ("ai","白发三千丈，高挂云间。")
]
text = chat_template.invoke({"history":history}).to_string()
print(text)
res = model.invoke(text)
print(res)
