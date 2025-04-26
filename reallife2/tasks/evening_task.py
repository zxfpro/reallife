from reallife2.event


def check_(func):
    result = func()
    if result:
        return result


def close():
    check_(git_push_check)
    check_(ding_evening)

def evening():
    check_(clean_cat_ning)
    check_(clean_ning)
    check_(exercise)
    check_(sleep)


# def close():
#     # 知识库整理
#     # 检查和收集咨询
#     # 检查是否仍在禅模式
#     # 执行池为完成的内容回归到就绪池
#     # 同步酱油池
#     result = git_push_check()
#     if result:
#         return result

#     result = ding_evening()
#     if result:
#         return result
    
# def evening():
#     result = clean_cat_ning()
#     if result:
#         return result
    
#     result = clean_ning()
#     if result:
#         return result
    
#     result = exercise()
#     if result:
#         return result
    
#     result = sleep()
#     if result:
#         return result
