# 导入解析器类
from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
# 导入模板类
from langchain_core.prompts import PromptTemplate
# 导入聊天大模型
from langchain_community.chat_models import ChatTongyi

# 初始化大模型
model = ChatTongyi(model="qwen-max", temperature=0.7)

# 创建提示词模板（from_template 会自动从 {} 中识别变量，不能再手动传 input_variables）
First_template = PromptTemplate.from_template(
    "我的孩子姓{name},性别为{gender},然后帮我起一个名字,只需要告诉我名字,不需要其他内容，帮我封装成json格式"
    "要求key为name,value为起的名字"
)
Second_template = PromptTemplate.from_template("这个{name}有什么寓意吗")
strParse = JsonOutputParser()
jsonParse = JsonOutputParser()

chain = First_template | model | jsonParse | Second_template | model
res = chain.invoke({"name": "方", "gender": "女儿"})
print(res.content)
print(type(res))



