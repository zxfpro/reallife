""" 领取任务"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reallife.get_task import receive
# 将项目根目录添加到 Python 路径

if __name__ == "__main__":
    print(receive())