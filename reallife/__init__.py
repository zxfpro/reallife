""" 初始化 设定值"""

from llmada import BianXieAdapter
from .utils import Setting, load_config, Date
# Load configuration
config = load_config()
KANBAN_PATH = config.get('KANBAN_PATH', '')
WORK_CANVAS_PATH = config.get('WORK_CANVAS_PATH', [])

setting = Setting()
llm = BianXieAdapter()
llm.set_model("gemini-2.5-flash-preview-04-17-nothinking")
setting.llm = llm
setting.debug = True

Date(date = '2025-05-08',time = '09:40:10')
# Date()