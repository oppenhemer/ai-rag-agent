from langchain_community.llms import Tongyi

model = Tongyi(model="qwen-max", temperature=0.7)

# 导入few-shot提示词模板类
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate

example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")
example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "快乐", "antonym": "悲伤"}
]
fewshot_prompt = FewShotPromptTemplate(
    examples=example_data,
    example_prompt=example_template,
    prefix="告诉我单词的反义词，参考下面的示例",
    suffix="基于前面示例数据告诉我,{input_word}的反义词是？",
    input_variables=["input_word"]
)
# format_prompt 只接受关键字参数，变量名要和 suffix 里的 {input_word} 一致
text = fewshot_prompt.format_prompt(input_word="贫穷").to_string()
print(text)
res = model.invoke(text)
print(res)
