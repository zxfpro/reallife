"""
获取酱油池中的内容到备忘录
"""
import os
import re
import json
from typing import Optional
from datetime import datetime
import subprocess

obsidian = "/Users/zhaoxuefeng/GitHub/obsidian"

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
        print(f"文件 {file_path} 未找到")
        return ""
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return ""

# 正则解析相关
def parse_execution_pool(text: str) -> Optional[str]:
    """
    使用正则表达式解析 "执行池" 内容
    :param text: 输入文本
    :return: 解析后的执行池内容
    """
    pattern = r'## 酱油池\n(.+?)\n\n'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        content = match.group(1).strip()
        formatted_content = '\n'.join([line.strip() for line in content.split('\n') if line.strip()])
        return formatted_content
    else:
        print("未找到匹配的执行池内容")
        return None

def write_notes(content):
    content = content.replace("\n","换行")
    # 构造 AppleScript 脚本  TODO 解决无法换行问题
    script = f'''
    tell application "Notes"
        activate
        -- 获取默认账户
        set defaultAccount to default account
        -- 创建一个新的备忘录
        set newNote to make new note in defaultAccount
        -- 写入文本信息到备忘录
        set body of newNote to "{content}"
        -- 显示新创建的备忘录
        show newNote
    end tell
    '''

    # 执行 AppleScript 脚本
    subprocess.run(['/usr/bin/osascript', '-e', script])

# 主程序入口
def sync_notes_function():
    # 参数配置
    file_path = f"{obsidian}/工作/事件看板/事件看板.md"
    # 读取文件
    text = read_file(file_path)
    # 解析执行池
    execution_pool = parse_execution_pool(text)

    # 生成日程安排
    current_utc_time = datetime.utcnow()
    schedule_result = str(current_utc_time)[:10] + '\n' + execution_pool

    write_notes(schedule_result)

