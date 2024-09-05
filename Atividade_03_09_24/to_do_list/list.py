def add_task (list, task):
    list.append(task)
    return list

def reset_list ():
    return []

def remove_task (list, task):
    del list[task - 1]
    return list