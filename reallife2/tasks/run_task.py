from reallife2.event.tips.task import write_thinking

def check_(func):
    result = func()
    if result:
        return result
    


def tasks():
    check_(write_thinking)
