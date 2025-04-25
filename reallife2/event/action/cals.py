
from reallife2.utils.llm_utils import read_file, logging, parse_execution_pool, update_calulate, generate_schedule

# 主程序入口
def sync_calulate_func():
    # 参数配置
    obsidian = "/Users/zhaoxuefeng/GitHub/obsidian"
    file_path = f"{obsidian}/工作/事件看板/事件看板.md"
    p = '2025年'

    # 读取文件
    text = read_file(file_path)

    if not text:
        logging.error("文件内容为空，无法解析执行池")
        return

    # 解析执行池
    execution_pool = parse_execution_pool(text)

    if execution_pool:
        logging.debug("解析到的执行池内容:\n{}".format(execution_pool))
        # 生成日程安排
        schedule_result = generate_schedule(execution_pool,habit ="7点-9点起床洗漱, 12点到14点吃饭+午休,19点以后就是自由时间")
        xx = [i for i in schedule_result.split('\n') if i!='']
        for xp in xx:
            v = [(p+k if i<2 else k) for i,k in enumerate(xp.split('$'))]
            v[0]
            v[1]
            v[2]
            update_calulate(*v)

    else:
        logging.error("未能解析到执行池内容")

if __name__ == "__main__":
    sync_calulate_func()
