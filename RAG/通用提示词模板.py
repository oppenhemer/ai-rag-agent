# 导入大语言模型
from langchain_community.llms import Tongyi
# 导入提示词模型类
from langchain_core.prompts import PromptTemplate

# 创建提示词模板
prompt_template = PromptTemplate(
    template="What is the capital of {country}?",
    input_variables=["country"]
)

# 1.format()：直接返回填好值的纯字符串
print(prompt_template.format(country="France"))

# 2.invoke()：传入变量字典，返回 StringPromptValue 对象（链式调用中的标准形式）
print(prompt_template.invoke({"country": "Japan"}))

# 3.from_template()：自动从模板里推断 input_variables，省得手写
auto_template = PromptTemplate.from_template("用三句话向{audience}解释{topic}。")
print(auto_template.input_variables)  # ['audience', 'topic']
print(auto_template.format(audience="小学生", topic="量子计算"))

# 2.使用大语言模型
model = Tongyi(
    model = "qwen-max",
    temperature=0.7  # temperature（温度）控制模型生成文本时的随机程度
)
res = model.invoke(prompt_template.format(country="France"))
print(res)
