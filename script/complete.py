""" 完成任务"""
import sys
import os
# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reallife.get_task import complete

if __name__ == "__main__":
    print(complete())