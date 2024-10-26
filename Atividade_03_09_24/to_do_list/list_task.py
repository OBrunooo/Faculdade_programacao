def add_task_to_list (list, task):
    list.append(task)
    return list

def reset_list ():
    return []

def remove_task_to_list (list, task):
    del list[task - 1]
    return list