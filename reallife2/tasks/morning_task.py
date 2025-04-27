from reallife2.event.tips.morning import record_thinking,record_weight, running, record_eatning, clean_face, clean_room

def check_(func):
    result = func()
    if result:
        return result
    
def morning():
    check_(record_thinking)
    check_(record_weight)
    check_(running)
    check_(record_eatning)
    check_(clean_face)
    check_(clean_room)
