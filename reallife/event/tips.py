"""提供一些带状态的消息"""

from .utils import Date, create_func

date_c = Date()
date = date_c.date


record_thinking = create_func(task='记录灵感',date=date)
record_weight = create_func(task='记录体重',date=date)
running = create_func(task='跑步',date=date)
record_eatning = create_func(task='记录吃了什么',date=date)
clean_face = create_func(task='洗漱护肤',date=date)
clean_room = create_func(task='收拾家与锻炼',date=date)
# start_work
ding_morning = create_func(task='上班打卡',date=date)
change_frist = create_func(task='调整优先级',date=date)
update_to_cal = create_func(task='上传到日历',date=date)
# tasks
write_thinking = create_func(task='写下灵感',date=date)
update_state_pause = create_func(task='跟进阻塞池',date=date)
# finish_work
check_news = create_func(task='检查和收集咨询',date=date)
check_chan = create_func(task='检查是否仍在禅模式',date=date)
git_push_check = create_func(task='检测git提交',date=date)
ding_evening = create_func(task='下班打卡',date=date)
# evening
clean_cat_ning = create_func(task='整理家里和猫猫',date=date)
clean_ning = create_func(task='晚上洗漱,刷牙,护肤',date=date)
exercise = create_func(task='锻炼',date=date)
sleep = create_func(task='睡觉',date=date)
