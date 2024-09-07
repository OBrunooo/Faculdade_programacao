from .list import *
from .interface import *

def to_do_list():
    return_menu = True
    list = []
    welcome()

    while return_menu == True:
        menu = select_menu()
        match menu :
            case 1:
                show_list(list)
                value = add_task()
                list = add_task_to_list(list, value)
            case 2:
                show_list(list)
            case 3:
                show_list(list)
                remove = remove_task()
                list = remove_task_to_list(list, remove)
            case 4:
                print("Lista reiniciada")
                list = reset_list()
            case 5: 
                thanks()
                return_menu = False