from openai import OpenAI
import os

"""
期望的最终输出格式（必须是标准 Python 列表，顺序一一对应）：
python
['新闻报道', '公司公告', '财务公告', '分析师报告'] 
"""

# 1.获取客户端对象

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-3sl9qxa7tpgtbbm0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

# texts = [
#     "今日，央行发布公告宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
#     "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC"
#     "公司在行业中的地位，并为未来业务发展提供更广阔的发展空间。详情请见公司官方网站公告栏",
#     "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
#     "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会"
# ]
examples_data = {
    "新闻报道": "今日，央行发布公告宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
    "公司公告": "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC"
}
# 2.调用模型
messages = [
    {"role": "system", "content": "你是一个专业的金融文本分类器。请将用户输入的金融新闻分类为以下四类之一：['新闻报道', '公司公告', '财务公告', '分析师报告'] "
                                  "。不清楚的输出'不清楚'"},
]
quesion_data = ["公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。", "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会"]

for key, value in examples_data.items():
    messages.append({"role": "user", "content": value})
    messages.append({"role": "assistant", "content": key})

for key in quesion_data:
    messages.append({"role": "user", "content": key})
    completion = client.chat.completions.create(
        model="qwen3.8-max",  # 您可以按需更换为其它深度思考模型
        messages=messages,
        extra_body={"enable_thinking": True},
        stream=False
    )
    response = completion.choices[0].message.content
    print(response)
    messages.append({"role":"assistant","content":response})

