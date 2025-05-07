import subprocess
from datetime import datetime
from functools import lru_cache
import requests
from grapherz.canvas.core import Canvas,Color
from kanban.core import Pool,Kanban
from llama_index.core import PromptTemplate
from bs4 import BeautifulSoup
from llmada import BianXieAdapter
from .utils import read_file,parse_execution_pool,parse_execution_jiangyou_pool,status,Date
from promptlibz import Templates,TemplateType

from .kanbantools import KanBanManager


from .utils import Setting

class APPIO():
    def __init__(self):
        self.year = '2025年'
        self.kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md"
        self.habit ="7点-9点起床洗漱, 12点到14点吃饭+午休,19点以后就是自由时间"

    def _update_calulate(self,start_date = "2025年4月25日8:00",
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

    def _write_notes(self,content):
        content = content.replace("\n",",").replace('- [ ]','')
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

    def _write_reminder(self,content, 
                        list_name="Reminders",  # 指定列表名称
                        due_date=None,         # 设置到期日
                        priority=None,         # 设置优先级(1-4)
                        notes=""               # 添加备注
                    ):
        # 预处理内容
        processed_content = content.replace('\n', ' ').replace('- [ ]', '').strip()
        processed_content = processed_content.replace('"', '\\"')
        notes = notes.replace('"', '\\"')
        
        # 构建属性字典
        properties = [f'name:"{processed_content}"']
        if due_date:
            properties.append(f'due date:(date "{due_date}")')
        if priority and 1 <= priority <= 4:
            properties.append(f'priority:{priority}')
        if notes:
            properties.append(f'body:"{notes}"')
        
        # 构造AppleScript
        script = f'''
        tell application "Reminders"
            activate
            set targetList to list "{list_name}"
            make new reminder in targetList with properties {{{', '.join(properties)}}}
        end tell
        '''
        script = f'''
        tell application "Reminders"
            activate
            set targetList to default list
            set newReminder to make new reminder in targetList with properties {{{', '.join(properties)}}}
            show newReminder
        end tell
        '''    
        subprocess.run(['/usr/bin/osascript', '-e', script])

    def _get_context_from_jq_url(self,url):
        # 目标网页的 URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/91.0.4472.124 Safari/537.36"
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
    def _extra_text(self,text):
        template = """
        我希望你可以对一个内容进行汇总和总结, 我会给你一段网页的内容，你来用一些简短的文字告诉我这篇内容的主要信息, 以及列出其中相关的重点和链接

        网页内容:
        ---
        {text}
        ---

        输出信息:
        """

        llm = BianXieAdapter()
        llm.set_model("gpt-4o")
        prompt = template.format(text = text)
        completion = llm.product(prompt)
        return completion

    def _get_articlie_link(self):
        # 目标网页的 URL
        url = "https://www.jiqizhixin.com"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/91.0.4472.124 Safari/537.36"
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

    def sync_calulate(self):

        # 读取文件
        text = read_file(self.kanban_path)

        if not text:
            print("文件内容为空，无法解析执行池")
            return

        # 解析执行池
        execution_pool = parse_execution_pool(text)

        if execution_pool:
            print(f"解析到的执行池内容:\n{execution_pool}")
            # 生成日程安排
            schedule_result = generate_schedule(execution_pool,habit =self.habit)
            xx = [i for i in schedule_result.split('\n') if i!='']
            for xp in xx:
                v = [(self.year+k if i<2 else k) for i,k in enumerate(xp.split('$'))]
                self._update_calulate(*v)

        else:
            print("未能解析到执行池内容")

    def sync_notes(self):
        # 读取文件
        text = read_file(self.kanban_path)
        # 解析执行池
        execution_pool = parse_execution_jiangyou_pool(text)

        # 生成日程安排
        current_utc_time = datetime.utcnow()
        schedule_result = str(current_utc_time)[:10] + '\n' + execution_pool

        self._write_notes(schedule_result)
        for content in schedule_result.split("\n")[1:]:
            self._write_reminder(content, 
                list_name="工作",
                due_date=f"{date_c.date} {date_c.time}",
                priority=2,
                notes="")

    def sync_news(self,date:str):
        """同步咨询到ob

        Args:
            date (str): 日期,字符串格式
        """
        file_links = self._get_articlie_link()
        print(file_links,'file_links')
        article = []
        for file_link in file_links:
            print(file_link)
            result = self._get_context_from_jq_url(file_link)
            xx = self._extra_text(result)
            article.append(xx)

        file_path = f"/Users/zhaoxuefeng/GitHub/obsidian/工作/日记/{date}.md"
        with open(file_path,'a') as f:
            f.write("\n\n# 今日资讯\n---\n## 消息\n" +'\n\n---\n## 消息\n'.join(article))
