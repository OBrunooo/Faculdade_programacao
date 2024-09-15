from to_do_list import interface as i
from to_do_list import list_task as l



def to_do_list():
    return_menu = True
    list = []
    i.welcome()

    while return_menu == True:
        menu = i.select_menu()
        match menu :
            case 1:
                i.show_list(list)
                value = i.add_task()
                list = l.add_task_to_list(list, value)
            case 2:
                i.show_list(list)
            case 3:
                i.show_list(list)
                remove = i.remove_task()
                list = l.remove_task_to_list(list, remove)
            case 4:
                print("Lista reiniciada")
                list = l.reset_list()
            case 5: 
                i.thanks()
                return_menu = False