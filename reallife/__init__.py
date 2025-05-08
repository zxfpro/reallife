""" 初始化 设定值"""
from .utils2 import Date
from .utils import load_config
from llmada import BianXieAdapter
from .utils2 import Setting

# Load configuration
config = load_config()
KANBAN_PATH = config.get('KANBAN_PATH', '')
WORK_CANVAS_PATH = config.get('WORK_CANVAS_PATH', [])

setting = Setting()
llm = BianXieAdapter()
llm.set_model("gpt-4.1-mini")
setting.llm = llm
setting.debug = False

# Date(date = '2025-01-01',time = '14:40:10')
Date()
