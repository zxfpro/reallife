import sys
import os
# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from reallife2.get_task import pull

if __name__ == "__main__":
    print(pull())