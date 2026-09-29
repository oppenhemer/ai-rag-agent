from openai import OpenAI
import os
import json


# 需要抽取的字段
schema = ["期数", "中奖号码", "一等奖"]
# 1.获取客户端对象

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-3sl9qxa7tpgtbbm0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)
# Few-Shot 示例数据（图片中给出的文本和期望结果）
examples_data = [
    {
        "content": "2025年第100期，开好红球22 21 06 01 03 11 篮球 07，一等奖中奖为2注。",
        "answers": {
            "期数": "2025100",
            "中奖号码": [1, 3, 6, 11, 21, 22, 7],
            "一等奖": "2注"
        }
    },
    {
        "content": "2025101期，有3注1等奖，10注2等奖，开号篮球11，中奖红球3、5、7、11、12、16。",
        "answers": {
            "期数": "2025101",
            "中奖号码": [3, 5, 7, 11, 12, 16, 11],
            "一等奖": "3注"
        }
    }
]

# 待测试的数据（这里先放这两条，你可以自己编第3、4、5条）
questions = [
    "2025年第102期，开奖红球05 08 12 15 20 28 篮球 09，一等奖中奖为1注。",
    "2025103期，有5注1等奖，开号篮球02，中奖红球1、4、9、14、22、30。"
]
messages = [{"role": "system", "content": f"你帮我完成信息抽取，我给你句子，你抽取{schema}信息，按JSON字符串输出，如果某些信息不存在，用'原文未提及'表示，请参考如下示例："}]
for example in examples_data:
    messages.append({"role": "user", "content":example["content"]})
    messages.append({"role": "assistant", "content": json.dumps(example["answers"])})

for q in questions:
    response = client.chat.completions.create(
        model="qwen3.8-max",  # 您可以按需更换为其它深度思考模型
        messages=messages + [{"role": "user", "content": q}],
        extra_body={"enable_thinking": True},
        stream=False
    )
    print(response.choices[0].message.content)
