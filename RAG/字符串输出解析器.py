# 导入模型类
from langchain_community.chat_models import ChatTongyi
# 导入模板类
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# 创建模型
model = ChatTongyi(model="qwen-max", temperature=0.7)

# 创建提示词模板   from_template 自动提取变量
prompt_template = PromptTemplate.from_template("你知道{city}在哪儿吗")

parse = StrOutputParser()
chain = prompt_template | model | parse | model
print(chain.invoke({"city": "北京"}).content)





