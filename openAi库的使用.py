from openai import OpenAI
import os

# 1.获取客户端对象

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-3sl9qxa7tpgtbbm0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

# 2.调用模型
messages = [
    {"role": "system", "content": "你是AI助理，回答很简洁"},
    {"role": "user", "content": "小明有2条宠物狗"},
    {"role": "assistant", "content": "好的"},
    {"role": "user", "content": "小红有3只宠物猫"},
    {"role": "assistant", "content": "好的"},
    {"role": "user", "content": "总共有几个宠物？"},
]
stream = client.chat.completions.create(
    model="qwen3.8-max",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)

# # 3.处理结果
# response = completion.choices[0].message.content
# print(response)

# 流式输出结果
full = ""
for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if delta.content:
        full += delta.content
        print(delta.content, end="", flush=True)

print("\n完整内容：", full)

