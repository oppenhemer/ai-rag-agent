# 导入模板类
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 导入大语言模型
from langchain_community.llms import Tongyi
model = Tongyi(model="qwen-max", temperature=0.7)

history_data = [
    ("human", "写一首关于大漠的诗"),
    ("ai", "白发三千丈，高挂云间。")
]
# 创建模板类对象
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一名边塞诗人"),
        MessagesPlaceholder("history"),
        ("human", "写一首关于国家的诗")
    ]
)
# # 基础调用
# text = chat_template.invoke({"history": history_data}).to_string()
# print(text)
# res = model.invoke(text)
# print(res)

# 链式调用
chain = chat_template | model
res = chain.invoke({"history":history_data})
print(res)
