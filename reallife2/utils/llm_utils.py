import os
import re
from typing import Optional

# 配置相关
from llama_index.llms.openai import OpenAI

# 日志相关
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 初始化 LLM 和 Embedding 模型
llm = OpenAI(
    model="o3-mini",
    api_key=os.getenv("BIANXIE_API_KEY"),
    api_base='https://api.bianxieai.com/v1',
    temperature=0.1,
)


# 数据读取相关
def read_file(file_path: str) -> str:
    """
    读取文件内容
    :param file_path: 文件路径
    :return: 文件内容字符串
    """
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"文件 {file_path} 未找到")
        return ""
    except Exception as e:
        logging.error(f"读取文件时发生错误: {e}")
        return ""

# 正则解析相关
def parse_execution_pool(text: str) -> Optional[str]:
    """
    使用正则表达式解析 "执行池" 内容
    :param text: 输入文本
    :return: 解析后的执行池内容
    """
    pattern = r'## 执行池\n(.+?)\n##'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        content = match.group(1).strip()
        formatted_content = '\n'.join([line.strip() for line in content.split('\n') if line.strip()])
        return formatted_content
    else:
        logging.warning("未找到匹配的执行池内容")
        return None
from datetime import datetime


# AI 处理相关
def generate_schedule(text: str,habit: str="") -> str:
    """
    使用 GPT 模型生成日程安排
    :param text: 输入文本
    :return: 生成的日程安排结果
    """
    current_utc_time = str(datetime.today())[:-7]

    prompt = f"""
    你是一个日程管理者, 擅长做日程安排并按照标准格式输出.

    有以下几点需要注意:
        1 **不需要输出多余内容 严格按照输出格式**.
        2 将日常规划做到未来时间, 而不是已经过去的时间, 现在的时间为: {current_utc_time}
        3 日常规划要避开用户习惯占用的时间

    用户习惯:
    ---
    {habit}
    ---

    输出格式:
    我会输入一段文字,里面包含了我今天需要做的任务的标题,以及任务预估的消耗时间(例如2P P代表一个番茄钟,也就是30分钟 2P就是60分钟)
    任务可以拆开, 只需要保证总时间是对的.
    我希望可以获得合理的时间安排并按照 "开始时间 结束时间 任务标题" 的格式输出,其中 "$" 是分隔符,标签以 # 开头应该去掉.


    例子输入:
    ---
    - [ ] 2P 研究一下算法知识吧
    - [ ] 2P 数据结构 #长期
    - [ ] 4P 时间复杂度算法 #长期
    - [ ] 4P 做一些整理和知识层面上 的游走

    例子输出:
    2月11日8:00$2月11日9:00$研究一下算法知识吧
    2月11日9:00$2月11日10:00$数据结构
    2月11日13:00$2月11日15:00$时间复杂度算法
    2月11日17:00$2月11日19:00$做一些整理和知识层面上 的游走

    ---
    {text}
    """.format(text=text,habit=habit,current_utc_time = current_utc_time)
    completion = llm.complete(prompt)
    return completion.text if completion else ''



from llama_index.core import PromptTemplate
import subprocess

def update_calulate(start_date = "2025年4月25日8:00",
                    end_date = "2025年4月25日9:00",
                    event_name = "会议w",
                    ):
    script = PromptTemplate(template='''
    tell application "Calendar"
        activate
        tell calendar "Obsidian" -- 或者 tell first calendar
            -- nih
            -- 假设您已经将开始时间、结束时间和标题存储在变量中
            set theStartDate to date "{start_date}" -- 示例日期时间
            set theEndDate to date "{end_date}" -- 示例日期时间
            set theSummary to "{event_name}" -- 示例标题
            make new event with properties {summary:theSummary, start date:theStartDate, end date:theEndDate}
        end tell
    end tell
    ''')

    # 构造 AppleScript 脚本
    scrip = script.format(start_date=start_date,end_date=end_date,event_name=event_name)

    # 执行 AppleScript 脚本
    subprocess.run(['/usr/bin/osascript', '-e', scrip])













