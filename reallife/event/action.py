
from reallife.utils.manager_utils import status, Date
date_c = Date()
date = date_c.date
# 同步预备池

from grapherz.canvas.core import Canvas,Color
from kanban.core import Pool,Kanban
import requests

from llama_index.core import PromptTemplate
import subprocess
import os
from datetime import datetime

from bs4 import BeautifulSoup
from llama_index.llms.openai import OpenAI
from functools import lru_cache
from reallife.utils.llm_utils import read_file, logging, parse_execution_pool, generate_schedule, parse_execution_jiangyou_pool





class KanBanManager():
    def __init__(self):
        self.kanban_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md"
        self.pathlib = ["/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas",
                        "/工程系统级设计/项目级别/数字人生/DigitalLife/DigitalLife.canvas",
                        "/工程系统级设计/项目级别/自动化工作/coder/coder.canvas",]
        

    def _encode(self,i,project_name):
        return project_name+'-'+i

    def _save_in_pauses(self,i,pauses):
        for pause in pauses:
            if i.get('text') in pause:
                return True
        return False

    def toReady(self,canvas_path:str,kanban_path:str):
        project_name = canvas_path.rsplit('/',2)[-2] 

        canvas = Canvas(file_path=canvas_path)
        kanban = Kanban(kanban_path)
        kanban.pull()
        pauses = kanban.get_tasks_in(pool=Pool.阻塞池)
        readys = kanban.get_tasks_in(pool=Pool.预备池)

        nodes = [i.get('text') or '' for i in canvas.select_by_color(Color.yellow,type='node') if not self._save_in_pauses(i,pauses=pauses)]
        for i in nodes:
            if i not in readys:
                kanban.insert(text=self._encode(i,project_name),pool=Pool.预备池)
        kanban.push()

        return 'success'
    
    def _give_a_task_time(self,task:str)->str:
        return "2P " + task
    
    def _get_weight(self,date):
        url = f"http://101.201.244.227:8000/weight/{date}"
        response = requests.get(url)
        return response.json().get('weight')
    
    def sync_ready(self):
        for path in self.pathlib:
            self.toReady(canvas_path="/Users/zhaoxuefeng/GitHub/obsidian/工作"+path,
                    kanban_path =self.kanban_path)
        return 'success'
    
    def sync_order(self):
        kanban = Kanban(self.kanban_path)
        kanban.pull()
        
        tasks = kanban.get_tasks_in(Pool.预备池)
        order_tasks = kanban.get_tasks_in(Pool.就绪池)
        orders = ' '.join(order_tasks)
        for task in tasks:
            kanban.pop(text = task,pool = Pool.预备池)
            if task not in orders:
                task_ = self._give_a_task_time(task)
                kanban.insert(text=task_,pool=Pool.就绪池)

        kanban.push()
        return 'success'
    
    def sync_run(self)->str:
        kanban = Kanban(self.kanban_path)
        kanban.pull()

        tasks = kanban.get_tasks_in(Pool.就绪池)
        all_task_time = 0
        for task in tasks:
            task_time = int(task.split(' ')[0][:-1])

            if all_task_time + task_time <=14:
                all_task_time += task_time
                kanban.pop(text=task,pool=Pool.就绪池)
                kanban.insert(text=task,pool=Pool.执行池)

            elif all_task_time < 8:
                pass
        kanban.push()
        return 'success'
    
    def sync_run2order(self,task):
        kanban = Kanban(self.kanban_path)
        kanban.pull()

        task_ = kanban.select_by_word(task)[0] # select_by_word_in
        kanban.pop(inputs=task_,by='description',pool=Pool.执行池)
        kanban.insert(text=task_,pool=Pool.就绪池)
        kanban.push()
        return 'success'

    def sync_run2over(self,task:str,
                      canvas_path:str):

        """从执行池添加到完成池
        # multi_line_input = "备案-新域名做域名备案$/工程系统级设计/项目级别/数字人生/模拟资质认证/模拟资质认证.canvas\n"

        1 将task从执行池添加到完成池
        2 将canvas 中的颜色变绿
        Args:
            kanban_path (str): 看板路径

        Returns:
            None: None
        """
        kanban_path =self.kanban_path
        canvas_path = canvas_path.replace('\n','')
        canvas_path ="/Users/zhaoxuefeng/GitHub/obsidian/工作"+canvas_path


        kanban = Kanban(kanban_path)
        kanban.pull()
        task = task.split('-',1)[-1]
        if len(kanban.get_task_by_word(task,pool=Pool.执行池)) == 0:
            kanban.insert(text=task,pool=Pool.完成池)
            kanban.push()
            return 'failed'
            
        task_ = kanban.get_task_by_word(task,pool=Pool.执行池)[0]
        kanban.pop(text=task_,pool=Pool.执行池)
        kanban.insert(text=task_,pool=Pool.完成池)
        
        # and
        canvas = Canvas(file_path=canvas_path)
        tasks = canvas.select_nodes_by_text(task)
        try:
            tasks[0].color = Color.green.value
        except IndexError as e:
            return f'error: {e}'
        canvas.to_file(canvas_path)
        kanban.push()
        return 'success'


    def add_tips(self,task:str,kanban_path:str):
        """从执行池添加到完成池
        1 将task从执行池添加到完成池
        2 将canvas 中的颜色变绿
        Args:
            kanban_path (str): 看板路径

        Returns:
            None: None
        """
        kanban_path = self.kanban_path
        kanban = Kanban(kanban_path)
        kanban.pull()

        kanban.insert(text=task,pool=Pool.酱油池)
        kanban.push()
        return 'success'


    def sync_weight(self,date)->str:
        result = self._get_weight(date)
        x = f"""---
番茄: 14
体重: {result}
---
"""
        with open(f'/Users/zhaoxuefeng/GitHub/obsidian/工作/日记/{date}.md','a') as f:
            f.write(x)
        return 'success'


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

    def _get_context_from_jq_url(self,url):
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
    def _extra_text(self,text):
        llm = OpenAI(
            model="gpt-4o",
            api_key=os.getenv("BIANXIE_API_KEY"),
            api_base='https://api.bianxieai.com/v1',
            temperature=0.1,
        )
        resp = llm.complete(f"""
        我希望你可以对一个内容进行汇总和总结, 我会给你一段网页的内容，你来用一些简短的文字告诉我这篇内容的主要信息, 以及列出其中相关的重点和链接

        网页内容:
        ---
        {text}
        ---

        输出信息:
        """)
        return resp.text

    def _get_articlie_link(self):
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

    def sync_calulate(self):

        # 读取文件
        text = read_file(self.kanban_path)

        if not text:
            logging.error("文件内容为空，无法解析执行池")
            return

        # 解析执行池
        execution_pool = parse_execution_pool(text)

        if execution_pool:
            logging.debug("解析到的执行池内容:\n{}".format(execution_pool))
            # 生成日程安排
            schedule_result = generate_schedule(execution_pool,habit =self.habit)
            xx = [i for i in schedule_result.split('\n') if i!='']
            for xp in xx:
                v = [(self.year+k if i<2 else k) for i,k in enumerate(xp.split('$'))]
                self._update_calulate(*v)

        else:
            logging.error("未能解析到执行池内容")

    def sync_notes(self):
        # 读取文件
        text = read_file(self.kanban_path)
        # 解析执行池
        execution_pool = parse_execution_jiangyou_pool(text)

        # 生成日程安排
        current_utc_time = datetime.utcnow()
        schedule_result = str(current_utc_time)[:10] + '\n' + execution_pool

        self._write_notes(schedule_result)

    def sync_news(self,date:str):
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


@status(task="同步体重",date=date,run_only=True)
def sync_weight():
    kanb = KanBanManager()
    kanb.sync_weight(date)

@status(task="同步预备池",date=date,run_only=True)
def sync_ready_pool()->str:
    kanb = KanBanManager()
    kanb.sync_ready()

@status(task="同步就绪池",date=date,run_only=True)
def sync_order_pool()->str:
    kanb = KanBanManager()
    kanb.sync_order()

@status(task="同步执行池",date=date,run_only=True)
def sync_run_pool()->str:
    kanb = KanBanManager()
    kanb.sync_run()

@status(task="同步日历",date=date,run_only=True)
def sync_calulate()->str:
    appio = APPIO()
    appio.sync_calulate()


@status(task="同步备忘录",date=date,run_only=True)
def sync_note()->str:
    appio = APPIO()
    appio.sync_notes()


@status(task="收集资讯",date=date,run_only=True)
def sync_news()->str:
    appio = APPIO()
    appio.sync_news(date)




# prompt = """
# 你是一个计划构筑师,根据我的任务帮我拆分编写工作流程与计划, 使用mermaid 的方式构建.

# 注意: 相对简明, mermaid格式简单,清晰

# ---
# 任务:
# {任务}

# """



# import requests
# from bs4 import BeautifulSoup
# import os
# # 配置相关
# from llama_index.llms.openai import OpenAI

# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# from functools import lru_cache


# # 初始化 LLM 和 Embedding 模型
# llm = OpenAI(
#     model="gpt-4.1-2025-04-14",
#     api_key=os.getenv("BIANXIE_API_KEY"),
#     api_base='https://api.bianxieai.com/v1',
#     temperature=0.1,
# )
# obsidian = "/Users/zhaoxuefeng/GitHub/obsidian"

# def main(task:str):
#     return llm.complete(prompt.format(任务=task))



# if __name__ == "__main__":
#     import sys
#     multi_line_input = sys.stdin.read()
#     print(main(multi_line_input))