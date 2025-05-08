import sys
import os
# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import re
import pytest

from reallife.core import receive,complete





from reallife.utils2 import Date
from reallife.action.action import sync_calulate,sync_weight,sync_ready_pool,sync_order_pool,APPIO
from reallife.action.action import sync_run_pool, sync_note, sync_news, sync_note_night

from reallife.nodes import clean_and_update,edit_coder
from reallife.nodes import design, meeting_and_talk, judge_type
from reallife.nodes import task_failed,task_complete

from reallife.utils2 import run_shortcut, display_dialog



date_c = Date()
date = date_c.date
time = date_c.time

class Test_Action():
    @pytest.mark.skip(reason='暂时不执行')
    def test_sync_ready_pool(self):
        sync_ready_pool()

    @pytest.mark.skip(reason='暂时不执行')
    def test_sync_order_pool(self):
        sync_order_pool()

    @pytest.mark.skip(reason='暂时不执行')
    def test_sync_run_pool(self):
        sync_run_pool()

    @pytest.mark.skip(reason='暂时不执行')
    def test_sync_news(self):
        sync_news_func(date)

    # @pytest.mark.skip(reason='暂时不执行')p
    def test_sync_note(self):
        appio = APPIO()
        appio.sync_notes()

    @pytest.mark.skip(reason='暂时不执行')
    def test_sync_weight(self):
        sync_weight()

class Test_Info():
    @pytest.mark.skip(reason='暂时不执行')
    def test_record_thinking(self):
        record_thinking()
