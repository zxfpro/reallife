"""
收集每日资讯 V1
"""

import requests
from bs4 import BeautifulSoup
import os
# 配置相关
from llama_index.llms.openai import OpenAI

import requests
from bs4 import BeautifulSoup
from datetime import datetime

from functools import lru_cache


# 初始化 LLM 和 Embedding 模型
llm = OpenAI(
    model="gpt-4o",
    api_key=os.getenv("BIANXIE_API_KEY"),
    api_base='https://api.bianxieai.com/v1',
    temperature=0.1,
)
obsidian = "/Users/zhaoxuefeng/GitHub/obsidian"

def get_context_from_jq_url(url):
    # 目标网页的 URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # 发送 HTTP 请求获取网页内容
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 HTML 内容
        soup = BeautifulSoup(response.content, 'html.parser')

        # 提取网页中的文字内容
        text = soup.get_text()
        return text
        # 打印提取的文字内容
    else:
        print("请求失败，状态码：", response.status_code)
        return ''


@lru_cache(maxsize=100)
def extra_text(text):
    print('run extra_text')
    resp = llm.complete(f"""
    我希望你可以对一个内容进行汇总和总结, 我会给你一段网页的内容，你来用一些简短的文字告诉我这篇内容的主要信息, 以及列出其中相关的重点和链接

    网页内容:
    ---
    {text}
    ---

    输出信息:
    """)
    return resp.text


def get_articlie_link():
    # 目标网页的 URL
    url = "https://www.jiqizhixin.com"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # 发送 HTTP 请求获取网页内容
    # response = requests.get(url)
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 HTML 内容
        soup = BeautifulSoup(response.content, 'html.parser')

        # 提取所有文件链接
        file_links = []
        for link in soup.find_all('a', href=True,attrs={
            'class': 'article-item__title t-strong js-open-modal',
        }):
            href = link['href']
            file_links.append(url + href)
    else:
        print("请求失败，状态码：", response.status_code)
    return file_links

def sync_news_func(date:str):
    file_links = get_articlie_link()
    print(file_links,'file_links')
    article = []
    for file_link in file_links:
        print(file_link)
        result = get_context_from_jq_url(file_link)
        xx = extra_text(result)
        article.append(xx)

    file_path = f"{obsidian}/工作/日记/{date}.md"
    with open(file_path,'a') as f:
        f.write("\n\n# 今日资讯\n---\n## 消息\n" +'\n\n---\n## 消息\n'.join(article))


if __name__ == "__main__":
    sync_news_func('2025-02-12')