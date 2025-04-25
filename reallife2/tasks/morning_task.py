
def morning():
    result = record_thinking()
    if result:
        return result
    result = record_weight()
    if result:
        return result
    result = running()
    if result:
        return result
    result = record_eatning()
    if result:
        return result
    result = clean_face()
    if result:
        return result
    result = clean_room()
    if result:
        return result
    

