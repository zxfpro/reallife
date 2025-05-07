""" 初始化 设定值"""
from .event.utils import Date
# Date(date = '2025-01-01',time = '14:40:10')
Date()




import os
import yaml

# Load configuration from YAML file
def load_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# Load configuration
config = load_config()
KANBAN_PATH = config.get('KANBAN_PATH', '')
WORK_CANVAS_PATH = config.get('WORK_CANVAS_PATH', [])


from llmada import BianXieAdapter
from .event.utils import Setting
setting = Setting()

llm = BianXieAdapter()
llm.set_model("gpt-4.1-mini")
setting.llm = llm




