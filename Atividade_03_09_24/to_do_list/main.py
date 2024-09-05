import list as l
import interface as i

return_menu = True
list = []
i.welcome()

while return_menu == True:
    menu = i.menu()
    match menu :
        case 1:
            i.show_list(list)
            value = i.add_task()
            list = l.add_task(list, value)
        case 2:
            i.show_list(list)
        case 3:
            i.show_list(list)
            remove = i.remove_task()
            list = l.remove_task(list, remove)
        case 4:
            print("Lista reiniciada")
            list = l.reset_list()
        case 5: 
            i.thanks()
            return_menu = False