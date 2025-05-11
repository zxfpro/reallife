import sys
import os
# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest


from reallife.action.appiotools import APPIO
from reallife.action.kanbantools import KanBanManager
from reallife.action.scripts import *
from reallife import Date


class Test_APPIO():

    @pytest.mark.skip(reason='#TODO')
    def test_sync_news(self):
        appio = APPIO()
        appio.sync_news(Date().date)

    @pytest.mark.skip(reason='#TODO')
    def test_sync_calulate(self):
        appio = APPIO()
        appio.sync_calulate()

    @pytest.mark.skip(reason='通过')
    def test_sync_notes(self):
        appio = APPIO()
        appio.sync_notes()

class Test_KanBan():

    @pytest.mark.skip(reason='通过')
    def test_sync_ready(self):
        """同步到预备池
        """ 
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        kanb.sync_ready()

    @pytest.mark.skip(reason='通过')
    def test_sync_order(self):
        """同步到就绪池
        """ 
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        kanb.sync_order()

    @pytest.mark.skip(reason='通过')
    def test_sync_run(self):
        """同步到执行池
        """ 
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        kanb.sync_run()

    @pytest.mark.skip(reason='通过')
    def test_sync_run2order(self):
        """从执行池未完成的迁移回就绪池
        """ 
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        kanb.sync_run2order()

    @pytest.mark.skip(reason='暂时不执行')
    def test_sync_run2over(self):
        """从执行池迁移到完成池
        """ 
        # TODO 将信息融到task中
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        kanb.sync_run2over(task='')


    @pytest.mark.skip(reason='通过')
    def test_add_tips(self):
        """增加随笔到预备池

        """ 
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        task = "你好 测试"
        kanb.add_tips(task)

    @pytest.mark.skip(reason='通过')
    def test_sync_weight(self):
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        kanb.sync_weight(Date().date)

class Test_Script():

    @pytest.mark.skip(reason='通过')
    def test_give_a_task_time(self):
        result = give_a_task_time(task='修复资讯功能')
        assert result[1:] == "P 修复资讯功能"


    @pytest.mark.skip(reason='暂时不执行')
    # @pytest.mark.run(order=1) @pytest.mark.run(order=2)
    def test_generate_schedule(self):
        """同步到就绪池
        """ 
        generate_schedule(text, habit)
        

    @pytest.mark.skip(reason='通过')
    def test_judge_type(self):
        task = "修复资讯功能"
        result = judge_type(task)
        print(result)

    @pytest.mark.skip(reason='暂时不执行')
    def test_run_applescript(self):
        # run_applescript
        # run_shortcut
        pass

    @pytest.mark.skip(reason='通过')
    def test_write_notes(self):
        write_notes('content')

    @pytest.mark.skip(reason='通过')
    def test_write_reminder(self):
        write_reminder('如何使测试')

    @pytest.mark.skip(reason='通过')
    def test_update_calulate(self):
        update_calulate()

    @pytest.mark.skip(reason='通过')
    def test_get_choice_from_applescript(self):
        get_choice_from_applescript()

    @pytest.mark.skip(reason='通过')
    def test_display_dialog(self):
        display_dialog('我的','你的')
        display_dialog_for_end('我的','你的')

    @pytest.mark.skip(reason='暂时不执行')
    def test_uget_page_html(self):
        kanb = KanBanManager(kanban_path = "/Users/zhaoxuefeng/GitHub/obsidian/工作/事件看板/事件看板.md",
                             pathlib = ["/工程系统级设计/能力级别/grapher/grapher.canvas","/工程系统级设计/能力级别/kanban/kanban.canvas"])
        kanb.add_tips(task)


