from openai import OpenAI
import os

# 1.获取客户端对象

api_key = os.getenv("DASHSCOPE_API_KEY")
if not api_key:
    raise ValueError("未找到环境变量 DASHSCOPE_API_KEY，请先配置 API Key")

client = OpenAI(
    api_key=api_key,
    base_url="https://ws-3sl9qxa7tpgtbbm0.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

# Few-Shot 示例数据（交错排列，避免答案顺序偏置）
examples_data = [
    ("是", "公司ABC发布了季度财报，显示盈利增长。", "财报披露，公司ABC利润上升。"),
    ("不是", "黄金价格下跌，投资者抛售。", "外汇市场交易额创下新高。"),
    ("是", "公司ITCAST发布了年度财报，显示盈利大幅度增长。", "财报披露，公司ITCAST更赚钱了。"),
    ("不是", "央行降息，刺激经济增长。", "新能源技术的创新。")
]

# 待测试的问题（每个元素是一个包含两段文本的元组）
questions = [
    ("利率上升，影响房地产市场。", "高利率对房地产有一定的冲击。"),
    ("油价大幅度下跌，能源公司面临挑战。", "未来智能城市的建设趋势越加明显。"),
    ("股票市场今日大涨，投资者乐观。", "持续上涨的市场让投资者感到满意。")
]
messages = [
    {"role": "system", "content": "帮我判断文本是否匹配,我给你两个分别用[]包起来两个的句子，你需要判断是否匹配，回答是或者不是，请参考如下示例："}
]
for label, s1, s2 in examples_data:
    messages.append({"role": "user", "content": f"句子1[{s1}],句子2[{s2}]"})
    messages.append({"role": "assistant", "content": label})

for q in questions:
    response = client.chat.completions.create(
        model="qwen3.8-max",  # 您可以按需更换为其它深度思考模型
        messages=messages + [{"role": "user", "content": f"句子1[{q[0]}],句子2[{q[1]}]"}],
        stream=False
    )
    print(response.choices[0].message.content.strip())
