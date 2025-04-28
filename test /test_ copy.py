import sys
import os
# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import re
import pytest

from reallife.get_task import pull, push


def test_pull_push():
    print(pull())
    push()






# from reallife.status.action import *
# from reallife.status.info import *
# from reallife.status.news import sync_news_func
# from reallife.status.utils import Date

# date_c = Date()
# date = date_c.date
# time = date_c.time

# class Test_Action():
#     @pytest.mark.skip(reason='暂时不执行')
#     def test_sync_ready_pool(self):
#         sync_ready_pool()

#     @pytest.mark.skip(reason='暂时不执行')
#     def test_sync_order_pool(self):
#         sync_order_pool()

#     @pytest.mark.skip(reason='暂时不执行')
#     def test_sync_run_pool(self):
#         sync_run_pool()
#     @pytest.mark.skip(reason='暂时不执行')
#     def test_sync_news(self):
#         sync_news_func(date)

#     @pytest.mark.skip(reason='暂时不执行')
#     def test_sync_note(self):
#         sync_note()

#     @pytest.mark.skip(reason='暂时不执行')
#     def test_sync_weight(self):
#         sync_weight()

# class Test_Info():
#     @pytest.mark.skip(reason='暂时不执行')
#     def test_record_thinking(self):
#         record_thinking()
