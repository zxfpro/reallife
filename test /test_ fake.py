import sys
import os
# 将项目根目录添加到 Python 路径
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import re
import pytest


from reallife.core import receive,complete

# 将项目根目录添加到 Python 路径
@pytest.mark.skip('wait')
def test_receive():
    print(receive())

@pytest.mark.skip('wait')
def test_complete():
    print(complete())

